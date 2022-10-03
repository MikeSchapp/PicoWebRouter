from utils import unquote

def test_unquote():
    test = unquote("%21best%2ayes")
    assert test == b'!best*yes'

def test_unquote_key_error():
    test = unquote("%21best%2ayes")
    assert test == b'!best*yes'