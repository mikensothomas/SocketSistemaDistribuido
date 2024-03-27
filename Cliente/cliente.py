import socket
import time

def cliente(filename, host, port, protocolo):
    BUFFER_SIZE = 4096
    TIMEOUT = 0.1

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)

        print(f'Cliente {protocolo}://{host}:{port}/{filename}')
        try:
            s.connect((host, port))
            s.sendall(filename.encode())
            
            response = s.recv(4096)
            if response.decode() == 'Erro ao enviar o arquivo':
                print("Erro ao enviar o arquivo para o servidor porque o arquivo já exixte no servidor")
            else:
                with open(filename, 'rb') as f:
                    while True:
                        data = f.read(BUFFER_SIZE)
                        if not data:
                            break
                        s.sendall(data)
        except socket.timeout:
            print("Arquivo enviado com sucesso")

FILENAME = 'arquivo1.html'
HOST = '127.0.0.1'  
PORT = 5000
PROTOCOLO = 'HTTP'
cliente(FILENAME, HOST, PORT, PROTOCOLO)