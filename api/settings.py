"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import logging
import os
import socket
import sys
import urllib3

from api.kms import KMS
from datetime import timedelta
from decouple import config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

docker_id = socket.gethostname()

logging.basicConfig(
    format='%(asctime)s | ' + docker_id + ' | %(levelname)s | %(message)s',
    level=logging.DEBUG)
debug = config('DEBUG', default=False, cast=bool)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV = config('ENV', 'LOCAL')

# try to load the keys from KMS if not a LOCAL env and set vars automagically
# if we fail, use the default settings
if ENV != 'LOCAL':
    try:
        KEYS = KMS().fetch_keys()
        os.environ['DB_PASSWORD'] = KEYS.get('DB_PASSWORD')
        os.environ['SOAP_USERNAME'] = KEYS.get('SOAP_USERNAME')
        os.environ['SOAP_PASSWORD'] = KEYS.get('SOAP_PASSWORD')
        os.environ['SOAP_REGISTER_TICKET_CLIENT_ID'] = KEYS.get(
            'SOAP_REGISTER_TICKET_CLIENT_ID')
        os.environ['SOAP_REGISTER_TICKET_CLIENT_SECRET'] = KEYS.get(
            'SOAP_REGISTER_TICKET_CLIENT_SECRET')
    except:
        print('Keeping default keys')
        pass

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', 'SECRET')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
LOCAL = config('LOCAL', default=False, cast=bool)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_nose',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_expiring_authtoken',
    'djoser',
    'oauth',
    'microservices',
    'simulator',
    'health_check',
    'health_check.db',
    'sales',
    'authentication',
    'plans',
    'rentability'
]

XRAY_RECORDER = {
    'AUTO_INSTRUMENT': True,
    'AWS_XRAY_CONTEXT_MISSING': 'LOG_ERROR',
    'AWS_XRAY_DAEMON_ADDRESS':
        config('AWS_XRAY_ADDRESS', '127.0.0.1') + ':2000',
    'AWS_XRAY_TRACING_NAME': 'API',
    'PLUGINS': ('ElasticBeanstalkPlugin', 'EC2Plugin'),
    'SAMPLING': False,
}

if 'test' in sys.argv and LOCAL:
    INSTALLED_APPS.append('test_without_migrations')

if DEBUG:
    INSTALLED_APPS.append('django_extensions')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

if 'test' not in sys.argv:
    MIDDLEWARE.append('request_logging.middleware.LoggingMiddleware')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

if ENV != 'LOCAL' and 'test' not in sys.argv and 'startapp' not in sys.argv:
    INSTALLED_APPS.append('aws_xray_sdk.ext.django')
    MIDDLEWARE.append('aws_xray_sdk.ext.django.middleware.XRayMiddleware')

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', ],
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

WSGI_APPLICATION = 'api.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME', 'api'),
        'USER': config('DB_USER', 'postgres'),
        'PASSWORD': config('DB_PASSWORD', ''),
        'HOST': config('DB_HOST', 'db'),
        'PORT': 5432,
        'CONN_MAX_AGE': 600,
        'TEST': {
            'NAME': 'test-' + config('ENV'),
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, "api/fixtures"),
]

REDIS_URL = config('REDIS_URL', '')
AMOUNT_TICKETS_PER_REQUEST = config(
    'AMOUNT_TICKETS_PER_REQUEST', 50000, cast=int)
MINIMUM_REQUIRED_TICKETS = config(
    'MINIMUM_REQUIRED_TICKETS', 3000, cast=int)
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

AUTH_USER_MODEL = 'authentication.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

DJOSER = {
    'SEND_ACTIVATION_EMAIL': False,
    'ACTIVATION_URL': '/activate/',
    'SERIALIZERS': {
        'user_registration':
            'authentication.serializers.CustomUserRegistrationSerializer',
        'login': 'authentication.serializers.CustomLoginSerializer',
        'password_reset':
            'authentication.serializers.CustomPasswordResetSerializer',
        'set_password':
            'authentication.serializers.CustomSetPasswordSerializer',
        'user': 'authentication.serializers.CustomUserSerializer',
    },
}

EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config('EMAIL_HOST_USER', 'brprev@d3.do')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', 'brasilprev')
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Token expiration
EXPIRING_TOKEN_LIFESPAN = timedelta(hours=24)

# PASSWORD_HASHERS = [
#     'pw_hasher.hasher.PasswordHasher',
# ]

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
MEDIA_URL = '/media/'
