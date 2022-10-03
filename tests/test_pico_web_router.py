from picowebrouter import WebRouter
from unittest.mock import patch

with patch('picowebrouter.walk_directories'):
    with patch('picowebrouter.socket'):
        app = webrouter = WebRouter("192.168.4.1", 80, "/test")

@webrouter.route("/best")
def test_route():
    return "test"


@patch('picowebrouter.walk_directories')
@patch("picowebrouter.socket")
def test_instantiate_webrouter(mock_socket, mock_walk):
    mock_walk.side_effect = [{"test": ["file.txt"]}]
    webrouter = WebRouter("192.168.4.1", 80, "/test")
    assert webrouter.static_files == ["test/file.txt"]

@patch('picowebrouter.walk_directories')
@patch("picowebrouter.socket")
def test_adding_route(mock_socket, mock_walk):
    assert "/best" in app.routes.keys()

@patch('picowebrouter.walk_directories')
@patch("picowebrouter.socket")
def test_serve(mock_socket, mock_walk):
    mock_walk.side_effect = [{"test": ["file.txt"]}]
    mock_socket["test", "test"]
    webrouter = WebRouter("192.168.4.1", 80, "/test")
    assert webrouter.static_files == ["test/file.txt"]

def test_mimetype():
    mimetype = app.determine_mimetype("/test.js")
    assert mimetype == "text/javascript"
    