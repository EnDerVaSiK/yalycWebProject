from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from config import DevelopmentConfig
from .database import db


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db.init_app(app)
with app.test_request_context():
    db.create_all()

migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, errors
