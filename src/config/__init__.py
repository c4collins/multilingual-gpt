import os
from sqlalchemy.exc import IntegrityError
from dotenv import load_dotenv

load_dotenv()

from .auth import openai
from .database import get_session, populate_database
from .i18n import translate as _

session = get_session("sqlite:///data/db.sqlite")

try:
    populate_database(session)
except IntegrityError:
    session.rollback()
    # NOTE: database has been populated
    pass