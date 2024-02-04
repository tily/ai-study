from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.retrievers import WikipediaRetriever

chat = ChatOpenAI()

retriever = WikipediaRetriever(
    lang="ja",
    doc_content_chars_max=500,
    top_k_results=2,
)

chain = RetrievalQA.from_llm(
    llm=chat,
    retriever=retriever,
    return_source_documents=True,
)

result = chain("ウーチャカとは？")

source_documents = result["source_documents"]

print(f"検索結果: {len(source_documents)}件")

for document in source_documents:
    print(document.metadata)
    print(document.page_content[:100])
    print("--------")
print("========")
print(result["result"])
