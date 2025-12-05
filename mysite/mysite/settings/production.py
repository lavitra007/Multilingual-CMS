from .base import *
import os
import dj_database_url

DEBUG = False

# Security settings
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-key-placeholder")

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")
if not ALLOWED_HOSTS or ALLOWED_HOSTS == ['']:
    ALLOWED_HOSTS = ["*"]

# Allow PythonAnywhere domains
ALLOWED_HOSTS.append('.pythonanywhere.com')

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# CSRF Settings
CSRF_TRUSTED_ORIGINS = ['https://*.pythonanywhere.com']
if RENDER_EXTERNAL_HOSTNAME:
    CSRF_TRUSTED_ORIGINS.append(f'https://{RENDER_EXTERNAL_HOSTNAME}')

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + str(BASE_DIR / "db.sqlite3"),
        conn_max_age=600,
    )
}

# Wagtail settings
WAGTAILADMIN_BASE_URL = os.environ.get("WAGTAILADMIN_BASE_URL", "https://" + (RENDER_EXTERNAL_HOSTNAME or "example.com"))

# Static files
# https://docs.djangoproject.com/en/5.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

try:
    from .local import *
except ImportError:
    pass
