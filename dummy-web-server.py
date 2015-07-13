#!/usr/bin/env python
"""
Very simple HTTP server in python.

Usage::
    ./dummy-web-server.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost

I tested by Python 3.4.3 on Windows 8.1.
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
"""
# https://docs.python.org/2/library/basehttpserver.html
# Note The BaseHTTPServer module has been merged into http.server in Python 3. 
from http.server import BaseHTTPRequestHandler, HTTPServer
# https://docs.python.org/2/library/socketserver.html
# Note The SocketServer module has been renamed to socketserver in Python 3.
import socketserver
 
class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
 
    def do_GET(self):
        self._set_headers()
        # https://stackoverflow.com/questions/23264569/python-3-x-basehttpserver-or-http-server
        self.wfile.write(b"<html><body><h1>hi!</h1></body></html>")
        self.log_rawRequestHeader()
 
    def do_HEAD(self):
        self._set_headers()
        self.log_rawRequestHeader()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write(b"<html><body><h1>POST!</h1></body></html>")
        self.log_rawRequestHeader()
        self.log_rawRequestBody()
 
    def log_rawRequestHeader(self):
        # https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler
        print(self.command, self.path, self.request_version)
        print(self.headers.as_string())
 
    def log_rawRequestBody(self):
        # https://docs.python.org/3/library/email.message.html#email.message.Message
        # https://github.com/Chanmoro/python/blob/master/WebServerSample/dummy_webapi.py
        # TODO: Error Handling
        print(self.rfile.read(int(self.headers.get('Content-Length'))).decode('utf-8'))
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()
 
if __name__ == "__main__":
    from sys import argv
 
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
