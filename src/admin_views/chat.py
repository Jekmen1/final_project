from .base import SecureModelView


class ChatView(SecureModelView):
    can_edit = False
    can_create = False
    can_delete = False

    column_list = ["id", "name"]

    column_filters = ["id"]

class MSGView(SecureModelView):
    can_edit = False
    can_create = False
    can_delete = True

    column_list = ["user_id", "room_id", "content", "timestamp"]

    column_filters = ["room_id", "content"]



