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

    distances, indices = index.search(query, top_k * 2)  # get more

    docs = []

    for i, dist in zip(indices[0], distances[0]):
        if i < len(metadata) and dist < 2:  # 🔥 FILTER
            docs.append(metadata[i]["text"])

    return docs[:top_k]
