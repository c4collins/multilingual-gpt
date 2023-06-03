from pprint import pprint
from data.models.chat import Chat
from src.chat import run_conversation_loop, start_new_conversation
from src.chat.cli import replay_chat_messages
from src.chat.database import check_for_existing_conversations
from src.config import session


if __name__ == "__main__":
    loaded_chat: Chat = check_for_existing_conversations()
    if loaded_chat:
        print(loaded_chat)
        conversation = loaded_chat
        replay_chat_messages(conversation)
    else:
        conversation = start_new_conversation()

    run_conversation_loop(conversation.id)
