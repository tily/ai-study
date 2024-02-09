from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma

long_text = """
GPT-4は、OpenAIが開発したAI技術であるGPTシリーズの第4世代目のモデルです。

自然言語処理(NLP)という技術を使い、文章の生成や理解を行うことができます。

これにより、人間と同じような文章を作成することが可能です。

GPT-4は、トランスフォーマーアーキテクチャに基づいており、より強力な性能を発揮します。

GPT-4は、インターネット上の大量のテキストデータを学習し、豊富な知識を持っています。

しかし、2021年9月までの情報しか持っていません。

このモデルは、質問応答や文章生成、文章要約など、様々なタスクで使用できます。

ただし、GPT-4は完璧ではありません。

時々、誤った情報や不適切な内容を生成することがあります。

使用者は、その限界を理解し、

適切な方法で利用することが重要です。
"""

text_splitter = CharacterTextSplitter(
    separator = "\n\n",
    chunk_size = 100,
    chunk_overlap = 0,
    length_function = len,
)

texts = text_splitter.split_text(long_text)

docsearch = Chroma.from_texts(texts, OpenAIEmbeddings())

query = "Q1. インターネット上の何のデータを使って、学習しているの？"
print(f"\n\n{query}")
docs = docsearch.similarity_search(query)
print(docs[0].page_content)

query = "Q2. GPT4 は第何世代のモデル？"
print(f"\n\n{query}")
docs = docsearch.similarity_search(query)
print(docs[0].page_content)
