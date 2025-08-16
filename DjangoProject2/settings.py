from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-fallback-key-for-dev-only')

DEBUG = True

ALLOWED_HOSTS = ['*']
# AUTH_USER_MODEL = 'core.User'
# Application Definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

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

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# Static Files
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Create static directory if it doesn't exist
os.makedirs(BASE_DIR / 'static', exist_ok=True)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')

# Allauth Settings
SITE_ID = 1
AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Authentication URLs
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'  # Use 'https' in production

ADMIN_LOGIN_URL = '/admin/login/'
LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = '/'  # Where to redirect after login
LOGOUT_REDIRECT_URL = '/'# LOGOUT_REDIRECT_URL = '/'  # Where users go after logout
# ACCOUNT_SIGNUP_REDIRECT_URL = '/accounts/login/?success=true'
# Account configuration (updated to use new settings)
ACCOUNT_LOGIN_METHODS = ['username', 'email']
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_LOGOUT_ON_GET = True
# Corrected ACCOUNT_SIGNUP_FIELDS to use 'password1' and 'password2'
ACCOUNT_SIGNUP_FIELDS = ['email', 'username', 'password1', 'password2']
ACCOUNT_LOGIN_ON_REGISTRATION = False
#ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Requires email verification before login
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False  # Disable auto-redirect after signup
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False  # Don't auto-login after email confirmation
ACCOUNT_SIGNUP_REDIRECT_URL = '/accounts/login/'
# LOGOUT_REDIRECT_URL = '/listuniv/'
# Social Account Providers
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': os.getenv('GOOGLE_CLIENT_ID'),
            'secret': os.getenv('GOOGLE_CLIENT_SECRET'),
        },
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        # Add this to skip the intermediate page:
        # 'OAUTH_PKCE_ENABLED': True,
    }
}
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}
SESSION_COOKIE_AGE = 30
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
