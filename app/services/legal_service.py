from app.services.rag_service import answer_question
from app.ai.llm_client import call_llm


SYSTEM_PROMPT = """
You are a legal assistant specialized in Bangladeshi law and constitution.

Answer the question using ONLY the provided context.

Rules:
- Keep it accurate
- Use plain English (no legal jargon)
- Use short sentences
- If complex → break into bullet points
- Do NOT add outside knowledge
- If answer not in context → say "Not found in the provided context"

Output format:
- Clear explanation
- Bullet points if needed
"""


def ask_legal(question: str):
    # 🔹 Step 1: Get RAG context
    answer, sources = answer_question(question)

    # 🔹 Step 2: Improve answer using system prompt
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"""
                        Question:
                        {question}
                        
                        Context-based answer:
                        {answer}
                        """
        }
    ]

    model = "openrouter/free"

    final_answer = call_llm(messages=messages, model=model)

    return {
        "success": True,
        "data": {
            "answer": final_answer,
            "sources": sources
        }
    }