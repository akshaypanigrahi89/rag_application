# ingestion.py

from utils.chunking import chunk_text
from utils.embedding import get_embedding

with open("data/docs.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = chunk_text(text)

# create embeddings
# save FAISS index