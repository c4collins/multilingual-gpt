from typing import Dict, List
from data.models.chat_message import ChatMessage

from src.config import openai


# Generate a chat completion response
def generate_chat_completion(session, chat_id: int):
    prompt = build_chat_history(session, chat_id)
    response = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo-0301",
        model="gpt-3.5-turbo",
        # model="gpt-4",
        messages=prompt,
        # max_tokens=100,
        temperature=0.7,
        # n=1,
        # stop=None,
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
