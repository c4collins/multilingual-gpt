from data.models.chat import Chat
from src.utils.cli import ask_user, ask_user_boolean
from src.config.i18n import lang
from . import prompts


def user_wants_to_continue_existing_chat(existing_conversations: int = 0) -> bool:
    print(
        prompts.available_conversations.format(
            existing_conversations=existing_conversations
        )
    )
    return ask_user_boolean(prompts.ask_to_continue_conversation)


def ask_for_new_chat_purpose() -> str:
    # returns purpose and derived websafe title
    resp = ask_user(prompts.ask_for_ai_purpose)
    return resp


def ask_user_for_existing_conversation_id_to_load() -> int:
    try:
        return int(ask_user(f"{prompts.select_old_conversation_or_0}: "))
    except ValueError:
        return 0


def ask_user_for_input() -> str:
    return ask_user(prompts.ask_for_next_goal)


def ask_user_to_continue() -> str:
    return ask_user_boolean(prompts.ask_for_permission_to_continue)


def replay_chat_messages(chat: Chat):
    print(prompts.start_of_chat_message_replay.center(120, "*"))
    for msg in chat.messages:
        role = msg.role.name.value
        content = msg.content
        if content.startswith(f"{lang}: "):
            # still shows language tags that don't match the current language
            content = content[4:]
        content = content.split("\n")
        content = "\n\t".join(content)
        print(f"{role}: {content}")
    print(prompts.end_of_chat_message_replay.center(120, "*"))
