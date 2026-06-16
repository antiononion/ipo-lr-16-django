# ─────────────────────────────────────────────────────────────────────────────
# ДОБАВЬ ЭТИ НАСТРОЙКИ В КОНЕЦ СВОЕГО settings.py
# ─────────────────────────────────────────────────────────────────────────────

# ── CUSTOM USER MODEL ──────────────────────────────────────────────────────
AUTH_USER_MODEL = 'shoppy.CustomUser'  # имя твоего приложения

# ── LOGIN/LOGOUT REDIRECT ──────────────────────────────────────────────────
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# ── MEDIA FILES (для загрузки фото товаров) ───────────────────────────────
import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ── EMAIL — Gmail SMTP ────────────────────────────────────────────────────
# ВНИМАНИЕ: не храни пароли в коде!
# Используй переменные окружения или python-decouple.
# Для Gmail нужен "Пароль приложения" (не обычный пароль):
# myaccount.google.com → Безопасность → Двухфакторная → Пароли приложений

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'твой_email@gmail.com'       # ← ЗАМЕНИ
EMAIL_HOST_PASSWORD = 'твой_пароль_приложения'  # ← ЗАМЕНИ (пароль приложения Gmail)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ── MESSAGES FRAMEWORK (для flash-сообщений) ─────────────────────────────
from django.contrib.messages import constants as messages_const
MESSAGE_TAGS = {
    messages_const.DEBUG:   'info',
    messages_const.INFO:    'info',
    messages_const.SUCCESS: 'success',
    messages_const.WARNING: 'warning',
    messages_const.ERROR:   'error',
}

# ── INSTALLED_APPS — убедись, что есть все нужные ────────────────────────
# INSTALLED_APPS = [
#     ...
#     'shoppy',          # твоё приложение
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
# ]

# ── TEMPLATES — убедись, что DIRS включает папку templates ───────────────
# TEMPLATES = [{
#     ...
#     'DIRS': [BASE_DIR / 'templates'],
#     ...
# }]

# ── ДЛЯ РАЗРАБОТКИ: показывать email в консоли вместо реальной отправки ──
# Раскомментируй строку ниже для тестирования без реального SMTP:
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
