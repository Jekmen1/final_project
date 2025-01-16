from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
admin = Admin()

from .models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
