from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

llm = OpenAI()
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=memory,
)

conversation("DI とは何か？")
print(conversation("VI とは何か？"))
