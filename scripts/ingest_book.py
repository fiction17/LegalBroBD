from app.rag.ingest.pipeline import run_ingestion

if __name__ == "__main__":
    run_ingestion("data/raw/Constitutional_law.pdf")