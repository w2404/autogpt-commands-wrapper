from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
from . import config
import json
from . import lib

def readnum(sock):
    s=b''
    ss=sock.read(1)
    while not ss==b' ':
        s+=ss
        ss=sock.read(1)
    return int(s)

class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        size=readnum(self.rfile)
        s= self.rfile.read(size)
        o=json.loads(s) 
        print(o)
        o=lib.main(o)
        s=json.dumps(o).encode()
        self.wfile.write(f'{len(s)} '.encode())
        self.wfile.write(s)
print("localhost", config.port)
with socketserver.TCPServer(("localhost", config.port), MyTCPHandler) as server:
    server.serve_forever()
