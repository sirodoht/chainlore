import os
import secrets
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PRODUCTION = os.environ.get('CHAINLORE_PRODUCTION') == '1'
DEBUG = not PRODUCTION
DATA_DIR = Path(os.environ.get('CHAINLORE_DATA_DIR', BASE_DIR / '.data'))
DATA_DIR.mkdir(parents=True, exist_ok=True, mode=0o700)
secret_file = DATA_DIR / 'secret-key'
if not secret_file.exists():
    try:
        with open(secret_file, 'x', opener=lambda path, flags: os.open(path, flags, 0o600)) as file:
            file.write(secrets.token_urlsafe(64))
    except FileExistsError:
        pass
SECRET_KEY = secret_file.read_text().strip()
ALLOWED_HOSTS = ['chainlore.xyz'] if PRODUCTION else ['localhost', '127.0.0.1', 'testserver']
INSTALLED_APPS = [
    'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes',
    'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles',
    'submissions',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'submissions.middleware.AdminThrottleMiddleware',
]
ROOT_URLCONF = 'service.urls'
WSGI_APPLICATION = 'service.wsgi.application'
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'service/templates'], 'APP_DIRS': True,
    'OPTIONS': {'context_processors': [
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
    ]},
}]
DATABASES = {'default': {
    'ENGINE': 'django.db.backends.sqlite3', 'NAME': DATA_DIR / 'submissions.sqlite3',
    'OPTIONS': {'timeout': 20, 'transaction_mode': 'IMMEDIATE'},
}}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_TZ = True
SITE_ROOT = Path(os.environ.get('CHAINLORE_SITE_ROOT', BASE_DIR / 'dist'))
ARTICLE_CATALOG = SITE_ROOT / 'article-catalog.json'
STATIC_URL = '/service-static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') if PRODUCTION else None
SECURE_SSL_REDIRECT = PRODUCTION
SESSION_COOKIE_SECURE = PRODUCTION
CSRF_COOKIE_SECURE = PRODUCTION
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 60 * 60 * 8
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SECURE_HSTS_SECONDS = 31536000 if PRODUCTION else 0
# Apply HSTS to this hostname only; do not opt unrelated subdomains or the
# domain into browser preloading as a side effect of adding a forms service.
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SILENCED_SYSTEM_CHECKS = ['security.W005', 'security.W021']
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'same-origin'
X_FRAME_OPTIONS = 'DENY'
DATA_UPLOAD_MAX_MEMORY_SIZE = 65536
DATA_UPLOAD_MAX_NUMBER_FIELDS = 30
FILE_UPLOAD_MAX_MEMORY_SIZE = 0
# Email secrets live in the environment or private DATA_DIR, outside the repository.
admin_email_file = DATA_DIR / 'admin-email'
ADMIN_NOTIFICATION_EMAIL = os.environ.get('CHAINLORE_ADMIN_EMAIL',
    admin_email_file.read_text().strip() if admin_email_file.exists() else '').strip()
postmark_token_file = DATA_DIR / 'postmark-token'
POSTMARK_TOKEN = postmark_token_file.read_text().strip() if postmark_token_file.exists() else ''
if POSTMARK_TOKEN:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.postmarkapp.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = EMAIL_HOST_PASSWORD = POSTMARK_TOKEN
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Without a token, production skips notifications rather than logging addresses to the console.
NOTIFICATIONS_ENABLED = bool(POSTMARK_TOKEN) or not PRODUCTION
EMAIL_TIMEOUT = 10
DEFAULT_FROM_EMAIL = 'Chainlore <notifications@chainlore.xyz>'
