from flask import Blueprint, request, Response, json, abort
from controllers.AuthController import AuthController

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['POST'])
def login():
    userEmail = request.json['userEmail']
    password = request.json['password']
    authC = AuthController()

    response = authC.authenticate(userEmail, password)

    return Response(json.dumps(response), mimetype='application/json'), response['status'], {}
