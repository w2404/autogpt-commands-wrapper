
import socket
import sys
import json
import config

def readnum(sock):
    s=b''
    ss=sock.recv(1)
    while not ss==b' ':
        s+=ss
        ss=sock.recv(1)
    return int(s)

HOST, PORT = "localhost", config.port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    o={'query':'invention of the chariot and its evolution into the war chariot','num_results':8}
    s=json.dumps(o)
    print(len(s))
    s=f'{len(s)} {s}'.encode()
    sock.sendall(s)
    size=readnum(sock)
    print('size',size)
    received = sock.recv(size).decode()
    o=json.loads(received )
    print(o)
