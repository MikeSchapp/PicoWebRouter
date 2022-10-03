from picowebrouter.utils import unquote
class Request:
    def __init__(self,
        raw=None,
        method=None,
        path=None,
        query_strings=None,
        protocol=None,
        headers=None,
        body=None
    ):
        self.raw = raw
        self.method = method
        self.path = path
        self.query_strings = query_strings
        self.protocol = protocol
        self.headers = headers
        self.body = body

    
    @classmethod
    def parse_request(cls, request):
        body = None
        try:
            request, body = request.split("\r\n\r\n")
        except ValueError:
            request = request
        split_request = request.split("\r\n")
        request_line = split_request.pop(0)
        method, path, protocol = request_line.split(" ")
        query_strings = {}
        if "?" in path:
            path, raw_query = path.split("?")
            raw_query = raw_query.split("&")
            for query in raw_query:
                key, value = query.split("=")
                query_strings[key] = unquote(value).decode("utf-8")
            query_strings = query_strings

        headers = {}
        for header in split_request:
            key, value = header.split(": ")
            headers[key] = value
        headers = headers
        return cls(
            request,
            method,
            path,
            query_strings,
            protocol,
            headers,
            body
        )
