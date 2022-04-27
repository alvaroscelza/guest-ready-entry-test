import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _

APP_NAME = '<<app name>>'
APP_DESCRIPTION = _('<<app description>>')
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]
BASE_DIR = Path(__file__).parent.parent.parent
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]
LOCAL_APPS = [
    'applications.apps.CoreConfig'
]
EXTERNAL_APPS = []
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + EXTERNAL_APPS
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
REST_FRAMEWORK = {
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S.%f',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'EXCEPTION_HANDLER': 'backend.applications.utils.exception_handler',
    'PAGE_SIZE': 10
}
ROOT_URLCONF = 'config.urls'
SECRET_KEY = os.getenv('SECRET_KEY')
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'generic_helper': 'templatetags.generic_helper',
            },
        },
    },
]
WSGI_APPLICATION = 'config.wsgi.application'

# region Internationalization
LANGUAGE_CODE = 'es'
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
LANGUAGES = [('es', _('Spanish'))]
TIME_ZONE = 'America/Montevideo'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# endregion

# region Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_storage')
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# endregion
