# -*- coding: utf-8 -*-
# By OL Consulting, SRL Bot para gestion de preguntas frecuentes en Telegram
# Desarrollado por: https://olconsulting.com.do 

import requests
from bs4 import BeautifulSoup

def get_web_content():
    url = "https://latamt.ieeer9.org/index.php/transactions/index"
    r = requests.get(url, timeout=10)

    soup = BeautifulSoup(r.text, "html.parser")

    text = soup.get_text(separator="\n")
    return text #[:3000]  # limitar