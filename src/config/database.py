from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data.models import Base

# NOTE: Even if unused these need to be imported here (in this order?)
# This is where the application learns of them and if they aren't here.
# They will be imported in an uncontrolled manner if they are not here.
from data.models.chat_message import ChatMessage
from data.models.chat import Chat
from data.models.chat_role import ChatRole
from src.config.enums.chat import ChatUserRole


def get_session(connection="sqlite://", **kwargs):
    # possible kwargs:
    #   - echo=True
    engine = create_engine(connection, **kwargs)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    return session


def populate_database(session):
    session.add_all(
        [
            ChatRole(id=1, name=ChatUserRole.SYSTEM),
            ChatRole(id=3, name=ChatUserRole.USER),
            ChatRole(id=2, name=ChatUserRole.ASSISTANT),
        ]
    )
    session.commit()
    session.flush()
