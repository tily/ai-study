from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
)

result = chat(
    [
        HumanMessage(content="パスタの作り方教えて"),
        AIMessage(content="{ChatModelからの返答であるパスタの作り方}"),
        HumanMessage(content="英語に訳して"),
    ]
)
print(result.content)
