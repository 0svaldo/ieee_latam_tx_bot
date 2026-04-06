# -*- coding: utf-8 -*-
# By OL Consulting, SRL Bot para gestion de preguntas frecuentes en Telegram
# Desarrollado por: https://olconsulting.com.do 

import requests
import logging
from config.settings import OLLAMA_URL_BASE, AI_MODEL

logger = logging.getLogger(__name__)

def ask_llm(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_URL_BASE,
            json={
                "model": AI_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 150,
                    "temperature": 0.2
                }

            },
            timeout=60
        )

        response.raise_for_status()
        data = response.json()

        return data.get("response", "").strip()

    except Exception as e:
        logger.error(f"Ollama error: {e}")
        return "⚠️ Error procesando la solicitud con el modelo."