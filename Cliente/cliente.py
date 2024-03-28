import socket
import sys
import os

def cliente(host, port, nome_arquivo):
    BUFFER_SIZE = 4096
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print(f'Conectado ao servidor {host}/{port}')

            if os.path.exists(nome_arquivo):
                print("Arquivo já existe")
            else:
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

if len(sys.argv) != 2:
    print("Erro do URL")
    sys.exit(1)

url = sys.argv[1]
host_port = url.split('/')[2].split(':')

if len(host_port) != 2:
    print("URL inválida.")
    sys.exit(1)

host = host_port[0]
port = int(host_port[1])

nome_arquivo = url.split('/')[-1]

cliente(host, port, nome_arquivo)
