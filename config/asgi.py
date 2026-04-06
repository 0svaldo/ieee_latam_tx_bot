# -*- coding: utf-8 -*-
# By OL Consulting, SRL Bot para gestion de preguntas frecuentes en Telegram
# Desarrollado por: https://olconsulting.com.do 


import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
