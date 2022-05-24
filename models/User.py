from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256

db = SQLAlchemy()

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)

class Patent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(6), default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(6), onupdate=db.func.current_timestamp())
    active = db.Column(db.Boolean(), default=True)
    team = db.Column(db.Integer, db.ForeignKey(Team.id), nullable=False)
    patent = db.Column(db.Integer, db.ForeignKey(Patent.id), nullable=False)
    role = db.Column(db.Integer, db.ForeignKey(Role.id), nullable=False)

    def hashPassword(self, password):
        try:
            return pbkdf2_sha256.hash(password)
        except:
            print("Erro ao criptografar")
        
    def verifyHash(self, password, hash):
        try:
            return pbkdf2_sha256.verify(password, hash)
        except ValueError:
            return False