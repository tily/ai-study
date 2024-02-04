from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

database = Chroma(
    persist_directory="./.data",
    embedding_function=embeddings
)

documents = database.similarity_search("what's the max speed of flying car?")

print(f"num: {len(documents)}")

for document in documents:
    print(f"document content: {document.page_content}")
