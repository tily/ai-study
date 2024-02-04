from langchain.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader("./sample.pdf")
documents = loader.load()

print(f"num of document: {len(documents)}")

print(f"1st document content: {documents[1].page_content}")
print(f"1st document metadata: {documents[1].metadata}")
