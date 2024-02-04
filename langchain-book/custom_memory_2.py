import chainlit as cl
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory

chat = ChatOpenAI(model="gpt-3.5-turbo")
memory = ConversationSummaryMemory(return_messages=True, llm=chat)
chain = ConversationChain(memory=memory, llm=chat)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Input messages").send()

@cl.on_message
async def on_message(message: str):
    messages = chain.memory.load_memory_variables({})["history"]
    print(f"Number of messages: {len(messages)}")
    for saved_message in messages:
        print(saved_message.content)
    result = chain(message.content)
    await cl.Message(content=result["response"]).send()
