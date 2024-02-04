from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import DatetimeOutputParser
from langchain.schema import HumanMessage

output_parser = DatetimeOutputParser()

chat = ChatOpenAI(model="gpt-3.5-turbo")

prompt = PromptTemplate.from_template("When is the release date of {product}")

result = chat(
    [
        HumanMessage(content=prompt.format(product="iPhone8")),
        HumanMessage(content=output_parser.get_format_instructions())
    ]
)

print(result.content)
