import numpy as np
import pickle
import faiss

INDEX_PATH = "data/vectorstore/index.faiss"
METADATA_PATH = "data/vectorstore/metadata.pkl"


def retrieve(query_embedding, top_k=5):
    index = faiss.read_index(INDEX_PATH)
    with open(METADATA_PATH, "rb") as f:
        metadata = pickle.load(f)

    query = np.array([query_embedding]).astype("float32")

    # Get a larger pool (top_k * 4) to make sure we don't miss the
    # actual law hidden under textbook noise
    _, indices = index.search(query, top_k * 4)

    constitution_docs = []
    book_docs = []

    for idx in indices[0]:
        if idx == -1 or idx >= len(metadata):
            continue

        meta = metadata[idx]

        # Use the specific keys from your scraping script
        content = meta.get("content") or meta.get("text", "")
        source_info = f"SOURCE: {meta.get('article_no', 'Book Reference')}"
        formatted_doc = f"{source_info}\n{content}"

        # Hierarchy Logic: Separate constitution from books
        if meta.get('category') == 'constitution' or 'article_no' in meta:
            constitution_docs.append(formatted_doc)
        else:
            book_docs.append(formatted_doc)

    # Re-order: Constitution first, Books second, sliced to your top_k
    return (constitution_docs + book_docs)[:top_k]