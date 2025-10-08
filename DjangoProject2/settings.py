# from pathlib import Path
# import os
# from dotenv import load_dotenv
# import dj_database_url
# load_dotenv()
#
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-fallback-key-for-dev-only')
#
# DEBUG = False
#
# ALLOWED_HOSTS = ['*']
# AUTH_USER_MODEL = 'core.User'
# # Application Definition
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'django.contrib.sites',
#     'django_cron',
#
#     # Allauth
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',
#     'allauth.socialaccount.providers.google',
#
#     # Your apps
#     'rest_framework',
#     'core',
# ]
#
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'allauth.account.middleware.AccountMiddleware',
#     'core.middleware.SessionTimeoutMiddleware',
# ]
#
# ROOT_URLCONF = 'DjangoProject2.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'core/templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'DjangoProject2.wsgi.application'
#
# # Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
#
# # Password Validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]
#
# # Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'Asia/Kolkata'
# USE_I18N = True
# USE_TZ = True
#
# # Static Files
# STATIC_URL = 'static/'
# STATICFILES_DIRS = [BASE_DIR / 'static']
# STATIC_ROOT = BASE_DIR / 'staticfiles'
#
# # Create static directory if it doesn't exist
# os.makedirs(BASE_DIR / 'static', exist_ok=True)
#
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
# # Email Settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')
#
# # Allauth Settings
# SITE_ID = 1
# AUTHENTICATION_BACKENDS = [
#
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# ]
#
# # Authentication URLs
# ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
# SOCIALACCOUNT_LOGIN_ON_GET = True
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'  # Use 'https' in production
#
# ADMIN_LOGIN_URL = '/admin/login/'
# LOGIN_URL = 'account_login'
# LOGIN_REDIRECT_URL = '/'  # Where to redirect after login
# LOGOUT_REDIRECT_URL = '/'# LOGOUT_REDIRECT_URL = '/'  # Where users go after logout
# # ACCOUNT_SIGNUP_REDIRECT_URL = '/accounts/login/?success=true'
# # Account configuration (updated to use new settings)
# ACCOUNT_LOGIN_METHODS = ['username', 'email']
# ACCOUNT_EMAIL_VERIFICATION = 'none'
# ACCOUNT_SESSION_REMEMBER = True
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_LOGOUT_ON_GET = True
# # Corrected ACCOUNT_SIGNUP_FIELDS to use 'password1' and 'password2'
# ACCOUNT_SIGNUP_FIELDS = ['email', 'username', 'password1', 'password2']
# ACCOUNT_LOGIN_ON_REGISTRATION = False
# #ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Requires email verification before login
# ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False  # Disable auto-redirect after signup
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False  # Don't auto-login after email confirmation
# ACCOUNT_SIGNUP_REDIRECT_URL = '/accounts/login/'
# # LOGOUT_REDIRECT_URL = '/listuniv/'
# # Social Account Providers
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'APP': {
#             'client_id': os.getenv('GOOGLE_CLIENT_ID'),
#             'secret': os.getenv('GOOGLE_CLIENT_SECRET'),
#         },
#         'SCOPE': ['profile', 'email'],
#         'AUTH_PARAMS': {'access_type': 'online'},
#         # Add this to skip the intermediate page:
#         # 'OAUTH_PKCE_ENABLED': True,
#     }
# }
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.TokenAuthentication',
#     ],
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticatedOrReadOnly',
#     ]
# }
# SESSION_COOKIE_AGE = 300
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# # Allauth settings for custom user model
# ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = True
# ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
#
#
#
#
# # Add this to handle the custom user model with allauth
# SOCIALACCOUNT_ADAPTER = 'allauth.socialaccount.adapter.DefaultSocialAccountAdapter'
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'










# settings.py

from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

# Load environment variables from a .env file for local development
load_dotenv()

# --- Core Django Settings ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Production/Development Switch ---
# Render sets the 'RENDER' environment variable to 'true'
IS_PRODUCTION = os.environ.get('RENDER') == 'true'

SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY and not IS_PRODUCTION:
    # Use a fallback key for local development if SECRET_KEY is not set
    SECRET_KEY = 'django-insecure-fallback-key-for-dev-only'

DEBUG = not IS_PRODUCTION

# --- Host Configuration ---
ALLOWED_HOSTS = []
# On Render, the RENDER_EXTERNAL_HOSTNAME is automatically set
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
if not IS_PRODUCTION:
    ALLOWED_HOSTS.append('127.0.0.1') # For local development

# --- Application Definitions ---
AUTH_USER_MODEL = 'core.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_cron',

    # Allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # Your apps
    'rest_framework',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # --- Whitenoise Middleware for Production Static Files ---
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'core.middleware.SessionTimeoutMiddleware',
]

ROOT_URLCONF = 'DjangoProject2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'core/templates')],
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

WSGI_APPLICATION = 'DjangoProject2.wsgi.application'

# --- Database Configuration ---
DATABASES = {
    'default': dj_database_url.config(
        # Fallback to a local SQLite database if DATABASE_URL is not set
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600  # Enable persistent connections
    )
}

# --- Password Validation ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Internationalization ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# --- Static and Media Files ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

if IS_PRODUCTION:
    # Use Whitenoise to serve static files with compression and caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- Email Settings ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')

# --- Allauth Settings ---
SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https' if IS_PRODUCTION else 'http'
# ... (all your other specific allauth settings remain the same) ...
ACCOUNT_LOGIN_METHODS = ['username', 'email']
ACCOUNT_EMAIL_VERIFICATION = 'none'
# ... etc.

# --- REST Framework ---
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}

# --- Session Management ---
SESSION_COOKIE_AGE = 300
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# --- Production Security Settings ---
if IS_PRODUCTION:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True # Optional: If you want to force all connections to HTTPS
    SECURE_HSTS_SECONDS = 31536000 # Optional: 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True # Optional
    SECURE_HSTS_PRELOAD = True # Optional