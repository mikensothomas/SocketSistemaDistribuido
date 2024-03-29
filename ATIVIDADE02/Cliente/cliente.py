import socket

def main():
    # Configurando o cliente
    host = '127.0.0.1'
    port = 5000

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, port))

    # Autenticando o aluno
    matricula = input("Informe sua matrícula: ")
    senha = input("Informe sua senha: ")
    credenciais = matricula + ',' + senha  # Concatena matrícula e senha separados por vírgula
    cliente.send(credenciais.encode())

    resposta_servidor = cliente.recv(1024).decode()
    
    if resposta_servidor == "Autenticado":
        print("Autenticado com sucesso!")
        # Recebendo e respondendo as questões
        while True:
            enunciado = cliente.recv(1024).decode()
            if enunciado == "Fim":
                break
            alternativas = (cliente.recv(1024).decode())
            #print("OP")
            print(enunciado)
            print("Escolha uma das alternativas:", alternativas)
            resposta = input().lower().strip()
            cliente.send(resposta.encode())
            resposta_servidor = cliente.recv(1024).decode()
            print("Sua resposta foi:", resposta_servidor)
    else:
        print("Credenciais inválidas")
    cliente.close()

if __name__ == "__main__":
    main()