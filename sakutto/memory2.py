from langchain_openai import OpenAI
from langchain.chains import (
    LLMChain,
    SequentialChain,
)
from langchain.prompts import PromptTemplate
from langchain.memory import SimpleMemory

llm = OpenAI()

prompt_1 = PromptTemplate(
    input_variables=["adjective", "job", "time"],
    template="{time}において、{adjective}{job}に一番オススメのプログラミング言語は?\nプログラミング言語：",
)
chain_1 = LLMChain(llm=llm, prompt=prompt_1, output_key="programming_language")

prompt_2 = PromptTemplate(
    input_variables=["programming_language", "time"],
    template="現在は{time}だとします。{programming_language}を学ぶためにやるべきことを3ステップで100文字で教えて。",
)
chain_2 = LLMChain(llm=llm, prompt=prompt_2, output_key="learning_step")

overall_chain = SequentialChain(
    chains=[chain_1, chain_2],
    input_variables=["adjective", "job"],
    output_variables=["programming_language", "learning_step"],
    verbose=True,
    memory=SimpleMemory(memories={"time": "2030年"}),
)
output = overall_chain({
    "adjective": "ベテランの",
    "job": "エンジニア",
})
print(output)
