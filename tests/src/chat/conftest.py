from pytest import fixture
from typing import Callable
from sqlalchemy import desc
from pytest import mark, fixture

from data.models.chat_message import ChatMessage
from data.models.chat import Chat


@fixture(scope="session")
def chat_completion_chat_id(session):
    chat = Chat(name="chat completion test chat")
    session.add(chat)
    session.commit()
    session.refresh(chat)
    chat_id = chat.id
    yield chat_id


@fixture(scope="session")
def message_chat_id(session):
    chat = Chat(name="message test chat")
    session.add(chat)
    session.commit()
    session.refresh(chat)
    chat_id = chat.id
    yield chat_id


@fixture(scope="session")
def chat_id(session):
    chat = Chat(name="Test chat")
    session.add(chat)
    session.commit()
    session.refresh(chat)
    chat_id = chat.id
    yield chat_id


@fixture(scope="session")
def generic_message(session):
    def _send_message(chat_id: int, role_name: str, message: str, message_fn: Callable):
        message_count: int = session.query(ChatMessage).count()
        last_message: ChatMessage = (
            session.query(ChatMessage).order_by(desc(ChatMessage.id)).first()
        )
        message_fn(session, chat_id, message)
        final_message: ChatMessage = (
            session.query(ChatMessage).order_by(desc(ChatMessage.id)).first()
        )
        assert message_count + 1 == session.query(ChatMessage).count()
        assert last_message != final_message
        assert final_message.role.name == role_name

    return _send_message
