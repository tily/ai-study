#from langchain.llms import OpenAI
#llm = OpenAI(model="gpt-3.5-turbo-instruct")
from langchain.llms import GPT4All
llm = GPT4All()

result = llm("美味しいラーメンを", stop="。")

print(result)
