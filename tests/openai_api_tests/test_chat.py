# from data.models.chat_message import ChatMessage
from src.chat import prompts
from src.config.enums.chat import ChatUserRole
from src.chat.messages import (
    add_assistant_message,
    add_system_message,
    add_user_message,
)
from src.chat.mechanicals import build_chat_history


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


def test_generate_chat_completion():
    pass


def test_build_chat_history(session, chat_id):
    add_system_message(session, chat_id, f"{prompts.new_chat_with_purpose}: Get tested")
    add_user_message(session, chat_id, "Who won the world series in 2020?")
    add_assistant_message(
        session, chat_id, "The Los Angeles Dodgers won the World Series in 2020."
    )
    add_user_message(session, chat_id, "Where was it played?")
    session.commit()
    session.flush()
    chat_history: str = build_chat_history(session, chat_id)

    assert len(chat_history) == 4
    print(chat_history)
    assert chat_history[-1]["role"] == ChatUserRole.USER.value
    assert chat_history[-2]["role"] == ChatUserRole.ASSISTANT.value
    assert chat_history[0]["role"] == ChatUserRole.SYSTEM.value
