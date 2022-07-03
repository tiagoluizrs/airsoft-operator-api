from .settings import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Crie a secret key para seu ambiente de desenvolvimento
SECRET_KEY = 'q_a$9$rq9an++-iiy7gn^f=j-n#(zswduraa88jb&2%jizcjvt'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}