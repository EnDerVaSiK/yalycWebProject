from app import create_app
from flask_login import LoginManager

app = create_app()
login = LoginManager(app)

if __name__ == '__main__':
    app.run()
