import socket
import os

def servidor(file_name, host, port):
    BUFFER_SIZE = 4096

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f'O servidor está esperando a conexão do cliente no endreço IP: {host}: e na porta: {port}')
        conn, addr = s.accept()
        with conn:
            print(f'Conectado por {addr}')
            if os.path.exists(file_name):
                print("Erro: Este arquivo já exixte.")
            else:
                with open(file_name, 'wb') as f:
                    while True:
                        data = conn.recv(BUFFER_SIZE)
                        if not data:
                            break
                        f.write(data)
                print('File received successfully!')

saved_file_name = 'arquivoCliente.exe'
HOST = '127.0.0.1'  
PORT = 5000
servidor(saved_file_name, HOST, PORT)