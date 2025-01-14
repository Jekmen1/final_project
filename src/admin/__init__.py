from flask_admin import Admin
from ..models.user import User
from ..extensions import db
from .views import UserAdminView
def init_admin(app):
    """Initialize Flask-Admin."""
    admin = Admin(app, name='Admin Panel', template_mode='bootstrap4')
    admin.add_view(UserAdminView(User, db.session))

