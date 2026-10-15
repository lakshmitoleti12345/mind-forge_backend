import os
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-mindforge-super-secret-key-for-portfolio-demo'
)

# In production (Vercel) keep DEBUG off so errors return clean JSON, not HTML
DEBUG = os.environ.get('DJANGO_DEBUG', 'False').lower() in ('true', '1', 'yes')

# ---------------------------------------------------------------------------
# Vercel read-only filesystem workaround
# Vercel's serverless environment mounts the project directory as read-only.
# SQLite can only be opened for writing inside /tmp.  On cold-start we copy
# the bundled db.sqlite3 (which holds the seeded decks/cards data) to /tmp
# so that auth writes (register, login session) succeed.
# ---------------------------------------------------------------------------
_BUNDLED_DB = BASE_DIR / 'db.sqlite3'
_TMP_DB = Path('/tmp/db.sqlite3')

if os.environ.get('VERCEL'):
    # Only copy if the /tmp copy doesn't exist yet (or is older/smaller)
    if not _TMP_DB.exists() and _BUNDLED_DB.exists():
        shutil.copy2(_BUNDLED_DB, _TMP_DB)
    _ACTIVE_DB = str(_TMP_DB)
else:
    _ACTIVE_DB = str(_BUNDLED_DB)

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party apps
    'rest_framework',
    'corsheaders',
    # Local apps
    'api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mindforge_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mindforge_backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': _ACTIVE_DB,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS & CSRF Settings for Cookie Auth
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:5173',
    'http://localhost:5173',
    'http://127.0.0.1:8000',
    # Vercel deployment domains
    'https://*.vercel.app',
    'https://mind-forge-backendfolder.vercel.app',
]

# Use signed-cookie sessions so login() doesn't need a DB write.
# The session data is stored client-side in a signed cookie (tamper-proof).
# This avoids an extra SQLite write on every login call.
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_SAMESITE = 'None'   # Required for cross-site cookie delivery
SESSION_COOKIE_SECURE = True       # Required when SameSite=None
SESSION_COOKIE_HTTPONLY = False

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}
