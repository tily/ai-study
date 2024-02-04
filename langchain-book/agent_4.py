from langchain.agents import AgentType, initialize_agent, Tool
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.chat_models import ChatOpenAI
from langchain.retrievers import WikipediaRetriever
from langchain.tools.file_management import WriteFileTool

chat = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
tools = []
tools.append(WriteFileTool(root_dir="./"))

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

agent = initialize_agent(
    tools,
    chat,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

result = agent.run("スコッチウイスキーについて Wikipedia で調べて概要を日本語で result.txt というファイルに保存してください。")

print(f"実行結果: {result}")
