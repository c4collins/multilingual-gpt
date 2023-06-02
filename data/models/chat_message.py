from . import *
from .chat import Chat
from .chat_role import ChatRole


class ChatMessage(Base):
    __tablename__ = "open_api_chat_message"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String)
    created = Column(DateTime)
    modified = Column(DateTime)
    chat_id = Column(Integer, ForeignKey("openapi_chat.id"))
    role_id = Column(Integer, ForeignKey("openapi_chat_role.id"))
    chat = relationship("Chat", back_populates="messages")
    role = relationship("ChatRole", back_populates="messages")

    def __repr__(self):
        return f'ChatMessage#{self.id}(from={self.role.name.value}, content="{self.content}")'

    def as_conversation(self):
        return {"role": self.role.name.value, "content": self.content}
