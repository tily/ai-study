import os
from langchain.memory import ChatMessageHistory
from langchain.memory import ConversationTokenBufferMemory
from langchain_openai import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun
from langchain.tools import Tool
from langchain.agents import initialize_agent

CONVERSATION_MAX_TOKEN = int(os.environ["CONVERSATION_MAX_TOKEN"])
OPENAI_MODEL = os.environ.get("OPENAI_MODEL") or "gpt-3.5-turbo"

llm = ChatOpenAI(model=OPENAI_MODEL)
tools = [
        Tool(
            name="duckduckgo-search",
            func=DuckDuckGoSearchRun().run,
            description="useful when you need to search or latest information in web",
        ),
]

history = ChatMessageHistory()
history.add_ai_message("Hello")
history.add_user_message("Hello")

memory = ConversationTokenBufferMemory(
    llm=llm,
    chat_memory=history,
    max_token_limit=CONVERSATION_MAX_TOKEN,
)

agent = initialize_agent(tools, llm, agent="chat-zero-shot-react-description", verbose=True)
text = agent.run({"input": "こんにちは", "chat_history":memory.load_memory_variables({})})
print(text)
