import faiss
import numpy as np
import os

INDEX_PATH = "data/vectorstore/index.faiss"


def save_faiss_index(embeddings):
    if not len(embeddings):
        raise ValueError("Embeddings are empty ❌")

    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)

    embeddings_np = np.array(embeddings).astype("float32")
    index.add(embeddings_np)

    os.makedirs("data/vectorstore", exist_ok=True)
    faiss.write_index(index, INDEX_PATH)

    print(f"✅ FAISS saved at {INDEX_PATH}")


def load_faiss_index():
    if not os.path.exists(INDEX_PATH):
        raise FileNotFoundError("FAISS index not found")

    return faiss.read_index(INDEX_PATH)