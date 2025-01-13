from flask import Flask
from .config import Config
from .extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from .views.auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
