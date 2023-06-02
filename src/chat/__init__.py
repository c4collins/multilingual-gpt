from pprint import pprint
from src.config import session
from data.models.chat import Chat
from src.chat.messages import (
    add_system_message,
    add_user_message,
    add_assistant_message,
)
from . import cli, prompts, mechanicals


def _check_resp(resp: str) -> bool:
    return resp == "exit"


def _get_input_from_user(chat_id: int) -> bool:
    user_resp = cli.ask_user_for_input()
    exit = _check_resp(user_resp)
    if not exit:
        add_user_message(session, chat_id, user_resp)
    return exit


def _get_response_from_assistant(chat_id) -> str:
    assistant_message = mechanicals.generate_chat_completion(session, chat_id)
    add_assistant_message(session, chat_id, assistant_message.content)
    return assistant_message.content


def run_conversation_loop(chat_id):
    exit = False
    while not exit:
        exit = _get_input_from_user(chat_id)
        if not exit:
            pprint(_get_response_from_assistant(chat_id))
            # exit = not cli.ask_user_to_continue()


def start_new_conversation() -> Chat:
    purpose, chat_name = cli.ask_for_new_chat_purpose()
    chat = Chat(name=chat_name, purpose=purpose)
    session.add(chat)
    session.commit()
    session.refresh(chat)

    add_system_message(session, chat.id, f"{prompts.new_chat_with_purpose}: {purpose}")

    return chat
