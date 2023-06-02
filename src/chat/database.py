from src.config import session
from data.models.chat import Chat

from . import cli, prompts


def check_for_existing_conversations():
    existing_chat_count = session.query(Chat).count()
    if existing_chat_count and cli.user_wants_to_continue_existing_chat(
        existing_chat_count
    ):
        existing_chats = session.query(Chat).all()
        for chat in existing_chats:
            print(f"{chat.id}: {chat.name}")

        chat_id = cli.ask_user_for_existing_conversation_id_to_load()

        return next((chat for chat in existing_chats if chat.id == chat_id), False)
