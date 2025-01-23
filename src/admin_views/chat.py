from .base import SecureModelView


class ChatView(SecureModelView):
    can_edit = False
    can_create = True
    can_delete = True

    # form_columns = ("name",)
    # column_list = ("id", "name")




class MSGView(SecureModelView):
    can_edit = False
    can_create = False
    can_delete = False


