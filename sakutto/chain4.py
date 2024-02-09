from langchain_openai import OpenAI
from langchain.chains import (
    LLMChain,
    SequentialChain,
)
from langchain.prompts import PromptTemplate

llm = OpenAI()

prompt_1 = PromptTemplate(
    template="{adjective}な{job}におすすめのプログラミング言語は何？\nプログラミング言語:",
    input_variables=["adjective", "job"],
)
chain_1 = LLMChain(llm=llm, prompt=prompt_1, output_key="programming_language")

prompt_2 = PromptTemplate(
    template="{programming_language}の学び方を教えて。",
    input_variables=["programming_language"],
)
chain_2 = LLMChain(llm=llm, prompt=prompt_2, output_key="learning_step")

overall_chain = SequentialChain(
    chains=[chain_1, chain_2],
    input_variables=["adjective", "job"],
    output_variables=["programming_language", "learning_step"],
    verbose=True, 
)

print(overall_chain({"job": "医者", "adjective": "新米"}))
