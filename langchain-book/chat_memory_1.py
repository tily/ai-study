import chainlit as cl
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage

chat = ChatOpenAI(model="gpt-3.5-turbo")
memory = ConversationBufferMemory(return_messages=True)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="I can understand contexts. Input messages").send()

@cl.on_message
async def on_message(message: str):
    memory_message_result = memory.load_memory_variables({})
    messages = memory_message_result["history"]
    messages.append(HumanMessage(content=message.content))
    result = chat(messages)
    memory.save_context(
        {
            "input": message.content,
        },
        {
            "output": result.content,
        }
    )
    await cl.Message(content=result.content).send()
