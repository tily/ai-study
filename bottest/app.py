from datetime import datetime
import logging
import os
import sys
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain.chains import ConversationChain
from langchain.memory import ChatMessageHistory
from langchain.memory import ConversationTokenBufferMemory
from langchain_openai import ChatOpenAI

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_BOT_USER_ID = os.environ.get("SLACK_BOT_USER_ID")
SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN")

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
app = App(token=SLACK_BOT_TOKEN)

def convert_messages_to_chain(messages):
    llm = ChatOpenAI(model="gpt-4")
    history = ChatMessageHistory()

    for message in messages:
        if message["user"] == SLACK_BOT_USER_ID:
            history.add_ai_message(message["text"]) 
        else:
            history.add_user_message(message["text"]) 

    memory = ConversationTokenBufferMemory(
        llm=llm,
        chat_memory=history,
        max_token_limit=5000,
    )

    return ConversationChain(memory=memory, llm=llm, verbose=False)

@app.event("app_mention")
def app_mention(ack, event, client, say, logger):
    logger.info(event)

    thread_ts = event["ts"]
    if "thread_ts" in event:
        thread_ts = event["thread_ts"]
    said = say(text="お待ちください", thread_ts=thread_ts)

    messages = [event]
    if "thread_ts" in event:
        messages = client.conversations_replies(
            channel=event["channel"],
            ts=event["thread_ts"],
        )["messages"]

    chain = convert_messages_to_chain(messages)
    result = chain(event["text"])["response"]
    text = f"<@{event["user"]}> {result}"

    client.chat_update(channel=event["channel"], ts=said["ts"], text=text)

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
