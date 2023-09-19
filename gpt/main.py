import openai


openai.api_key = "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"
MODEL = "gpt-3.5-turbo"

response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "hola que tal, como estas?"
        }
    ], 
    max_tokens=200
)

print(response['choices'][0]['message']['content'])