from langchain.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(lang="ja")
docments = retriever.get_relevant_documents("大規模言語モデル")
print(f"検索結果: {len(documents)}件")
for document in documents:
    print("## 取得したメタデータ")
    print(docment.metadata)
    print("## 取得したテキスト")
    print(document.page_content[:100])
