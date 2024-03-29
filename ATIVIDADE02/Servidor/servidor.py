import socket

# Dicionário com as credenciais dos alunos
credenciais_alunos = {
    "123456": "senha123",
    "654321": "senha456"
}

# Dicionário com as questões e respostas
questoes = {
    "1": {"enunciado": "Qual é a capital do Brasil?",
          "alternativas": ["a) São Paulo", "b) Rio de Janeiro", "c) Brasília", "d) Belo Horizonte"],
          "resposta": "c"},
    "2": {"enunciado": "Quem escreveu 'Dom Casmurro'?",
          "alternativas": ["a) Machado de Assis", "b) Jorge Amado", "c) Graciliano Ramos", "d) Lima Barreto"],
          "resposta": "a"}
}

def main():
    # Configurando o servidor
    host = '127.0.0.1'
    port = 5000

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, port))
    servidor.listen(1)

    print("Servidor aguardando conexão...")

    conn, addr = servidor.accept()
    print("Conexão estabelecida com:", addr)

    # Autenticação do aluno
    matricula, senha = conn.recv(1024).decode().split(',')
    
    if matricula in credenciais_alunos and credenciais_alunos[matricula] == senha:
        conn.send("Autenticado".encode())  # Envio da confirmação de autenticação
        # Enviando questões para o aluno
        try:
            # Enviando questões para o aluno
            for num, questao in questoes.items():
                enunciado = questao["enunciado"]
                print("Enviando enunciado:", enunciado)  # Verificação para debug
                conn.send(enunciado.encode())
                conn.send(str(questao["alternativas"]).encode())
                conn.send("FimQuestao".encode())  # Envio da marcação de fim da questão
                try:
                    resposta = conn.recv(1024).decode().lower().strip()
                except ConnectionResetError:
                    print("Conexão fechada pelo cliente.")
                    break
                if resposta == questao["resposta"]:
                    conn.send("Correta".encode())
                else:
                    conn.send("Incorreta".encode())
        except Exception as e:
            print("Erro:", e)
        finally:
            conn.send("Fim".encode())  # Envio da marcação de fim do envio de todas as questões
        conn.close()

if __name__ == "__main__":
    main()