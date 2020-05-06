from app.database import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    companies = db.relationship("Company", backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String(64), index=True, unique=True)
    logoCompany = db.Column(db.LargeBinary)
    tagLine = db.Column(db.String(64))
    foreword = db.Column(db.String(256))
    aboutUs = db.Column(db.String(256))
    workWithUs = db.Column(db.String(256))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    games = db.relationship("Game", backref='company', lazy='dynamic')


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    picture = db.Column(db.LargeBinary)
    describe = db.Column(db.String(256))
    companyId = db.Column(db.Integer, db.ForeignKey('company.id'))
