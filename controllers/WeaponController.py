from models.Weapon import Weapon, FpsWeapon, db

class WeaponController:
    def listAll(self, request):
        page = int(request.args.get('page', 1))
        limit = 2

        offset = (page - 1) * limit

        try:
            weapons = db.session.query(Weapon).limit(limit).offset(offset).all()
            if len(weapons) > 0:
                response = {
                    'status': 200,
                    'data': [
                        {
                            'id': weapon.id,
                            'name': weapon.name,
                            'image': weapon.image,
                            'fps': weapon.fps,
                            'category': 'Nada',
                            'brand': 'Nada'
                        } for weapon in weapons
                    ],
                }
        except Exception as e:
            response = {
                'status': 500,
                'msg': str(e)
            }
        finally:
            db.session.close()

        return response