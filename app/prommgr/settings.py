"""
Django settings for prommgr project.

Generated by 'django-admin startproject' using Django 1.8.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from distutils.util import strtobool


def string_to_bool(string):
    return bool(strtobool(str(string)))


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    ')os73z-ew^jc#jhg!am(hxltn&x8dh$(_9d+7h$36d(1sjml-m'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = string_to_bool(
    os.getenv(
        'DEBUG',
        False
    )
)

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'restapi',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'prommgr.urls'

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

WSGI_APPLICATION = 'prommgr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
LOCAL_SERVER = string_to_bool(
    os.getenv(
        'LOCAL_SERVER',
        False
    )
)

if LOCAL_SERVER:
    DB_ENGINE = 'django.db.backends.sqlite3'
    DB_NAME = os.path.join(BASE_DIR, 'db.sqlite3'),
    DB_USER = ''
    DB_HOST = ''
    DB_PASS = ''
    DB_PORT = ''
else:
    DB_ENGINE = 'django.db.backends.postgresql_psycopg2'
    DB_USER = os.getenv('DB_USER')
    DB_NAME = os.getenv('DB_NAME')
    DB_HOST = os.getenv('DB_HOST')
    DB_PASS = os.getenv('DB_PASS')
    DB_PORT = os.getenv('DB_PORT', 5432)

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

if not LOCAL_SERVER:
    DATABASES['OPTIONS'] = {
        'timeout': 20,
    }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
