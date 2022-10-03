from objects.request import Request
import os

test_request = "GET /echo HTTP/1.1\r\nHost: example.com\r\nAccept: text/html\r\n\r\n"
test_request_get_params = "GET /echo?test=best&best=test HTTP/1.1\r\nHost: example.com\r\nAccept: text/html\r\n\r\n"

def test_instantiate_from_raw_request():
    request = Request.parse_request(test_request)
    assert request.method == "GET"
    assert request.headers["Host"] == "example.com"

def test_instantiate_from_raw_request_params():
    request = Request.parse_request(test_request_get_params)
    assert request.method == "GET"
    assert request.headers["Host"] == "example.com"
    assert request.query_strings["test"] == "best"
