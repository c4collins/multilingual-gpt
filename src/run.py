from src.chat import run_conversation_loop, start_new_conversation
from src.chat.database import check_for_existing_conversations
from src.utils.cli import ask_user


if __name__ == "__main__":
    loaded_conversation = check_for_existing_conversations()
    if loaded_conversation:
        print(loaded_conversation)
        conversation = loaded_conversation
    else:
        conversation = start_new_conversation()

    run_conversation_loop(conversation.id)
