from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI


chat = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo"
)

tools = load_tools(["requests"])

agent = initialize_agent(
    tools=tools,
    llm=chat,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

result = agent.run("""以下の URL にアクセスして東京の天気を調べて日本語で答えてください。
https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json
""")

print(f"実行結果: {result}")
