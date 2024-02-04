from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
)

result = chat(
    [
        HumanMessage(content="よー、元気？"),
    ]
)
print(result.content)
