import json
import openai

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "user",
      "content": "妹になった父への手紙、未練がましく",
    }
  ],
  max_tokens=100,
  temperature=1,
  n=2,
)

print(json.dumps(response, indent=2, ensure_ascii=False))
