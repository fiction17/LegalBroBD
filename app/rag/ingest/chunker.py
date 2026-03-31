import nltk
nltk.download("punkt")

from nltk.tokenize import sent_tokenize

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")
    nltk.download("punkt_tab")


def chunk_text(text, chunk_size=500, overlap=100):
    sentences = sent_tokenize(text)

    chunks = []
    current = []
    current_len = 0

    for sentence in sentences:
        words = sentence.split()
        if current_len + len(words) > chunk_size:
            chunks.append(" ".join(current))

            # overlap
            overlap_words = " ".join(current).split()[-overlap:]
            current = overlap_words
            current_len = len(overlap_words)

        current.append(sentence)
        current_len += len(words)

    if current:
        chunks.append(" ".join(current))

    return chunks


def filter_chunks(chunks):
    clean_chunks = []
    for c in chunks:
        # remove short / junk chunks
        if len(c.split()) < 30:
            continue

        # remove TOC-like chunks
        if "chapter" in c.lower() and "...." in c:
            continue

        clean_chunks.append(c)

    return clean_chunks