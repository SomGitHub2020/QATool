"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2l5ce8_qw+2ks#!3%t-gk-7s0ok4ry62e1!r19r)+@j#hfw3a+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',            # add this
    'rest_framework',         # add this    
    'rest_framework.authtoken',
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'customuser',
    'qaconfig',
    'django_filters',
    'qalog.apps.QalogConfig',
    'autoproc',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',    # add this
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend')], # BASE_DIR = django-todo-react, 
                                                      #so this whole new path is django-todo-react/frontend
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': 'postgres', # database name
        #'USER': 'postgres', # user name to access postgresql server
        #'PASSWORD': 'postgre2020', # password to access postgresql server
        #'HOST': '127.0.0.1', # ip server where postgresql is hosted 
        #'PORT': '5432', # port of the server to listen

        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': 'postgres', # database name
        'USER': 'postgres', # user name to access postgresql server
        'PASSWORD': 'postgre2020', # password to access postgresql server
        'HOST': 'actualdb', # ip server where postgresql is hosted # '127.0.0.1', 
        'PORT': '5432', # port of the server to listen
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# same as we have DIRS in TEMPLATES, 
# but with a name to be joined into staticfiles directory
REACT_APP = os.path.join(BASE_DIR, 'frontend') 

STATICFILES_DIRS = [
    os.path.join(REACT_APP, "build","static"), # this is now pathed to django-todo-react/frontend/build/static
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^.*'
CORS_ORIGIN_WHITELIST = ['http://localhost:3000',
                         'http://9.79.245.254:3000',
                         'http://9.206.183.228:3000'
                            ]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}