import socket
import sys
import os

def cliente(url):
    parts = url.split('/')
    if len(parts) != 4 or parts[0] != 'http:' or ':' not in parts[2]:
        print("URL inválida.")
        sys.exit(1)
    
    host = parts[2].split(':')[0]
    port = int(parts[2].split(':')[1])
    nome_arquivo = parts[3]

    BUFFER_SIZE = 4096
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print(f'Conectado ao servidor {host}/{port}')

            if(os.path.exists(nome_arquivo)):
                print("Arquivo já exixte no diretório do cliente")
            else:
                s.sendall(nome_arquivo.encode())

                confirmacao = s.recv(BUFFER_SIZE).decode()
                if confirmacao.startswith('Erro'):
                    print(confirmacao)
                else:
                    with open(nome_arquivo, 'wb') as f:
                        while True:
                            chunk = s.recv(BUFFER_SIZE)
                            if not chunk:
                                break
                            f.write(chunk)
                        print(f'Arquivo "{nome_arquivo}" recebido com sucesso.')

        except Exception as e:
            print(f"Erro ao conectar com servidor: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("URL inválido")
        sys.exit(1)
    
    url = sys.argv[1]
    cliente(url)
