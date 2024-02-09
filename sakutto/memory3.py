from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(return_messages=True)

memory.save_context(
    {"input": "AI とは何か？"},
    {"output": "AI とは人工知能です。"},
)

print(memory.load_memory_variables({}))
