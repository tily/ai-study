import chainlit as cl
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from langchain.vectorstores import Chroma

embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

database = Chroma(
    persist_directory="./.data",
    embedding_function=embeddings
)

prompt = PromptTemplate(
    template="""Please answer the question based on the sentences.

Sentences:
{document}

Question: {query}
""",
    input_variables=["document", "query"]
)

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Ready! Input messages").send()

@cl.on_message
async def on_message(input_message):
    print(input_message)
    documents = database.similarity_search(input_message.content)
    
    documents_string = ""
    
    for document in documents:
        documents_string += f"""
    ---------------------------
    {document.page_content}
    """

    result = chat([
        HumanMessage(content=prompt.format(document=documents_string, query=input_message.content))
    ])
    await cl.Message(content=result.content).send()

