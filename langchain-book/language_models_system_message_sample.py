from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
)

result = chat(
    [
        SystemMessage(content="カタコトで話して。"),
        HumanMessage(content="パスタの作り方教えて"),
    ]
)
print(result.content)
