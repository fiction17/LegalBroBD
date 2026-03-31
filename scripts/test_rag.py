from app.services.rag_service import answer_question

if __name__ == "__main__":
    query = "What is the basic structure of the Constitution of Bangladesh?"

    result = answer_question(query)

    print("\n🧠 QUESTION:\n", result["question"])
    print("\n📖 ANSWER:\n", result["answer"])
    print("\n📚 SOURCES:\n")

    for i, src in enumerate(result["sources"], 1):
        print(f"{i}. {src[:200]}...\n")