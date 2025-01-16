from flask import Flask
from .config import Config
from .extensions import db, login_manager, admin
# from .admin import init_admin
from flask_admin.contrib.sqla import ModelView
from .models.user import User
from .admin_views.base import SecureModelView

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    admin.add_view(SecureModelView(User, db.session))

    from .views.auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/')


    return app
