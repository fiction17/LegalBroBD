import pickle
import numpy as np

from app.rag.embedder import embed_texts
from app.rag.vectorstore.faiss_store import load_faiss_index


class Retriever:
    def __init__(self):
        self.index = load_faiss_index()

        with open("app/rag/vectorstore/chunks.pkl", "rb") as f:
            self.chunks = pickle.load(f)

    def retrieve(self, query: str, top_k: int = 5):
        # 1. Embed query
        query_embedding = embed_texts([query])[0]

        query_embedding = np.array([query_embedding]).astype("float32")

        # 2. Search FAISS
        distances, indices = self.index.search(query_embedding, top_k)

        # 3. Get chunks
        results = []
        for idx in indices[0]:
            if idx < len(self.chunks):
                results.append(self.chunks[idx])

        return results