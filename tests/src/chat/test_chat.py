from src.chat import _check_resp


def test__check_resp():
    assert _check_resp("exit") == True
    assert _check_resp("not exit") != True
    assert _check_resp("anything else") != True
