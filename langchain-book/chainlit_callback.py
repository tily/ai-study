import chainlit as cl
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
agent = initialize_agent(
  tools=[],
  llm=chat,
  agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
  verbose=True,
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Agent initialized").send()

@cl.on_message
async def on_message(input_message):
    result = agent.run(
        input_message.content,
        callbacks=[
            cl.LangchainCallbackHandler()
        ]
    )
    await cl.Message(content=result.content).send()
