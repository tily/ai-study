from langchain_openai.chat_models import ChatOpenAI
from langchain.output_parsers import OutputFixingParser
from langchain.output_parsers import PydanticOutputParser
from langchain.schema import HumanMessage
from pydantic import BaseModel, Field, field_validator

chat = ChatOpenAI()

class SmartPhone(BaseModel):
    release_date: str = Field(description="The release date of the smartphone")
    screen_inches: float = Field(description="The size of the smartphone in inches")
    os_installed: str = Field("The OS installed into the smartphone")
    model_name: str = Field(description="The model name of the smartphone")

    @field_validator("screen_inches")
    def validate_screen_inches(cls, field):
        if field <= 0:
            raise ValueError("Screen inches must be a positive number")
        return field

parser = OutputFixingParser.from_llm(
    parser=PydanticOutputParser(pydantic_object=SmartPhone),
    llm=chat
)

print(parser.get_format_instructions())

result = chat([
    HumanMessage(content="Please tell me a smartphone with Android installed"),
    HumanMessage(content=parser.get_format_instructions())
])

parsed_result = parser.parse(result.content)
print(f"Model Name: {parsed_result.model_name}")
print(parsed_result.screen_inches)
print(parsed_result.os_installed)
print(parsed_result.model_name)
