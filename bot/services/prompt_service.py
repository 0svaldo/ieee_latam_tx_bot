# -*- coding: utf-8 -*-
# By OL Consulting, SRL Bot para gestion de preguntas frecuentes en Telegram
# Desarrollado por: https://olconsulting.com.do 

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROMPTS_DIR = BASE_DIR / "prompts"

def load_prompt(filename: str) -> str:
    with open(PROMPTS_DIR / filename, "r", encoding="utf-8") as f:
        return f.read()

def build_prompt(question: str, context: str = "", user_lang: str = "es") -> str:
    return f"""
        You are the IEEE LATAM Transactions editorial assistant.

        Use the context as the primary source.

        If the answer is NOT explicitly in the context:
        provide a realistic and helpful answer based on standard academic publishing practices.

        Avoid saying "not specified" unless absolutely necessary.

        Be helpful, natural, and professional.

        Format:

        Español:
        <respuesta natural y útil>

        English:
        <natural and helpful answer>

        Context:
        {context}

        Question:
        {question}
    """