# -*- coding: utf-8 -*-
# By OL Consulting, SRL Bot para gestion de preguntas frecuentes en Telegram
# Desarrollado por: https://olconsulting.com.do 

from django.urls import path
from .views import telegram_webhook

urlpatterns = [
    path("webhook/", telegram_webhook, name="telegram_webhook"),
]

