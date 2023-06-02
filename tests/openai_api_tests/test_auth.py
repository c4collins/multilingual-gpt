from src.config import openai


def test_auth():
    assert len(openai.Model.list()) > 0
