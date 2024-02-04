from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI
from langchain.tools.file_management import WriteFileTool

chat = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
tools = load_tools(["requests_get", "serpapi"], llm=chat)
tools.append(WriteFileTool(root_dir="./"))
agent = initialize_agent(tools, chat, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
result = agent.run("北海道の名産品を調べて日本語で result.txt というファイルに保存して。")
print(f"実行結果: {result}")

