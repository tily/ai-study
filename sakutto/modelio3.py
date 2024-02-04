from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain_openai import OpenAI

examples = [
    {"fruit": "りんご", "color": "red"},
    {"fruit": "バナナ", "color": "yellow"},
    {"fruit": "すもも", "color": "pink"},
]
example_template = """
フルーツ: {fruit}
色: {color}
"""
example_prompt = PromptTemplate(
    template=example_template,
    input_variables=["fruit", "color"],
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="フルーツの色を英語で教えて",
    suffix="フルーツ: {input}\n色:",
    input_variables=["input"],
    example_separator="\n\n",
)

prompt_text = few_shot_prompt.format(input="犬")
print(prompt_text)

llm = OpenAI(model="gpt-3.5-turbo-instruct")
print(llm(prompt_text))
