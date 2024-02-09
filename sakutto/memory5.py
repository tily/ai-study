from langchain.memory import ConversationBufferMemory
from langchain import OpenAI, LLMChain, PromptTemplate

template = """あなたはにんげんと話す妖怪チャットぼっとだよ。

{chat_history}
Human: {human_input}
Yokai:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"],
    template=template,
)

memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(
    llm=OpenAI(),
    prompt=prompt,
    verbose=True,
    memory=memory,
)

llm_chain.predict(human_input="OEM とは何か？")
