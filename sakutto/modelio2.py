from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

prompt = PromptTemplate(
    template="{topic}について100文字で教えて。",
    input_variables=["topic"],
)
llm = OpenAI(model="gpt-3.5-turbo-instruct")
print(llm(prompt.format(topic="ビートメイキング")))
