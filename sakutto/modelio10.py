from typing import List
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain.output_parsers import (
    PydanticOutputParser,
    OutputFixingParser,
)

class Job(BaseModel):
    name: str = Field(description="Name of the job")
    skill_list: List[str] = Field(description="List of skills required for that job")

parser = PydanticOutputParser(pydantic_object=Job)
misformatted = "name is doctor, skills are communication and medical knowledge"

new_parser = OutputFixingParser.from_llm(parser=parser, llm=ChatOpenAI())
print(new_parser.parse(misformatted))
