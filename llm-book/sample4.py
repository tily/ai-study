from transformers import pipeline
from pprint import pprint

ner_pipeline = pipeline(
    model="llm-book/bert-base-japanese-v3-ner-wikipedia-dataset",
    aggregation_strategy="simple",
)
text = "大谷翔平は岩手県水沢市出身のプロ野球選手"
pprint(ner_pipeline(text))
