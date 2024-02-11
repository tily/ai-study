from datetime import datetime
import logging
import os
import sys
from slack_bolt.app.async_app import AsyncApp
from slack_bolt.adapter.socket_mode.async_handler import AsyncSocketModeHandler
from langchain.memory import ChatMessageHistory
from langchain.memory import ConversationTokenBufferMemory
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import Tool
from langchain.agents import initialize_agent
from langchain.agents import AgentType

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_USER_ID = os.environ["SLACK_BOT_USER_ID"]
CONVERSATION_MAX_TOKEN = int(os.environ["CONVERSATION_MAX_TOKEN"])
OPENAI_MODEL = os.environ.get("OPENAI_MODEL") or "gpt-3.5-turbo"
LOADING_MESSAGE = os.environ.get("LOADING_MESSAGE") or ":running: お待ちください…"

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
app = AsyncApp(token=SLACK_BOT_TOKEN)
llm = ChatOpenAI(model=OPENAI_MODEL)
tools = [
        Tool(
            name="duckduckgo-search",
            func=DuckDuckGoSearchRun().run,
            description="useful when you need to search or latest information in web",
        ),
]
agent = initialize_agent(tools, llm, agent="chat-zero-shot-react-description", verbose=True)

def convert_messages_to_memory(messages):
    history = ChatMessageHistory()

    for message in messages:
        if message["user"] == SLACK_BOT_USER_ID:
            history.add_ai_message(message["text"]) 
        else:
            history.add_user_message(message["text"]) 

    return ConversationTokenBufferMemory(
        llm=llm,
        chat_memory=history,
        max_token_limit=CONVERSATION_MAX_TOKEN,
        memory_key="chat_history",
        return_messages=True,
    )


@app.event("app_mention")
async def app_mention(ack, event, client, say, logger):
    logger.info(event)

    thread_ts = event["ts"]
    if "thread_ts" in event:
        thread_ts = event["thread_ts"]
    said = await say(text=LOADING_MESSAGE, thread_ts=thread_ts)

    messages = [event]
    if "thread_ts" in event:
        messages = (await client.conversations_replies(
            channel=event["channel"],
            ts=event["thread_ts"],
        ))["messages"]

    memory = convert_messages_to_memory(messages)
    agent = initialize_agent(tools, llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)
    text = agent.run(event["text"])
    await client.chat_update(channel=event["channel"], ts=said["ts"], text=text)

async def main():
    handler = AsyncSocketModeHandler(app, SLACK_APP_TOKEN)
    await handler.start_async()

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
