from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tiagosilva01',
        'USER': 'tiagosilva01',
        'PASSWORD': 'Brendhas3v3n',
        'HOST': 'mysql.tiagosilva.dev',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}