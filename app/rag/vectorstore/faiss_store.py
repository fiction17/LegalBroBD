import faiss
import numpy as np
import os

INDEX_PATH = "app/rag/vectorstore/index.faiss"

def save_faiss_index(embeddings):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)

    embeddings_np = np.array(embeddings).astype("float32")
    index.add(embeddings_np)

    os.makedirs("app/rag/vectorstore", exist_ok=True)
    faiss.write_index(index, INDEX_PATH)

    print(f"✅ FAISS index saved at {INDEX_PATH}")

def load_faiss_index():
    if not os.path.exists(INDEX_PATH):
        raise FileNotFoundError("FAISS index not found")

    return faiss.read_index(INDEX_PATH)