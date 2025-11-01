import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_ai(question, context):
    messages = [
        {"role": "system", "content": "You are a helpful assistant summarizing papers."},
        {"role": "user", "content": f"Given the following paper:\n{context[:4000]}\nAnswer concisely:\nQ: {question}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.3,
        max_tokens=200,
    )
    return response.choices[0].message.content.strip()
