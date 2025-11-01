import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_ai(question, context):
    prompt = f"Given the following paper:\n{context[:4000]}\nAnswer concisely:\nQ: {question}\nA:"
    response = openai.Completion.create(
        engine="gpt-4o-mini",
        prompt=prompt,
        max_tokens=200,
        temperature=0.3
    )
    return response.choices[0].text.strip()
