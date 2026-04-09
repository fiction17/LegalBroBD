from app.ai.llm_client import call_llm

SYSTEM_PROMPT = """
You are a legal expert on Bangladesh Constitution.

If answer is not clearly in context, extract the closest explanation and summarize it.
DO NOT say "Not found" until the context is too irrelevant.

Rules:
- Do NOT hallucinate
- If answer not found → "Build answer from context and add caution in the end"
- Keep answer precise
- Cite concepts clearly
"""


def generate_answer(question, context):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"""
                        Context:
                        {context}
                        
                        Question:
                        {question}
                        """
        }
    ]

    return call_llm(messages=messages,model="openrouter/free")