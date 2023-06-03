from pytest import mark
from src.chat import prompts
from src.chat.mechanicals import build_chat_history, generate_chat_completion
from src.chat.messages import (
    add_assistant_message,
    add_system_message,
    add_user_message,
)
from src.config.enums.chat import ChatUserRole


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


@mark.skip(
    """
1) has a (minimal but never diminshing) cost
2) this test is kinda jank and relies on third-party input
3) you're gonna know pretty quick if this, the core function of this app, doesn't work
    """
)
def test_generate_chat_completion(session, chat_completion_chat_id):
    test_message = "Hello, this was a successful test."

    add_system_message(
        session,
        chat_completion_chat_id,
        f"{prompts.new_chat_with_purpose}: This is a test program; I want you to repeat after the user exactly.",
    )
    add_user_message(session, chat_completion_chat_id, test_message)
    session.commit()
    session.flush()

    history = build_chat_history(session, chat_completion_chat_id)
    assert len(history) == 2

    response_message = generate_chat_completion(session, chat_completion_chat_id)
    assert (
        test_message == response_message["content"][4:]
    )  # the slice is to remove the language marker (e.g. `en: `) from the start of the content response
