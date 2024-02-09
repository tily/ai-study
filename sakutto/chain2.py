from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain

llm = OpenAI()
human_message_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        template="{job}に一番おすすめのプログラミング言語は？",
        input_variables=["job"],
    )
)
chat_message_prompt = ChatPromptTemplate.from_messages([human_message_prompt])
chain = LLMChain(llm=llm, prompt=chat_message_prompt)
print(chain("医者"))
