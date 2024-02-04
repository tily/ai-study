import os
import chainlit as cl
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import RedisChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage

chat = ChatOpenAI(model="gpt-3.5-turbo")


@cl.on_chat_start
async def on_chat_start():
    thread_id = None
    while not thread_id:
        res = await cl.AskUserMessage(content="I'm context bot, please input thread id", timeout=600).send()
        if res:
            thread_id = res["output"]
    history = RedisChatMessageHistory(
        session_id=thread_id,
        url=os.environ.get("REDIS_URL"),
    )
    memory = ConversationBufferMemory(return_messages=True, chat_memory=history)
    chain = ConversationChain(memory=memory, llm=chat)

    memory_message_result = chain.memory.load_memory_variables({})
    messages = memory_message_result["history"]
    for message in messages:
        if isinstance(message, HumanMessage):
            await cl.Message(author="User", content=f"{message.content}").send()
        else:
            await cl.Message(author="ChatBot", content=f"{message.content}").send()
    cl.user_session.set("chain", chain)

@cl.on_message
async def on_message(message: str):
    chain = cl.user_session.get("chain")
    result = chain(message.content)
    await cl.Message(content=result["response"]).send()
