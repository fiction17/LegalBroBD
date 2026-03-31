# app/rag/ingest/loader.py

from PyPDF2 import PdfReader
import re


def clean_text(text: str) -> str:
    # remove page numbers / dotted TOC lines
    text = re.sub(r"\.{3,}", " ", text)

    # fix hyphenated line breaks
    text = re.sub(r"-\s*\n\s*", "", text)

    # remove excessive newlines
    text = re.sub(r"\n+", "\n", text)

    return text.strip()


def load_pdf(path: str) -> str:
    reader = PdfReader(path)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    return clean_text(text)