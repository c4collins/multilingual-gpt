from pytest import fixture
from src.config.database import get_session, populate_database


@fixture(scope="session", autouse=True)
def session():
    session = get_session()
    populate_database(session)
    try:
        yield session
    except:
        session.rollback()
    finally:
        session.close()
