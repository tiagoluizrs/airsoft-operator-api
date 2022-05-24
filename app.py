from flask import Flask, request, redirect, Response, json
from flask_sqlalchemy import SQLAlchemy
from models.User import User, Role, Patent, Team

import config

app = Flask(__name__, template_folder='templates')
app.secret_key = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/')
def home():
    # user = db.session.query(User).filter(User.username=='Magrinho').update({'username': 'magrinho'})
#     role1 = Role()
#     role1.name = "Admin"
#     role2 = Role()
#     role2.name = "Operator"
#     db.session.add(role1)
#     db.session.add(role2)
    
#     patent1 = Patent()
#     patent1.name = "Capitão"
#     patent2 = Patent()
#     patent2.name = "Operador"
#     patent3 = Patent()
#     patent3.name = "Recruta"
#     db.session.add(patent1)
#     db.session.add(patent2)
#     db.session.add(patent3)

#     team = Team()
#     team.name = "Comandos Airsoft Brasil"
#     db.session.add(team)

#     db.session.commit()

#     user = User()
#     user.email = "tiagoluizrs@gmail.com"
#     user.username = "Magrinho"
#     user.password = user.hashPassword("#Tiagos3v3n")
#     user.role = 1
#     user.team = 1
#     user.patent = 3

    # db.session.add(user)
    # db.session.commit()

    return 'App is running'

@app.route('/login', methods=['POST'])
def login():
    data = {}
    print(request.json)
    userEmail = request.json['userEmail']
    password = request.json['password']

    user = db.session.query(User).filter(User.email==userEmail)
    if not user.first():
        user = db.session.query(User).filter(User.username==userEmail)

    if user.first():
        user = user.filter(User.active==1).first()
        if user:
            verifyPassword = user.verifyHash(password, user.password)
            if user is not None and verifyPassword:
                response = {
                    'status': 200,
                    'message': 'Usuário logado com sucesso.',
                    'messageType': 'success',
                    'data': {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email,
                        'patent': user.patent,
                        'team': user.team,
                        'role': user.role,
                        'created_at': user.created_at,
                        'updated_at': user.updated_at,
                        'active': user.active
                    }
                }
            else:
                response = {
                    'status': 404,
                    'message': 'Dados de usuário incorreto.',
                    'messageType': 'danger',
                    'data': None
                }
        else:
            response = {
                'status': 404,
                'message': 'Usuário inativo. Confirme o e-mail para ativá-lo.',
                'messageType': 'danger',
                'data': None
            }
    else:
        response = {
            'status': 404,
            'message': 'Usuário inexistente .',
            'messageType': 'danger',
            'data': None
        }

    return Response(json.dumps(response), mimetype='application/json'), response['status'], {}



