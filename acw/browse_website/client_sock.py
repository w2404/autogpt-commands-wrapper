
import socket
import sys
import json

def readnum(sock):
    s=b''
    ss=sock.recv(1)
    while not ss==b' ':
        s+=ss
        ss=sock.recv(1)
    return int(s)

HOST, PORT = "localhost", 12723
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    s=json.dumps({'command':'page_source'}) #get','url':'http://baidu.com'})
    print(len(s))
    s=f'{len(s)} {s}'.encode()
    sock.sendall(s)
    size=readnum(sock)
    print('size',size)
    received = sock.recv(size).decode()
    print(received)
