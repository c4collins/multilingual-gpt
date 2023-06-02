from enum import Enum
from . import gettext

_ = gettext.gettext


class ChatUserRole(Enum):
    USER = _("user")
    SYSTEM = _("system")
    ASSISTANT = _("assistant")
