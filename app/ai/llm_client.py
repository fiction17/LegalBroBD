from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)


def call_llm(prompt=None, messages=None, model="nvidia/nemotron-3-super-120b-a12b:free"):
    try:
        if messages is None and prompt is not None:
            messages = [
                {"role": "user", "content": str(prompt)}
            ]

        if messages is None:
            raise ValueError("Either 'prompt' or 'messages' must be provided")

        # 🔥 Ensure all contents are strings
        for m in messages:
            m["content"] = str(m["content"])

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.3,
        )

        return response.choices[0].message.content or "⚠️ Empty response"

    except Exception as e:
        return f"error occured: {str(e)}"