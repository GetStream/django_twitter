"""
Django settings for pytutorial project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(__file__)
TEMPLATE_PATH = os.path.join(BASE_DIR, "templates")

BASE_ROOT = os.path.abspath(os.path.join(os.path.split(__file__)[0], '..'))
STATIC_ROOT = os.path.join(BASE_ROOT, 'static/')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*m&(&5!c^7j^7s$33u(bt567k!q0)@&p1io_w($ec+g66zr!0@'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = os.environ.get("DEBUG", "on") == "on" 
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, "fixtures")
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stream_twitter',
    'stream_django',
    'pytutorial',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pytutorial.urls'

WSGI_APPLICATION = 'pytutorial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {'default':dj_database_url.config()}
# DATABASES = {}

# print(DATABASES.get('default'))


DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
} if not DATABASES.get('default') else DATABASES.get('default')

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)

STREAM_NEWS_FEEDS = dict(flat='flat')

LOGIN_URL='/accounts/login'
LOGIN_REDIRECT_URL='tweet'
USE_AUTH = bool(os.environ.get('USE_AUTH'))

# if you run on Heroku you don't need to set this
STREAM_API_KEY = 'h7mu8swwk4aw'
STREAM_API_SECRET = 'cqwmk2cd74h9zrksbfbkxsf8vbcj6f7ks3kfwnh5j5nfy9c593j78zd27ukg8f9d'
