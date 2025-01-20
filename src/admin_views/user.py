from .base import SecureModelView

class UserView(SecureModelView):
    can_delete = False
    can_create = False
    can_edit = False

    column_exclude_list = ["password"]