# -*- coding: utf-8 -*-
# By OL Consulting, SRL Bot para gestion de preguntas frecuentes en Telegram
# Desarrollado por: https://olconsulting.com.do 

import os
import pickle
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss

MODEL_NAME = "all-MiniLM-L6-v2"
INDEX_PATH = "bot/rag/vector_store/index.faiss"
CHUNKS_PATH = "bot/rag/vector_store/chunks.pkl"


def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


def main():
    print("Cargando PDF...")
    text = load_pdf("bot/rag/manual.pdf")

    print("Dividiendo en chunks...")
    chunks = chunk_text(text)

    print(f"{len(chunks)} chunks generados")

    print("Generando embeddings...")
    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(chunks)

    print("Creando índice FAISS...")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    os.makedirs("bot/rag/vector_store", exist_ok=True)

    faiss.write_index(index, INDEX_PATH)

    with open(CHUNKS_PATH, "wb") as f:
        pickle.dump(chunks, f)

    print("RAG listo 🚀")


if __name__ == "__main__":
    main()