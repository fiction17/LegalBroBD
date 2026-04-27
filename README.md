# ⚖️ LegalBro - AI Agent

LegalBro is an AI-powered legal assistant focused on **Bangladeshi law and constitution**.  
It uses a **Retrieval-Augmented Generation (RAG)** system to provide accurate, context-aware answers from legal documents, simplified into plain English.

---

## 🚀 Features

*  🔍 AI-powered legal Q&A (RAG-based)
*  📚 Hybrid retrieval (**Semantic + Keyword search**)
*  🇧🇩 Focused on **Bangladeshi law & constitution**
*  🧠 Context-aware answers from legal PDFs
*  ⚡ FastAPI backend with clean architecture
*  🔌 Pluggable LLM support (OpenAI / OpenRouter / DeepSeek)
*  📦 Preprocessed vector store (optimized for deployment)

---

## 🧠 How It Works

1. 📄 Legal PDFs are ingested and cleaned  
2. ✂️ Text is chunked using structure-aware + contextual chunking  
3. 🔗 Embeddings are generated using sentence-transformers  
4. 🗂️ Stored in FAISS vector database  
5. 🔎 Hybrid retrieval:
   * Semantic search (FAISS)
   * Keyword filtering (precision boost)
6. 🤖 LLM generates answers grounded in retrieved context  

---

## 📁 Project Structure

---

app/
├── rag/
│ ├── ingest/ # PDF loading, cleaning, chunking
│ ├── retrieval/ # Hybrid retrieval logic
│ ├── vectorstore/ # FAISS + metadata
│ └── embedder.py
├── services/ # RAG + LLM orchestration
├── ai/ # LLM integration
├── api/ # API routes
└── main.py # FastAPI entry point

data/
├── processed/ # chunks.json
└── vectorstore/ # index.faiss, metadata.pkl


---

## ⚙️ Setup

### 1. Clone repo


git clone https://github.com/fiction17/LegalBroBD.git

cd LegalBro


### 2. Create virtual environment


python -m venv .venv
source .venv/bin/activate


### 3. Install dependencies


pip install -r requirements.txt


### 4. Environment variables

Create `.env`:


OPENAI_API_KEY=your_api_key


---

## ▶️ Run locally


uvicorn app.main:app --reload


Visit:


http://localhost:8000


---

## 🔗 API Endpoint

### GET `/ask`

**Example:**


/ask?question=What is the basic structure of the Constitution of Bangladesh?


**Response:**

```json
{
  "answer": "...",
  "sources": ["...", "..."]
}
```
### 🧠 RAG Pipeline
PDF → Clean → Chunk → Embed → FAISS  
Query → Embed → Retrieve → LLM → Answer
## 🌍 Deployment
- Backend: Render
- Frontend: (Planned) Vercel

## 🛣️ Roadmap
- 🔥 Reranker (Cross-Encoder for better retrieval)
- 📄 Advanced legal chunking (section-aware)
- 🧾 Contract generation (e.g., partnership deed)
- 🧠 Multi-model support (DeepSeek, GPT, etc.)
- 🔐 Authentication & usage tracking
- ⚠️ Disclaimer

This project provides informational assistance only and does not constitute legal advice.

👨‍💻 Author

Built by Reyad
