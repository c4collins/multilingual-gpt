from data.models.chat import Chat
from data.models.chat_message import ChatMessage
from data.models.chat_role import ChatRole
from src.config import lang
from src.config.enums.chat import ChatUserRole


# Add any message to the conversation
def add_roled_message(session, chat_id: int, message: str, role_name: ChatUserRole, **kwargs):
    role = session.query(ChatRole).filter_by(name=role_name).first()
    chat: Chat = session.get(Chat, chat_id)
    message = ChatMessage(
        content=f"{lang}: {message}",
        chat=chat,
        role=role,
        chat_id=chat.id,
        role_id=role.id,
        **kwargs,
    )
    session.add(message)
    session.commit()
    session.flush()


# Add user message to the conversation
def add_user_message(session, chat_id: int, message: str, **kwargs):
    add_roled_message(session, chat_id, message, ChatUserRole.USER, **kwargs)


# Add system message to the conversation
def add_system_message(session, chat_id: int, message: str, **kwargs):
    add_roled_message(session, chat_id, message, ChatUserRole.SYSTEM, **kwargs)


# Add assistant message to the conversation
def add_assistant_message(session, chat_id: int, message: str, **kwargs):
    add_roled_message(session, chat_id, message, ChatUserRole.ASSISTANT, **kwargs)
