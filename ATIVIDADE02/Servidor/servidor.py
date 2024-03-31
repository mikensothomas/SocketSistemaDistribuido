import socket

host = '127.0.0.1'
porta = 8080

def servidor(host, porta):

    servidor_secket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    servidor_secket.bind((host, porta))

    servidor_secket.listen()

    print(f"Servidor está conectado no: {host}:{porta}")
    print("Está esperando a conexão do cliente...")

    

    while True:
        matricula = '123456'
        senha = 'senha123'
        questao_certa = 0
        qtd_questao = 5
        nota_total = 0

        socket_cli, endereco_cli = servidor_secket.accept()
        print("Conectado com um aluno")
        print("")

        dado_matri = socket_cli.recv(1024).decode()
        print(f"Matrícula do aluno: {dado_matri}")
        dado_senha = socket_cli.recv(1024).decode()
        print(f"Senha do aluno: {dado_senha}")

        print("")
        if(dado_matri == matricula and dado_senha == senha):
            mensagem0 = "Escolhe uma letra em cada questão:\n"
            socket_cli.send(mensagem0.encode())

            mensagem1 = "Capital do Brasil?\n"
            a1 = "a) Santa Catarina\n"
            b2 = "b) Rio de janeiro\n"
            c3 = "c) Brasilia\n"
            d4 = "d) Maranho\n"

            socket_cli.send(mensagem1.encode())
            socket_cli.send(a1.encode())
            socket_cli.send(b2.encode())
            socket_cli.send(c3.encode())
            socket_cli.send(d4.encode())
            dado1 = socket_cli.recv(1024).decode()
            print(f"Resposta da primeira questão: {dado1}")

            if(dado1 == 'c'):
                questao_certa = questao_certa + 1
                nota_total = nota_total + 2

            print("")
            mensagem3 = "2 + 3:\n"
            a11 = "a) 4\n"
            b22 = "b) 5\n"
            c33 = "c) 7\n"
            d44 = "d) 21\n"

            socket_cli.sendall(mensagem3.encode())
            socket_cli.send(a11.encode())
            socket_cli.send(b22.encode())
            socket_cli.send(c33.encode())
            socket_cli.send(d44.encode())
            dado2 = socket_cli.recv(1024).decode()
            print(f"Resposta da segunda questão: {dado2}")

            if(dado2 == 'b'):
                questao_certa = questao_certa + 1
                nota_total = nota_total + 2

            print("")
            mensagem4 = "10 / 2:\n"
            a111 = "a) 5\n"
            b222 = "b) 7\n"
            c333 = "c) 32\n"
            d444 = "d) 90\n"

            socket_cli.send(mensagem4.encode())
            socket_cli.send(a111.encode())
            socket_cli.send(b222.encode())
            socket_cli.send(c333.encode())
            socket_cli.send(d444.encode())
            dado3 = socket_cli.recv(1024).decode()
            print(f"Resposta da terceira questão: {dado3}")

            if(dado3 == 'a'):
                questao_certa = questao_certa + 1
                nota_total = nota_total + 2

            print("")
            mensagem5 = "9 * 9:\n"
            a1111 = "a) 5\n"
            b1111 = "b) 23\n"
            c1111 = "c) 98\n"
            d1111 = "d) 81\n"

            socket_cli.send(mensagem5.encode())
            socket_cli.send(a1111.encode())
            socket_cli.send(b1111.encode())
            socket_cli.send(c1111.encode())
            socket_cli.send(d1111.encode())
            dado4 = socket_cli.recv(1024).decode()
            print(f"Resposta da quarta questão: {dado4}")

            if(dado4 == 'd'):
                questao_certa = questao_certa + 1
                nota_total = nota_total + 2

            print("")
            mensagem6 = "7 * 7:\n"
            a1111a = "a) 5\n"
            b1111b = "b) 23\n"
            c1111c = "c) 49\n"
            d1111d = "d) 81\n"

            socket_cli.send(mensagem6.encode())
            socket_cli.send(a1111a.encode())
            socket_cli.send(b1111b.encode())
            socket_cli.send(c1111c.encode())
            socket_cli.send(d1111d.encode())
            dado5 = socket_cli.recv(1024).decode()
            print(f"Resposta da quarta questão: {dado5}")

            if(dado5 == 'c'):
                questao_certa = questao_certa + 1
                nota_total = nota_total + 2

            nota = (f"Você respondeu {qtd_questao} questões \nAcertou {questao_certa} questões \nTirou {nota_total} pontos")
            socket_cli.send(nota.encode())

            if(nota):
                break
        else:
            print("Senha ou matŕcula inválido")
            break

servidor(host, porta)