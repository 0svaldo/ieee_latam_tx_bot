# -*- coding: utf-8 -*-
# By OL Consulting, SRL Bot para gestion de preguntas frecuentes en Telegram
# Desarrollado por: https://olconsulting.com.do 

import os
import requests
from config.settings import TOKEN_BOT_IEEE_TELEGRAM 

def send_telegram_message(chat_id: int, text: str) -> dict:
    url = f"https://api.telegram.org/bot{TOKEN_BOT_IEEE_TELEGRAM}/sendMessage"
    response = requests.post(url, json={
        "chat_id": chat_id,
        "text": text
    }, timeout=30)
    return response.json()