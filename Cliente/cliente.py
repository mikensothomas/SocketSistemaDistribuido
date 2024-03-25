import socket

def cliente(filename, host, port, protocolo):
    BUFFER_SIZE = 4096

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        print(f'Cliente {protocolo}://{host}:{port}/{filename}')
        s.connect((host, port))
        with open(filename, 'rb') as f:
            while True:
                data = f.read(BUFFER_SIZE)
                if not data:
                    break
                s.sendall(data)
                print("Arquivo enviado com sucesso")

FILENAME = 'arquivo1.html'
HOST = '127.0.0.1'  
PORT = 5000
PROTOCOLO = 'HTTP'
cliente(FILENAME, HOST, PORT, PROTOCOLO)
