from langchain_experimental.tools import PythonREPLTool
from langchain.chains import LLMMathChain
from langchain.agents import Tool
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain_openai import OpenAI
from langchain.tools import DuckDuckGoSearchRun

llm = OpenAI()
tools = [PythonREPLTool()]

llm_math_chain = LLMMathChain(llm=llm, verbose=True)

tools.append(
   Tool(
       name="Calculator",
       func=llm_math_chain.run,
       description="useful when you need to answer questions about math",
   )
)

search = DuckDuckGoSearchRun()
tools.append(
    Tool(
        name="duckduckgo-search",
        func=search.run,
        description="useful when you need to search or latest information in web",
    )
)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("""
現在の20代の日本人男性の平均身長を教えて。
そして、私の身長は168cmなため、日本全国から見た時の差を2乗した結果を教えて。
""")
