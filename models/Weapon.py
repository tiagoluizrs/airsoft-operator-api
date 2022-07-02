from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from models.User import User

db = SQLAlchemy()

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    image = db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return self.name

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    
    def __repr__(self):
        return self.name

class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    image = db.Column(db.Text, nullable=True)
    fps = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id, ondelete='CASCADE'), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey(Brand.id, ondelete='CASCADE'), nullable=False)
    categoria = relationship(Category)
    brand = relationship(Brand)
    
    def __repr__(self):
        return self.name

class UserWeapon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    weapon_id = db.Column(db.Integer, db.ForeignKey(Weapon.id), nullable=False)
    created_at = db.Column(db.DateTime(6), default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(6), onupdate=db.func.current_timestamp())
    usuario = relationship(User)
    arma = relationship(Weapon)
    
    def __repr__(self):
        try:
            data = db.session.query(Weapon).filter_by(id=self.weapon_id).first()
            name = data.name
        except:
            print("Error")
            name = None
        finally:
            db.session.close()
            return name

class WeaponRating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime(6), default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(6), onupdate=db.func.current_timestamp())
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user_weapon_id = db.Column(db.Integer, db.ForeignKey(UserWeapon.id), nullable=False)
    upped = db.Column(db.Boolean, default=False)
    usuario = relationship(User)
    arma = relationship(UserWeapon)

class FpsWeapon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    userWeapon_id = db.Column(db.Integer, db.ForeignKey(UserWeapon.id), nullable=False)
    created_at = db.Column(db.DateTime(6), default=db.func.current_timestamp())
    
    def __repr__(self):
        return self.userWeapon.user.username

class Equipaments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    type = db.Column(db.Integer)
    price = db.Column(db.Float)
    
    def __repr__(self):
        return self.name