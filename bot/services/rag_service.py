# -*- coding: utf-8 -*-
# By OL Consulting, SRL Bot para gestion de preguntas frecuentes en Telegram
# Desarrollado por: https://olconsulting.com.do 

from bot.rag.search import search

def get_context(question: str) -> str:
    results = search(question, k=2)  #k=3, por ejemplo, para obtener los 3 resultados más relevantes

    return "\n\n".join(results)