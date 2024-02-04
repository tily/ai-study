from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

class LogCallbackHandler(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
        print("ChatModel begin execute ...")
        print(f"Input: {messages}")
    def on_chain_start(self, serialized, inputs, **kwargs):
        print("Chain begin execute ...")
        print(f"Input: {messages}")

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    callbacks=[LogCallbackHandler()]
)

result = chat([HumanMessage(content="HellO!")])

print(result.content)
    
