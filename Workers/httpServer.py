import os
from threading import Thread, Event
from multiprocessing import Pipe
from http.server import HTTPServer, BaseHTTPRequestHandler
from functools import partial


def get_info(pipe1, pipe2, event):
    info = "No new data"
    while True:
        if pipe1.poll(0.2):
            info = pipe1.recv()
        if event.is_set():
            pipe2.send(info)
            event.clear()


def main(external_pipe):
    event = Event()
    thread_pipe, server_pipe = Pipe()
    current_directory = os.getcwd()
    t = Thread(target=get_info, args=(external_pipe, thread_pipe, event))
    t.start()
    handler = partial(RequestHandler, server_pipe, event, current_directory)
    httpd = HTTPServer(("localhost", 8080), handler)
    httpd.serve_forever()


class RequestHandler(BaseHTTPRequestHandler):
    def __init__(self, pipe, event, dir, *args, **kwargs):
        self.pipe = pipe
        self.event = event
        self.dir = dir
        super().__init__(*args, **kwargs)

    def do_GET(self):
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
            self.event.set()
            self.wfile.write(bytes(self.pipe.recv(), "utf-8"))

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
