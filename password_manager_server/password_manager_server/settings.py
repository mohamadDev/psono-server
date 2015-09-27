"""
Django settings for password_manager_server project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import yaml
HOME = os.path.expanduser('~')

with open(os.path.join(HOME, '.password_manager_server', 'settings.yaml'), 'r') as stream:
    config = yaml.load(stream)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config['DEBUG']

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',
    'rest_framework',
    #'rest_framework.authtoken',
    #'rest_auth',
    #'allauth',
    #'allauth.account',
    #'rest_auth.registration',
    'restapi',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'middleware.sqlprinter.SQLLogToConsoleMiddleware',
)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10
}

ROOT_URLCONF = 'password_manager_server.urls'

CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = config['TEMPLATES']

WSGI_APPLICATION = 'password_manager_server.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = config['DATABASES']

EMAIL_FROM = config['EMAIL_FROM']
AUTH_KEY_LENGTH_BYTES = config.get('AUTH_KEY_LENGTH_BYTES', 64)
USER_PRIVATE_KEY_LENGTH_BYTES = config.get('USER_PRIVATE_KEY_LENGTH_BYTES', 80)
USER_PUBLIC_KEY_LENGTH_BYTES = config.get('USER_PUBLIC_KEY_LENGTH_BYTES', 32)
USER_SECRET_KEY_LENGTH_BYTES = config.get('USER_SECRET_KEY_LENGTH_BYTES', 80)
NONCE_LENGTH_BYTES = config.get('NONCE_LENGTH_BYTES', 24)
ACTIVATION_LINK_SECRET = config['ACTIVATION_LINK_SECRET']
ACTIVATION_LINK_TIME_VALID = config.get('ACTIVATION_LINK_TIME_VALID', 2592000) # in seconds
TOKEN_TIME_VALID = config.get('TOKEN_TIME_VALID', 86400) # in seconds

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_URL = '/static/'
