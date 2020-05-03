from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from config import DevelopmentConfig, ProductionConfig
from .database import db


def create_app():
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    from app import controllers

    migrate = Migrate(app, db)

    return app
