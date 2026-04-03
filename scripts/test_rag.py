from app.services.rag_service import answer_question

if __name__ == "__main__":
    question = "What is the basic structure of the Constitution of Bangladesh?"

    answer, sources = answer_question(question)

    print("\n🧠 QUESTION:\n", question)
    print("\n📖 ANSWER:\n", answer)

    print("\n📚 SOURCES:\n")
    for i in sources:
        print(f"{i}\n")