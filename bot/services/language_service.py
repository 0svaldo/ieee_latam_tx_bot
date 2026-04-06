# -*- coding: utf-8 -*-
# By OL Consulting, SRL Bot para gestion de preguntas frecuentes en Telegram
# Desarrollado por: https://olconsulting.com.do 

from langdetect import detect

def detect_language(text: str) -> str:
    try:
        lang = detect(text)
        return "en" if lang.startswith("en") else "es"
    except Exception:
        return "es"