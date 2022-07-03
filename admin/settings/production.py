from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Crie a secret key para seu ambiente de desenvolvimento
SECRET_KEY = 'q_a$9$rq9an++-iiy7gn^f=j-n#(zswduraa88jb&2%jizcjvt'

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