from src.config.enums.chat import ChatUserRole
from src.chat.messages import (
    add_assistant_message,
    add_system_message,
    add_user_message,
)


def test_add_user_message(message_chat_id, generic_message):
    generic_message(
        message_chat_id, ChatUserRole.USER, "user message", add_user_message
    )


def test_add_system_message(message_chat_id, generic_message):
    generic_message(
        message_chat_id, ChatUserRole.SYSTEM, "system message", add_system_message
    )


def test_add_assistant_message(message_chat_id, generic_message):
    generic_message(
        message_chat_id,
        ChatUserRole.ASSISTANT,
        "assistant message",
        add_assistant_message,
    )
