from flask import Blueprint, request, Response, json, abort
from controllers.WeaponController import WeaponController

weapons = Blueprint('weapons', __name__, template_folder='templates')

@weapons.route('/', methods=['GET'])
def get_weapon():
    weaponC = WeaponController()

    response = weaponC.listAll(request)

    return Response(json.dumps(response['data']), mimetype='application/json'), response['status'], {}