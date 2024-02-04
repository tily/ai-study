from langchain.agents import AgentType, initialize_agent, Tool
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.retrievers import WikipediaRetriever

chat = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
tools = []

retriever = WikipediaRetriever(
    lang="ja",
    doc_content_chars_max=500,
    top_k_results=1,
)

tools.append(
    create_retriever_tool(
        name="WikipediaRetriever",
        description="受け取った単語に関する Wikipedia の記事を取得できる",
        retriever=retriever,
    )
)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
)

agent = initialize_agent(
    tools,
    chat,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
)

result = agent.run("スコッチウイスキーについて Wikipedia で調べて概要を日本語でまとめてください。")

print(f"実行結果: {result}")

result_2 = agent.run("以前の指示をもう一度実行してください。")

print(f"実行結果: {result_2}")
