from fastembed import TextEmbedding

# This will download the model (if not already present) and load it
# 'all-MiniLM-L6-v2' is a supported default in FastEmbed
model = TextEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")


def embed_texts(texts):
    # .embed() returns a generator for memory efficiency
    # We convert to a list to match your original function's behavior
    return list(model.embed(texts))


def embed_query(query):
    # .query_embed() is optimized for single strings
    return list(model.query_embed(query))[0]
