from langchain.callbacks import StdOutCallbackHandler
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI()
prompt = PromptTemplate.from_template("1 + {number} = ")
handler = StdOutCallbackHandler()
#chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
chain = LLMChain(llm=llm, prompt=prompt, callbacks=[handler])
print(chain.run(number=2))
