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

query = "what's the max speed of flying car?"

documents = database.similarity_search(query)

documents_string = ""

for document in documents:
    documents_string += f"""
---------------------------
{document.page_content}
"""

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

result = chat([
    HumanMessage(content=prompt.format(document=documents_string, query=query))
])

print(result.content)
