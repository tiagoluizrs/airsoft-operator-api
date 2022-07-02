from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from admin.Admin import start_views
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from blueprints.auth import auth
from blueprints.admin import admin
from blueprints.weapons import weapons

from controllers.UserController import UserController

from config import app_config, app_active
config = app_config[app_active]

app = Flask(__name__, template_folder='templates')

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(weapons, url_prefix='/weapon')
app.register_blueprint(admin, url_prefix='/_admin')

app.secret_key = config.SECRET_KEY
app.config.from_object(config)
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_ADMIN_SWATCH'] = 'paper'

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
db.init_app(app)

start_views(app, db)
Bootstrap(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/')
def home():
    return 'App is running'

@login_manager.user_loader
def load_user(user_id):
    user = UserController()
    return user.get_user_by_id(user_id)