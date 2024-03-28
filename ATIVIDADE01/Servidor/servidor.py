import socket
import os

def servidor(host, port):
    BUFFER_SIZE = 4096

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f'Servidor {host}/{port}')
        while True:
            conn, addr = s.accept()
            print(f'Conectado com o cliente por {addr}')
            try:
                with conn:
                    nome_arquivo = conn.recv(BUFFER_SIZE).decode()
                    if os.path.exists(nome_arquivo):
                        with open(nome_arquivo, 'rb') as f:
                            data = f.read()
                        conn.sendall(data)
                        print(f'Arquivo "{nome_arquivo}" enviado para o cliente.')
                    else:
                        conn.sendall(b'Erro: Arquivo nao encontrado no servidor ou ele ja existe no cliente.')
                        print('Erro: Arquivo não encontrado no servidor ou ele ja existe no cliente.')
            except Exception as e:
                print(f"Erro ao enviar arquivo: {e}")

HOST = '127.0.0.1'  
PORT = 7777
servidor(HOST, PORT)
