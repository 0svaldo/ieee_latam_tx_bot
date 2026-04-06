# -*- coding: utf-8 -*-
# By OL Consulting, SRL Bot para gestion de preguntas frecuentes en Telegram
# Desarrollado por: https://olconsulting.com.do 

import pickle
import faiss
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

INDEX_PATH = "bot/rag/vector_store/index.faiss"
CHUNKS_PATH = "bot/rag/vector_store/chunks.pkl"

_model = None
_index = None
_chunks = None


def load_resources():
    global _model, _index, _chunks

    if _model is None:
        print("🔄 Cargando modelo embeddings...")
        _model = SentenceTransformer(MODEL_NAME)

    if _index is None:
        _index = faiss.read_index(INDEX_PATH)

    if _chunks is None:
        with open(CHUNKS_PATH, "rb") as f:
            _chunks = pickle.load(f)


def search(query, k=3):
    load_resources()

    query_embedding = _model.encode([query])
    distances, indices = _index.search(query_embedding, k)

    results = [_chunks[i] for i in indices[0]]
    return results