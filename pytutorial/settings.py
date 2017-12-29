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

BASE_ROOT = os.path.abspath(os.path.join(os.path.split(__file__)[0], '..'))
STATIC_ROOT = os.path.join(BASE_ROOT, 'static/')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*m&(&5!c^7j^7s$33u(bt567k!q0)@&p1io_w($ec+g66zr!0@'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = os.environ.get("DEBUG", "off") == "on"

ALLOWED_HOSTS = ['*']

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend"
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'stream_twitter',
    'stream_django',
    'pytutorial',
)

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': os.path.join(BASE_DIR, "templates"),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

ROOT_URLCONF = 'pytutorial.urls'

WSGI_APPLICATION = 'pytutorial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {'default': dj_database_url.config()}

if not DATABASES.get('default'):
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STREAM_NEWS_FEEDS = dict(timeline='timeline')

LOGIN_URL = '/'
USE_AUTH = bool(os.environ.get('USE_AUTH'))
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = False
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_VERIFICATION = "none"
SITE_ID = int(os.environ.get('SITE_ID', 1))
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

DEMO_USERNAME = 'theRealAlbert'
DEMO_PASSWORD = '1234'

AUTH_PROFILE_MODULE = 'stream_twitter.UserProfile'

# add your api keys from https://getstream.io/dashboard/
# you do not need this if you are running on Heroku
# and using getstream add-on
STREAM_API_KEY = ''
STREAM_API_SECRET = ''

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

ROLLBAR_ACCESS_TOKEN = os.environ.get('ROLLBAR_ACCESS_TOKEN')

if ROLLBAR_ACCESS_TOKEN is not None:
    MIDDLEWARE_CLASSES += ('rollbar.contrib.django.middleware.RollbarNotifierMiddleware',)
    ROLLBAR = {
        'access_token': ROLLBAR_ACCESS_TOKEN,
        'environment': 'development' if DEBUG else 'production',
        'branch': 'master',
        'root': BASE_DIR,
    }
