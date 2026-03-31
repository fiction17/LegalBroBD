from app.rag.retrieval.retriever import Retriever
from app.rag.prompts.legal_prompt import build_prompt
from app.ai.llm_client import call_llm

retriever = Retriever()

def answer_question(query: str):
    contexts = retriever.retrieve(query)

    prompt = build_prompt(query, contexts)

    response = call_llm(prompt)

    return {
        "question": query,
        "answer": response,
        "sources": contexts
    }