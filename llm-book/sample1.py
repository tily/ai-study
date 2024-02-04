from transformers import pipeline

text_classification_pipeline = pipeline(
    model="llm-book/bert-base-japanese-v3-marc_ja"
)

#positive_text = "世界には言葉がわからなくても感動する音楽がある。"
#print(text_classification_pipeline(positive_text)[0])
#
#negative_text = "世界には言葉にできないほどひどい音楽がある。"
#print(text_classification_pipeline(negative_text)[0])

negative_text = "あなたのことは好きだけど、好きじゃない、なぜなら好きです！ (嘘)"
print(text_classification_pipeline(negative_text)[0])
