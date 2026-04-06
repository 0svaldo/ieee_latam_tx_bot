# -*- coding: utf-8 -*-
# By OL Consulting, SRL Bot para gestion de preguntas frecuentes en Telegram
# Desarrollado por: https://olconsulting.com.do 


from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
TOKEN_BOT_IEEE_TELEGRAM = os.getenv("TOKEN_BOT_IEEE_TELEGRAM")
DOCKER_ACTIVE = os.getenv("DOCKER_ACTIVE", "False") == "True"
if DOCKER_ACTIVE:
    OLLAMA_URL_BASE = os.getenv("OLLAMA_DOCKER_URL", "http://ollama:11434/api/generate")
else:
    OLLAMA_URL_BASE = os.getenv("OLLAMA_LOCALHOST_URL", "http://localhost:11434/api/generate")

ACTIVE_AI_MODEL = os.getenv("ACTIVE_AI_MODEL", "llama3").lower()
AI_MODEL = os.getenv("LLAMA3_AI_MODEL", "llama3")
if ACTIVE_AI_MODEL == "llama3":
    AI_MODEL = os.getenv("LLAMA3_AI_MODEL", "llama3")
elif ACTIVE_AI_MODEL == "phi3":
    AI_MODEL = os.getenv("PHI3_AI_MODEL", "phi3")
elif ACTIVE_AI_MODEL == "mistral":
    AI_MODEL = os.getenv("MISTRAL_AI_MODEL", "mistral")
else:
    AI_MODEL = os.getenv("LLAMA3_AI_MODEL", "llama3")  # Default to llama3 if not specified

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'bot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'
