import os
import chainlit as cl
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyMuPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from langchain.text_splitter import SpacyTextSplitter
from langchain.vectorstores import Chroma

embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

prompt = PromptTemplate(
    template="""Please answer the question based on the sentences.

Sentences:
{document}

Question: {query}
""",
    input_variables=["document", "query"]
)

text_splitter = SpacyTextSplitter(chunk_size=300, pipeline="ja_core_news_sm")

@cl.on_chat_start
async def on_chat_start():
    files = None

    while files is None:
        files = await cl.AskFileMessage(
            max_size_mb=20,
            content="select PDF",
            accept=["application/pdf"],
            raise_on_timeout=False,
        ).send()
    file = files[0]
    #file_content = ""
    #if not os.path.exists("tmp"):
    #    os.mkdir("tmp")
    #with open(file.path, "r") as f:
    #    file_content = f.read()
    #with open(f"tmp/{file.name}", "wb") as f:
    #    f.write(file_content)
    #documents = PyMuPDFLoader(f"tmp/{file.name}").load()
    documents = PyMuPDFLoader(file.path).load()
    splitted_documents = text_splitter.split_documents(documents)
    database = Chroma(
        embedding_function=embeddings
    )
    database.add_documents(splitted_documents) 

    cl.user_session.set("database", database)

    await cl.Message(content="Ready! Input messages").send()

@cl.on_message
async def on_message(input_message):
    print(input_message)
    database = cl.user_session.get("database")
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
