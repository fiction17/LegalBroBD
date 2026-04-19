import numpy as np
import pickle
import faiss
import re

INDEX_PATH = "data/vectorstore/index.faiss"
METADATA_PATH = "data/vectorstore/metadata.pkl"


def retrieve(query_text, query_embedding, top_k=5):
    # 1. Load data
    index = faiss.read_index(INDEX_PATH)
    with open(METADATA_PATH, "rb") as f:
        metadata = pickle.load(f)

    # 2. Keyword Extraction
    # Look for "Article X" patterns or important legal keywords
    art_match = re.search(r'article\s*(\d+)', query_text.lower())
    target_art = art_match.group(1) if art_match else None

    # Simple keyword list (filtering short words)
    keywords = [kw.lower() for kw in query_text.split() if len(kw) > 3]

    constitution_docs = []
    book_docs = []
    seen_indices = set()

    # 3. Step One: Direct Keyword/Article Match (High Precision)
    for i, meta in enumerate(metadata):
        content = (meta.get("content") or meta.get("text", "")).lower()
        title = meta.get("title", "").lower()
        art_no = str(meta.get("article_no", "")).lower()

        is_const = meta.get('category') == 'constitution' or 'article_no' in meta

        # Match logic: Exact article number OR important keywords in the content
        if (target_art and target_art == art_no) or any(kw in content for kw in keywords if is_const):
            formatted = f"SOURCE: {meta.get('article_no', 'Constitution')}\n{meta.get('content') or meta.get('text', '')}"
            constitution_docs.append(formatted)
            seen_indices.add(i)

    # 4. Step Two: Vector Search (Semantic fallback)
    query_vec = np.array([query_embedding]).astype("float32")
    _, indices = index.search(query_vec, top_k * 3)

    for idx in indices[0]:
        if idx == -1 or idx >= len(metadata) or idx in seen_indices:
            continue

        meta = metadata[idx]
        is_const = meta.get('category') == 'constitution' or 'article_no' in meta

        content = meta.get("content") or meta.get("text", "")
        formatted = f"SOURCE: {meta.get('article_no', 'Reference')}\n{content}"

        if is_const:
            constitution_docs.append(formatted)
        else:
            book_docs.append(formatted)
        seen_indices.add(idx)

    # 5. Final Ranking: Constitution always wins, then cut to top_k
    return (constitution_docs + book_docs)[:top_k]