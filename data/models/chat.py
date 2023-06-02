from . import *


class Chat(Base):
    __tablename__ = "openapi_chat"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    created = Column(DateTime)
    modified = Column(DateTime)
    purpose = Column(Text)
    messages = relationship("ChatMessage", back_populates="chat")

    def __repr__(self):
        return f"Chat(id={self.id})"
