from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import SpacyTextSplitter

loader = PyMuPDFLoader("./sample.pdf")
documents = loader.load()

text_splitter = SpacyTextSplitter(
    chunk_size=300,
    pipeline="ja_core_news_sm"
)
splitted_documents = text_splitter.split_documents(documents)

print(f"before: {len(documents)}")
print(f"after: {len(splitted_documents)}")
