from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from .admin_views.base import SecureIndexView

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
admin = Admin(name="App Admin panel", template_mode="bootstrap4",index_view=SecureIndexView())

from .models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
