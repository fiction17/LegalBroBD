from sentence_transformers import SentenceTransformer

# Load once (IMPORTANT: global for performance)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def embed_texts(texts: list[str]) -> list[list[float]]:
    """
    Convert list of texts → embeddings
    """
    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        convert_to_numpy=True
    )

    return embeddings