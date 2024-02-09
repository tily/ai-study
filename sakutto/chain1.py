from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI()
prompt = PromptTemplate(
    template="{job}に一番おすすめのプログラミング言語は？",
    input_variables=["job"],
)
chain = LLMChain(llm=llm, prompt=prompt)
print(chain("医者"))

