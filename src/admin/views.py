from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for, flash


class UserAdminView(ModelView):
    """Custom admin view for the User model."""
    column_list = ['id', 'username', 'email', 'is_admin']

    form_columns = ['username', 'email', 'password', 'is_admin']

    def is_accessible(self):
        """Restrict access to authenticated admins only."""
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        """Redirect unauthorized users."""
        flash("You do not have permission to access the admin panel.", "danger")
        return redirect(url_for('auth.login'))
