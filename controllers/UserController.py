from models.User import User, db

class UserController:
    def get_user_by_id(self, id):
        try:
            res = db.session.query(User).filter(User.id == id).first()
        except Exception as e:
            res = None
            print(e)
        finally:
            db.session.close()
        return res