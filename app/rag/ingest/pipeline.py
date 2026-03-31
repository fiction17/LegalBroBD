import os
import pickle

from app.rag.ingest.loader import load_pdf
from app.rag.ingest.chunker import chunk_text
from app.rag.embedder import embed_texts
from app.rag.vectorstore.faiss_store import save_faiss_index


import re


def clean_text(text: str) -> str:
    # remove page numbers / dotted TOC lines
    text = re.sub(r"\.{3,}", " ", text)

    # fix hyphenated line breaks
    text = re.sub(r"-\s*\n\s*", "", text)

    # remove excessive newlines
    text = re.sub(r"\n+", "\n", text)

    return text.strip()


def run_ingestion(pdf_path: str):
    print("📥 Loading PDF...")

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"❌ File not found: {pdf_path}")

    # 1. Load
    raw_text = load_pdf(pdf_path)

    print(f"📄 Raw text length: {len(raw_text)}")

    # 2. Clean
    text = clean_text(raw_text)

    # 3. Chunk
    print("✂️ Chunking text...")
    chunks = chunk_text(
        text,
        chunk_size=500,      # 🔥 important
        overlap=100          # 🔥 improves context
    )

    print(f"📚 Total chunks: {len(chunks)}")

    # Debug sample
    print("\n🔍 Sample chunk:\n", chunks[0][:500])

    # 4. Embed
    print("🧠 Generating embeddings...")
    embeddings = embed_texts(chunks)

    # sanity check
    if len(embeddings) != len(chunks):
        raise ValueError("❌ Embedding count mismatch!")

    # 5. Save FAISS
    print("💾 Saving FAISS index...")
    save_faiss_index(embeddings)

    # 6. Save metadata (VERY IMPORTANT)
    os.makedirs("app/rag/vectorstore", exist_ok=True)

    metadata_path = "app/rag/vectorstore/chunks.pkl"

    with open(metadata_path, "wb") as f:
        pickle.dump(chunks, f)

    print(f"✅ Saved chunks → {metadata_path}")

    print("\n🎉 Ingestion complete!")