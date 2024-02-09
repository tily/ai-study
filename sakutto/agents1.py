from langchain_experimental.tools import PythonREPLTool
from langchain.chains import LLMMathChain
from langchain.agents import Tool
from langchain_openai import OpenAI

llm = OpenAI()
llm_math_chain = LLMMathChain(llm=llm, verbose=True)
tools = [PythonREPLTool()]

tools.append(
   Tool(
       name="Calculator",
       func=llm_math_chain.run,
       description="useful when you need to answer questions about math",
   )
)

print(tools)
print(len(tools))
