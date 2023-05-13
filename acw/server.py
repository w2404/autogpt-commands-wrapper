from http.server import BaseHTTPRequestHandler, HTTPServer
from . import config
import json
from . import lib

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_POST(self):
        length = int(self.headers.get('Content-Length'))
        o=json.loads(self.rfile.read(length))
        print(o)
        o=lib.main(o)
        #print(o)
        self._set_headers()
        self.wfile.write(json.dumps(o).encode())

print('start server')
httpd = HTTPServer(('',config.port ), Server)
httpd.serve_forever()
