from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from .admin_views.base import SecureIndexView
from flask_migrate import Migrate
from flask_socketio import SocketIO



db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
socketio = SocketIO()
login_manager.login_view = "auth.login"
admin = Admin(name="App Admin panel", template_mode="bootstrap4",index_view=SecureIndexView())

from .models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
