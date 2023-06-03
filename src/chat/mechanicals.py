from typing import Dict, List
from data.models.chat_message import ChatMessage

from src.config import openai, openai_chat_model


# Generate a chat completion response
def generate_chat_completion(session, chat_id: int):
    prompt = build_chat_history(session, chat_id)
    response = openai.ChatCompletion.create(
        model=openai_chat_model,
        messages=prompt,
    )
    return response.choices[0].message


# Build the prompt from the conversation history
def build_chat_history(session, chat_id: int) -> List[Dict[str, str]]:
    conversation = reversed(
        session.query(ChatMessage)
        .filter_by(chat_id=chat_id)
        .order_by(ChatMessage.id.desc())
        .limit(100)
        .all()
    )
    return [message.as_conversation() for message in conversation]
