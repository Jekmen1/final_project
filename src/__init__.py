from flask import Flask
from .config import Config
from .extensions import db, login_manager, admin, migrate, socketio
from .models.user import User
from .models.chat import ChatRoom, Message
from .admin_views.base import SecureModelView
from.commands import init_db, populate_db
from.admin_views.user import UserView
from.admin_views.chat import ChatView, MSGView

COMMANDS = [
    init_db,
    populate_db
]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_ext(app)
    login_manager.init_app(app)
    socketio.init_app(app)

    admin.init_app(app)
    admin.add_view(UserView(User, db.session))
    admin.add_view(ChatView(ChatRoom, db.session))
    admin.add_view(MSGView(Message, db.session))

    register_commands(app)

    from .views.auth.routes import auth_bp
    from .views.chat_view.routes import chat_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(chat_bp)


    return app


def register_ext(app):
    db.init_app(app)

    migrate.init_app(app, db)

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
