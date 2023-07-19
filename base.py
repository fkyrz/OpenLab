from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote
import os

ADDRESS = "127.0.0.2"
PORT = 8080

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            filepath = unquote(self.path[1:])  # remove the leading '/'
            if filepath == "":
                filepath = "index.html"  # default to index.html if no file is specified
            if os.path.isfile(filepath):
                self.send_response(200)
                if filepath.endswith(".html"):
                    self.send_header('Content-type', 'text/html')
                elif filepath.endswith(".js"):
                    self.send_header('Content-type', 'text/javascript')
                elif filepath.endswith(".css"):
                    self.send_header('Content-type', 'text/css')
                # Add more content types as needed
                else:
                    self.send_header('Content-type', 'text/plain')
                self.end_headers()
                with open(filepath, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'404 Not Found')
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(e).encode('utf8'))

httpd = ThreadingHTTPServer((ADDRESS, PORT), MyHandler)
httpd.serve_forever()
