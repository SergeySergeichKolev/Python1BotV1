import os
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key="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",
)

completion = client.chat.completions.create(
    model="moonshotai/Kimi-K2-Thinking:novita",
    messages=[
        {
            "role": "user",
            "content": "What is the mass of cat?"
        }
    ],
)

print(completion.choices[0].message)