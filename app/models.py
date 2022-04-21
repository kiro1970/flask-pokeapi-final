from email.policy import default
from enum import unique
from app import db, login
from datetime import datetime
from sqlalchemy import UniqueConstraint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Battle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id =db.Column(db.Integer, db.ForeignKey('user.id'))
    YourPokemon = db.Column(db.String(100))
    OpponentsPokemon = db.Column(db.String(100))
    Winner = db.Column(db.String(10))

    def __repr__(self):
        return f'id {self.id} {self.YourPokemon} {self.OpponentsPokemon} {self.Winner}'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(), index=True, unique=True)
    password = db.Column(db.String())
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    battles = db.relationship('Battle', backref='player', lazy='dynamic')
    
    def __repr__(self):
        return f'id {self.id} {self.name} {self.email}'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))