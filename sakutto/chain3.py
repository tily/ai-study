from langchain_openai import OpenAI
from langchain.chains import (
    LLMChain,
    SimpleSequentialChain,
)
from langchain.prompts import PromptTemplate

llm = OpenAI()

prompt_1 = PromptTemplate(
    template="{job}におすすめのプログラミング言語は何？\nプログラミング言語:",
    input_variables=["job"],
)
chain_1 = LLMChain(llm=llm, prompt=prompt_1)

prompt_2 = PromptTemplate(
    template="{programming_language}の学び方を教えて。",
    input_variables=["programming_language"],
)
chain_2 = LLMChain(llm=llm, prompt=prompt_2)

overall_chain = SimpleSequentialChain(
    chains=[chain_1, chain_2], 
    verbose=True, 
)

print(overall_chain("医者"))
