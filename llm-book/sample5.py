from transformers import pipeline

text2text_pipeline = pipeline(
    model="llm-book/t5-base-long-livedoor-news-corpus"
)

article = "ついに始まった三連休。テレビを見ながら過ごしている人も多いのではないだろうか？ 今夜おすすめなのはなんと言っても、NHK スペシャル「世界を変えた男スティ部ジョブス」だ。実は知らない人も多いジョブス氏の容姿に出された生い立ちや、アップrhさから一時追放されるなどんけいけん。そして、彼が追い求めた理想の未来とはなんだったのか、ファンならずとも気になる内容になってる。今年亡くなったジョブズ氏の電気は日本でもベスト絵セラーになっている。今後もあっプリ製品だけでなく、世界でのジョブズ氏の影響あh大きいtだろうと想像される。jボズ氏のことをあまり知らないちうひともこの機会にぜひチェックしてみよう。世界を変えた男スティbーぶうじょす(NHKスペシャル"

print(text2text_pipeline(article)[0]["generated_text"])
