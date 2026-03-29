from app.ai.llm_client import call_llm

SYSTEM_PROMPT = """
You are a legal assistant, specialized in Bangladeshi law and constitution.

Simplify legal text in plain English

Rules:
- Keep it accurate
- Avoid legal jargon
- Use short sentences
- If complex → break into bullet points
- Do NOT add information not present

Output format:
- Simple explanation
- Bullet points if needed
"""
def simplify_text(text: str):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": text}
    ]

    model = "stepfun/step-3.5-flash:free"

    simplified = call_llm(messages, model)

    return {
        "success": True,
        "data": {
            "original": text,
            "simplified": simplified
        }
    }