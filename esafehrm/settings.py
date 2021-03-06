"""
Django settings for esafehrm project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR_LOGIN= os.path.join(BASE_DIR,'login/templates')
TEMPLATE_DIR_MASTERS = os.path.join(BASE_DIR,'masters/templates')
TEMPLATE_DIR_PIM = os.path.join(BASE_DIR,'pim/templates')
TEMPLATE_DIR_LEAVES = os.path.join(BASE_DIR,'leaves/templates')
TEMPLATE_DIR_ORGANISATION = os.path.join(BASE_DIR,'organisation/templates')
TEMPLATE_DIR_ORGANISATION = os.path.join(BASE_DIR,'attendance/templates')
TEMPLATE_DIR_EMPPROFILE = os.path.join(BASE_DIR,'empprofile/templates')
TEMPLATE_DIR_PAYROLL = os.path.join(BASE_DIR,'payroll/templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yoph$16411j8b7_-h_x%_$kz0&$439)s_2)hq1*bo9@t@d++e+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'bootstrap4',
    'login.apps.LoginConfig',
    'masters.apps.MastersConfig',
    'organisation.apps.OrganisationConfig',
    'pim',
    'leaves',
    'empprofile',
    'payroll',
    'attendance.apps.AttendanceConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'esafehrm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR_LOGIN,TEMPLATE_DIR_MASTERS,TEMPLATE_DIR_PIM,TEMPLATE_DIR_LEAVES,
        TEMPLATE_DIR_ORGANISATION,TEMPLATE_DIR_EMPPROFILE,TEMPLATE_DIR_PAYROLL],
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

WSGI_APPLICATION = 'esafehrm.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'esafenewdatabase',
        'USER': 'root',
        'PASSWORD':'admin',
        'HOST':'127.0.0.1',
        'PORT':'3306'
    },
    'OPTIONS': { 'init_command' : 'SET storage_engine=MyISAM', }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# EMAIL
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'login/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets') 
# SESSION_COOKIE_SECURE = True

