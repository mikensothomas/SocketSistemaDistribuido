import socket
import os

def servidor(file, host, port, caminho):
    BUFFER_SIZE = 4096

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f'Servidor {host}/{port}/{caminho}')
        conn, addr = s.accept()
        with conn:
            print(f'Conectado com o cliente por {addr}')
            if os.path.exists(file):
                print("Erro: Este arquivo já exixte.")
            else:
                with open(file, 'wb') as f:
                    while True:
                        data = conn.recv(BUFFER_SIZE)
                        if not data:
                            break
                        f.write(data)
                print('Arquivo recebido com sucesso!')

SAVEFILE = 'arquivo1.html'
HOST = '127.0.0.1'  
PORT = 5000
CAMINHO = 'Área de trabalho/SocketSistemaDistribuido/Servidor'
servidor(SAVEFILE, HOST, PORT, CAMINHO)