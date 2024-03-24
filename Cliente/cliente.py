import socket
import os

def cliente(filename, host, port):
    BUFFER_SIZE = 4096

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with open(filename, 'rb') as f:
            while True:
                data = f.read(BUFFER_SIZE)
                if not data:
                    break
                else:
                    s.sendall(data)
filename = 'arquivoCliente.exe'
HOST = '127.0.0.1'  
PORT = 5000
cliente(filename, HOST, PORT)