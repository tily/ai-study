from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

chat = ChatOpenAI()
memory = ConversationBufferMemory(return_messages=True)
chain = ConversationChain(memory=memory, llm=chat, verbose=True)
print(chain("こんにちは、黒猫は好きですか？")["response"])
