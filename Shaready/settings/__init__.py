"""
Django settings for Shaready project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'viqz4ls2v73*6s*(6t+v^@z3i1-9g=r0$fapz1#+f#u0hm$4_#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'articles',
    'rest_framework',
    'api_articles',
    'api',
    'api_comments',
    'api_user',
    'api_notification',
    'corsheaders',
    'pwa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'Shaready.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "Shaready", "templates"),
)


WSGI_APPLICATION = 'Shaready.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shaready_db',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "../static"),
]

STATIC_URL = '/static/'
INTERNAL_IPS = ['127.0.0.1']

#Direction of user's Models

AUTHENTICATION_BACKENDS = ( 'django.contrib.auth.backends.ModelBackend', )
AUTH_USER_MODEL = 'user.CustomUser'
LOGIN_REDIRECT_URL = 'feed'

#Direction of my image

MEDIA_ROOT = os.path.join(BASE_DIR, '../static/assets/img')

#settings model articles

LikeChoicesArticles = [
    ('1', 'gold_like'),
    ('2', 'like'),
    ('3', 'dislike'),
]

LikeChoicesComment = [
    ('1', 'like'),
    ('2', 'dislike'),
]

ChoicesNotification = [
    ('1', 'follow'),
    ('2', 'like_article'),
    ('3', 'like_comment'),
    ('4', 'comment'),
]

#settings cors 

CORS_ORIGIN_ALLOW_ALL=True

#settings PWA

PWA_APP_NAME = 'Shaready'
PWA_APP_DESCRIPTION = "Shaready is a social information network."
PWA_APP_THEME_COLOR = '#FF3939'
PWA_APP_BACKGROUND_COLOR = '#FF3939'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS =[
   {
      "src": "/static/assets/img/logo_sr_96px.png",
      "sizes": "96x96",
    },
    {
      "src": "/static/assets/img/logo_sr_144px.png",
      "sizes": "144x144",
    },
    {
      "src": "/static/assets/img/logo_sr_192px.png",
      "sizes": "192x192",
    },
    {
      "src": "/static/assets/img/logo_sr_512px.png",
      "sizes": "512x512",
    }
]
PWA_APP_ICONS_APPLE = [
    {
      "src": "/static/assets/img/logo_sr_96px.png",
      "sizes": "96x96",
    },
    {
      "src": "/static/assets/img/logo_sr_144px.png",
      "sizes": "144x144",
    },
    {
      "src": "/static/assets/img/logo_sr_192px.png",
      "sizes": "192x192",
    },
    {
      "src": "/static/assets/img/logo_sr_512px.png",
      "sizes": "512x512",
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/assets/img/logo.svg',
        'media': 'screen and (max-device-width: 500px) and (-webkit-device-pixel-ratio: 2)'
    }
]

PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

#settings drf

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],

     'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        )

