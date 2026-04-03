import json
import pickle
import os

from app.rag.ingest.loader import load_pdf
from app.rag.ingest.chunker import chunk_text
from app.rag.embedder import embed_texts
from app.rag.vectorstore.faiss_store import save_faiss_index

CHUNKS_PATH = "data/processed/chunks.json"
METADATA_PATH = "data/vectorstore/metadata.pkl"


def remove_noise(text):
    blacklist = [
        "bibliography",
        "references",
        "acknowledgement",
        "contents",
        "table of contents",
        "index"
    ]

    lines = text.split("\n")

    filtered = [
        line for line in lines
        if not any(b.lower() in line.lower() for b in blacklist)
    ]

    return "\n".join(filtered)


def run_ingestion(pdf_path):
    print("📥 Loading PDF...")
    text = load_pdf(pdf_path)

    print(f"📄 Removing noise..")
    text = remove_noise(text)

    print(f"📄 Raw text length: {len(text)}")

    print("✂️ Chunking text...")
    chunks = chunk_text(text)

    print(f"🔹 Total chunks: {len(chunks)}")

    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("data/vectorstore", exist_ok=True)

    print("💾 Saving chunks + metadata...")

    # ✅ Save chunks
    with open(CHUNKS_PATH, "w") as f:
        json.dump(chunks, f)

    # ✅ Save metadata (ONLY ONCE)
    metadata = [
        {
            "text": chunk,
            "id": i,
            "length": len(chunk)
        }
        for i, chunk in enumerate(chunks)
    ]

    with open(METADATA_PATH, "wb") as f:
        pickle.dump(metadata, f)

    print("🧠 Generating embeddings...")
    embeddings = embed_texts(chunks)

    print("💾 Saving FAISS index...")
    save_faiss_index(embeddings)

    print("✅ Ingestion complete!")