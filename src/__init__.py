from flask import Flask
from .config import Config
from .extensions import db, login_manager, admin, migrate
from flask_admin.contrib.sqla import ModelView
from .models.user import User
from .models.chat import ChatRoom, Message
from .admin_views.base import SecureModelView
from.commands import init_db, populate_db


COMMANDS = [
    init_db,
    populate_db
]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_ext(app)
    login_manager.init_app(app)
    admin.init_app(app)
    admin.add_view(SecureModelView(User, db.session))
    register_commands(app)

    from .views.auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/')


    return app


def register_ext(app):
    db.init_app(app)

    migrate.init_app(app, db)

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
