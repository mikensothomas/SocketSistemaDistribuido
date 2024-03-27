import socket
import sys

def cliente(host, port, nome_arquivo):
    BUFFER_SIZE = 4096

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print(f'Conectado ao servidor {host}/{port}')

            s.sendall(nome_arquivo.encode())

            data = b''
            while True:
                chunk = s.recv(BUFFER_SIZE)
                if not chunk:
                    break
                data += chunk
            
            if data.startswith(b'Erro'):
                print(data.decode())
            else:
                with open(nome_arquivo, 'wb') as f:
                    f.write(data)
                print(f'Arquivo "{nome_arquivo}" recebido com sucesso.')
        except Exception as e:
            print(f"Erro ao conectar ao servidor: {e}")

HOST = '127.0.0.1'  
PORT = 5000

if len(sys.argv) != 2:
    print("Uso: python3 cliente.py <nome_arquivo>")
    sys.exit(1)

nome_arquivo = sys.argv[1]

cliente(HOST, PORT, nome_arquivo)
