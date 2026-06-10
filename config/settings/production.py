from decouple import UndefinedValueError, config
from django.core.exceptions import ImproperlyConfigured

from .base import *

DEBUG = False

try:
    SECRET_KEY = config("SECRET_KEY")
except UndefinedValueError as exc:
    raise ImproperlyConfigured(
        "SECRET_KEY precisa estar definida em producao."
    ) from exc

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
