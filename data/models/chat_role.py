from . import *

from src.config.enums.chat import ChatUserRole


class ChatRole(Base):
    __tablename__ = "openapi_chat_role"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Enum(ChatUserRole), nullable=False)
    created = Column(DateTime)
    modified = Column(DateTime)
    messages = relationship("ChatMessage", back_populates="role")

    def __repr__(self):
        return f"ChatRole(id={self.id})"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name.value,  # Convert the Enum value to its underlying value
            "created": self.created,
            "modified": self.modified,
        }

    def __str__(self):
        return self.name.value  # Convert the Enum value to its underlying value
