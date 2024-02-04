import os
import chainlit as cl
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import RedisChatMessageHistory
from langchain.memory import ConversationBufferMemory

chat = ChatOpenAI(model="gpt-3.5-turbo")
history = RedisChatMessageHistory(
    session_id="chat_history",
    url=os.environ.get("REDIS_URL"),
)
memory = ConversationBufferMemory(return_messages=True, chat_memory=history)
chain = ConversationChain(memory=memory, llm=chat)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="I can understand contexts. Input messages").send()

@cl.on_message
async def on_message(message: str):
    result = chain(message.content)
    await cl.Message(content=result["response"]).send()
