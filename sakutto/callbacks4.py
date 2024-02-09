from langchain.callbacks import get_openai_callback
from langchain_openai import OpenAI

llm = OpenAI()

with get_openai_callback() as cb:
    result = llm("弁いーキングについて教えて")
    print(result)
    print(cb)
