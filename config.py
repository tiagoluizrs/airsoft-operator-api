import os

class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = 'zVVAgQkWk48T6WTxyi9S6Z7dVA1rYizP'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class DevelopmentConfig(Config):
    TESTING = False
    DEBUG = True
    IP_HOST = '0.0.0.0'
    PORT_HOST = 8000
    URL = 'http://%s:%s/' % (IP_HOST, PORT_HOST)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:#Tiagos3v3n@localhost:3306/my_operator'

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL = 'http://%s:%s/' % (IP_HOST, PORT_HOST)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:#Tiagos3v3n@localhost:3306/my_operator'

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = '0.0.0.0'
    PORT_HOST = 8080
    URL = 'https://airsoft-operator-api.herokuapp.com/'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://tiagosilva01:Brendhas3v3n@mysql.tiagosilva.dev:3306/tiagosilva01'

app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')