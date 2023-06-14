import os
from sqlalchemy.exc import IntegrityError
from dotenv import load_dotenv

load_dotenv()

from .auth import openai
from .database import get_session, populate_database
from .i18n import lang, translate as _

session = get_session("sqlite:///data/db.sqlite")

try:
    populate_database(session)
except IntegrityError:
    session.rollback()
    # NOTE: database has been populated
    pass

openai_chat_model = "gpt-3.5-turbo-0613"
