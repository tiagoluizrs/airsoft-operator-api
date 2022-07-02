from flask import Blueprint, request, redirect, render_template
from flask_login import LoginManager, login_user, logout_user, current_user

from controllers.AuthController import AuthController

from config import app_config, app_active
config = app_config[app_active]

admin = Blueprint('_admin', __name__, template_folder='templates')

@admin.route('/login/')
def login():
    if current_user.is_authenticated :
        return redirect('/admin')

    return render_template('login.html', data={'status': 200, 'msg': None, 'type': None, 'url': '{}'.format(f'{config.URL}')})

@admin.route('/login/', methods=['POST'])
def login_post():
    authC = AuthController()

    email = request.form['email']
    password = request.form['password']

    response = authC.authenticate(email, password, True)
    if response:
        if response['status'] == 200:
            if response['object'].role_id != 1:
                return render_template('login.html', data={'status': 400, 'msg': 'Seu usuário não tem permissão para acessar o admin', 'type':2, 'url': '{}'.format(f'{config.URL}/admin')})
            else:
                login_user(response['object'])
                return redirect(f'{config.URL}admin')

    return render_template('login.html', data=response)

@admin.route('/logout')
def logout_send():
    logout_user()
    return render_template('login.html', data={'status': 200, 'msg': 'Usuário deslogado com sucesso!', 'type':3})