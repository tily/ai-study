from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("abeja/gpt2-large-japanese")
model = AutoModelForCausalLM.from_pretrained(
    "abeja/gpt2-large-japanese"
)
inputs = tokenizer("今日は天気が良いので", return_tensors="pt")

outputs = model.generate(
    **inputs,
    max_length=15,
    pad_token_id=tokenizer.pad_token_id
)

generated_text = tokenizer.decode(
    outputs[0], skip_special_tokens=True
)

print(generated_text) 
