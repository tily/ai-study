from langchain_openai import ChatOpenAI
from langchain.schema import (SystemMessage, HumanMessage)

chat = ChatOpenAI()
print(chat([
    SystemMessage(content="英語で答えて"),  
    HumanMessage(content="ダルマ落としだ"),
]))
