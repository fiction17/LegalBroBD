from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)


def call_llm(prompt=None, messages=None, model="stepfun/step-3.5-flash:free") -> str:
    try:
        if messages is None and prompt is not None:
            messages = [
                {"role": "user", "content": prompt}
            ]

        if messages is None:
            raise ValueError("Either 'prompt' or 'messages' must be provided")

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.3,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"error occured: {str(e)}"