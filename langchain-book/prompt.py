from langchain import PromptTemplate
prompt = PromptTemplate(
    template="{product}はどこの会社が開発した製品ですか？",
    input_variables=["product"]
)

print(prompt.format(product="iPhone"))
print(prompt.format(product="Xperia"))
