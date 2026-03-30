# ⚖️ LegalBro API (Backend)

LegalBro is an AI-powered legal assistant focused on **Bangladeshi law and constitution**.
It helps users understand legal queries in simple terms and will soon support **legal document generation** (e.g., partnership deeds, contracts).

---

## 🚀 Features

*  AI-powered legal Q&A
*  Focused on **Bangladeshi law & constitution**
*  FastAPI backend with clean architecture
*  Pluggable LLM support (OpenAI / OpenRouter / DeepSeek)
*  REST API for frontend integration

---

## 📁 Project Structure

```
app/
├── api/                # API routes
│   └── v1/endpoints/
├── services/           # Business logic
├── ai/                 # LLM integration
├── templates/          # (optional UI templates)
└── main.py             # FastAPI entry point
```

---

## ⚙️ Setup

### 1. Clone repo

```
git clone https://github.com/your-username/LegalBroBD.git
cd LegalBro
```

### 2. Create virtual environment

```
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Environment variables

Create `.env`:

```
OPENAI_API_KEY=your_api_key
```

---

## ▶️ Run locally

```
uvicorn app.main:app --reload
```

Visit:

```
http://localhost:8000
```

---

## 🔗 API Endpoint

### POST `/api/v1/legal/simplify`

**Request:**

```json
{
  "text": "What are tenant rights in Bangladesh?"
}
```

**Response:**

```json
{
  "data": {
    "simplified": "..."
  }
}
```

---

## 🌍 Deployment

* Backend: Render
* Frontend: Vercel

---

## 🛣️ Roadmap

* 📄 RAG with legal documents (PDF ingestion)
* 🧾 Contract generation (e.g., partnership deed)
* 🧠 Multi-model support (DeepSeek, GPT, etc.)
* 🔐 Authentication & usage tracking

---

## ⚠️ Disclaimer

This project provides **informational assistance only** and does not constitute legal advice.

---

## 👨‍💻 Author

Built by Reyad
