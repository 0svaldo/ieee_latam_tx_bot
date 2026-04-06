# -*- coding: utf-8 -*-
# By OL Consulting, SRL Bot para gestion de preguntas frecuentes en Telegram
# Desarrollado por: https://olconsulting.com.do 

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .services.telegram_service import send_telegram_message
from .services.language_service import detect_language
from .services.prompt_service import build_prompt
from .services.llm_service import ask_llm
from .services.rag_service import get_context
from .rag.web_source import get_web_content

import logging
logger = logging.getLogger(__name__)


@csrf_exempt
def telegram_webhook(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        return JsonResponse({"detail": "Invalid JSON"}, status=400)

    message = data.get("message", {})
    chat = message.get("chat", {})
    text = message.get("text", "").strip()
    chat_id = chat.get("id")

    if not chat_id:
        return JsonResponse({"ok": True})

    if not text:
        send_telegram_message(chat_id, "Solo puedo procesar mensajes de text por ahora.")
        return JsonResponse({"ok": True})

    print(f"Mensaje recibido: {text}")
    user_lang = detect_language(text)

    manual_context = get_context(text)
    web_context = get_web_content()
    context = manual_context + "\n\n" + web_context

    prompt = build_prompt(question=text, context=context, user_lang=user_lang)
    response_text = ask_llm(prompt)

    send_telegram_message(chat_id, response_text)
    return JsonResponse({"ok": True})
