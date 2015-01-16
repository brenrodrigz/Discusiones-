from .base import *
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
    	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'curso',
        'USER': 'brenda',
        'PASSWORD': 'brenda',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
STATIC_URL = '/static/'