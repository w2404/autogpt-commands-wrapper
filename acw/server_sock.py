import socketserver
import json

def readnum(sock):
    s=b''
    ss=sock.read(1)
    while not ss==b' ':
        s+=ss
        ss=sock.read(1)
    return int(s)

def run(func,port):
    class MyTCPHandler(socketserver.StreamRequestHandler):
        def handle(self):
            size=readnum(self.rfile)
            s= self.rfile.read(size)
            print(s[:40])
            o=json.loads(s) 
            s=func(o)
            if s is None:s=''
            print(s[:40])
            s=s.encode()
            self.wfile.write(f'{len(s)} '.encode())
            self.wfile.write(s)
    print("localhost", port)
    with socketserver.TCPServer(("localhost", port), MyTCPHandler) as server:
        server.serve_forever()
