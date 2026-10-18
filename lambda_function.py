
import base64
from urllib.parse import unquote

from app import app


def lambda_handler(event, context):
    """Adapt a Lambda Function URL request to Flask."""

    request_context = event.get("requestContext", {})
    http = request_context.get("http", {})

    method = http.get("method", "GET")
    path = unquote(event.get("rawPath", "/"))
    query_string = event.get("rawQueryString", "")
    headers = {
        key.lower(): value
        for key, value in event.get("headers", {}).items()
    }

    host = headers.get("host", "localhost")
    body = event.get("body") or ""

    if event.get("isBase64Encoded"):
        body = base64.b64decode(body)
    else:
        body = body.encode("utf-8")

    environ = {
        "REQUEST_METHOD": method,
        "SCRIPT_NAME": "",
        "PATH_INFO": path,
        "QUERY_STRING": query_string,
        "SERVER_NAME": host.split(":")[0],
        "SERVER_PORT": "443",
        "SERVER_PROTOCOL": "HTTP/1.1",
        "HTTP_HOST": host,
        "wsgi.version": (1, 0),
        "wsgi.url_scheme": "https",
        "wsgi.input": __import__("io").BytesIO(body),
        "wsgi.errors": __import__("sys").stderr,
        "wsgi.multithread": False,
        "wsgi.multiprocess": False,
        "wsgi.run_once": True,
        "CONTENT_LENGTH": str(len(body)),
    }

    for key, value in headers.items():
        if key == "content-type":
            environ["CONTENT_TYPE"] = value
        elif key == "content-length":
            environ["CONTENT_LENGTH"] = value
        elif key not in ("host",):
            environ["HTTP_" + key.upper().replace("-", "_")] = value

    response_data = {}

    def start_response(status, response_headers, exc_info=None):
        response_data["statusCode"] = int(status.split()[0])
        response_data["headers"] = dict(response_headers)

    response_body = b"".join(
        chunk if isinstance(chunk, bytes) else chunk.encode("utf-8")
        for chunk in app(environ, start_response)
    )

    response_data["body"] = response_body.decode("utf-8")
    response_data["isBase64Encoded"] = False

    return response_data
