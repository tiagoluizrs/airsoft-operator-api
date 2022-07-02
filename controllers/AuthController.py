from models.User import User, db

class AuthController:
    def authenticate(self, userEmail, password, _object=False):
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
                            'patent_id': user.patent_id,
                            'team_id': user.team_id,
                            'role_id': user.role_id,
                            'created_at': user.created_at,
                            'updated_at': user.updated_at,
                            'active': user.active
                        },
                    }

                    if _object:
                        response.update({'object': user})
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

        return response