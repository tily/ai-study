from typing import List
from pydantic import BaseModel, Field
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.output_parsers import PydanticOutputParser

class Job(BaseModel):
    name: str = Field(description="Name of the job")
    skill_list: List[str] = Field(description="List of skills required for that job")

parser = PydanticOutputParser(pydantic_object=Job)

prompt = PromptTemplate(
    template="{query}\n{format_instructions}",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
_input = prompt.format_prompt(query="悪魔の病気を治す職業は")
print(_input)

print(OpenAI()(_input.to_string()))
