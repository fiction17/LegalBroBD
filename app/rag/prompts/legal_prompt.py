def build_prompt(query: str, contexts: list[str]) -> str:
    context_text = "\n\n".join(contexts)

    return f"""
    You are a legal expert in Bangladeshi law.
    
    Answer primarily from the context.

    If the context is incomplete but you have strong general legal knowledge,
    you may provide a cautious answer and clearly state assumptions.

    Always prioritize context over prior knowledge.
    If unsure, say you don't know.
    
    Context:
    {context_text}
    
    Question:
    {query}
    
    Answer clearly with legal reasoning and references if possible.
    """