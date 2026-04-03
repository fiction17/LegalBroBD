import re


def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"-\s+", "", text)
    return text.strip()


def split_sentences(text):
    return re.split(r'(?<=[.!?]) +', text)


def chunk_text(text, chunk_size=800, overlap=150):
    text = clean_text(text)

    sentences = split_sentences(text)

    chunks = []
    current = ""

    for sent in sentences:
        if len(current) + len(sent) <= chunk_size:
            current += " " + sent
        else:
            chunks.append(current.strip())

            # overlap
            current = current[-overlap:] + " " + sent

    if current:
        chunks.append(current.strip())

    return chunks