from http.server import HTTPServer, BaseHTTPRequestHandler
from functools import partial
import os


def main(pipe):
    current_directory = os.getcwd()
    handler = partial(RequestHandler, pipe, current_directory)
    httpd = HTTPServer(("localhost", 8080), handler)
    httpd.serve_forever()


class RequestHandler(BaseHTTPRequestHandler):
    def __init__(self, pipe, dir, *args, **kwargs):
        self.pipe = pipe
        self.dir = dir
        super().__init__(*args, **kwargs)

    def do_GET(self):
        print(self.pipe.poll())
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                bytes(
                    open(self.dir + "/Workers/Server/index.html").read(),
                    "utf-8",
                )
            )
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            if self.pipe.poll():
                self.wfile.write(bytes(self.pipe.recv(), "utf-8"))
            else:
                self.wfile.write(bytes("No new data", "utf-8"))
        elif self.path == "/ajax.js":
            self.send_response(200)
            self.send_header("Content-type", "text/javascript")
            self.end_headers()
            self.wfile.write(
                bytes(
                    open(self.dir + "/Workers/Server/ajax.js").read(), "utf-8"
                )
            )
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes("File not found", "utf-8"))
