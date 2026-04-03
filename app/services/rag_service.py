from app.rag.retrieval.retriever import retrieve
from app.rag.embedder import embed_query
from app.services.llm_service import generate_answer


def answer_question(question):
    query_embedding = embed_query(question)

    docs = retrieve(query_embedding)

    context = "\n\n---\n\n".join(docs[:3])

    answer = generate_answer(question, context)

    return answer, docs
