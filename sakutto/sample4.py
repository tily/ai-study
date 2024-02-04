from langchain.prompts import(
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI

system_template = "あなたは質問者の質問に{language}の言語で回答する人です"
human_template = "質問者: {question}"
system_message_prompt = HumanMessagePromptTemplate.from_template(system_template)
#system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
prompt_message_list = chat_prompt.format_prompt(language="英語", question="お腹すいた").to_messages()
print(prompt_message_list)
chat = ChatOpenAI()
print(chat(prompt_message_list))
