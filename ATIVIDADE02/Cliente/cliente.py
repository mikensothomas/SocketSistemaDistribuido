import socket

host = '127.0.0.1'
porta = 8080

def cliente(host, porta):

    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.settimeout(0.1)

    endereco = (host, porta)
    
    socket_cliente.connect(endereco)

    print("Conectado com o servidor")
    print("")

    mensagem1 = input("Digite sua matricula: ")
    socket_cliente.send(mensagem1.encode())
    mensagem2 = input("Digite sua senha: ")
    socket_cliente.send(mensagem2.encode())
    print("")
    
    try:
        dado00 = socket_cliente.recv(1024).decode()
        print(dado00)

        dado11 = socket_cliente.recv(1024).decode()
        print(dado11)
        dado22 = socket_cliente.recv(1024).decode()
        print(dado22)
        dado33 = socket_cliente.recv(1024).decode()
        print(dado33)
        dado44 = socket_cliente.recv(1024).decode()
        print(dado44)
        dado55 = socket_cliente.recv(1024).decode()
        print(dado55)
    except socket.timeout:
        mensagem3 = input("Resposta1: ")
        socket_cliente.send(mensagem3.encode())

    try:
        print("")
        dado66 = socket_cliente.recv(1024).decode()
        print(dado66)
        dado77 = socket_cliente.recv(1024).decode()
        print(dado77)
        dado88 = socket_cliente.recv(1024).decode()
        print(dado88)
        dado99 = socket_cliente.recv(1024).decode()
        print(dado99)
        dado10 = socket_cliente.recv(1024).decode()
        print(dado10)
    except socket.timeout:
        mensagem4 = input("Resposta2: ")
        socket_cliente.send(mensagem4.encode())

    try:
        print("")
        dado3a = socket_cliente.recv(1024).decode()
        print(dado3a)
        dado3b = socket_cliente.recv(1024).decode()
        print(dado3b)
        dado3c = socket_cliente.recv(1024).decode()
        print(dado3c)
        dado3d = socket_cliente.recv(1024).decode()
        print(dado3d)
        dado3e = socket_cliente.recv(1024).decode()
        print(dado3e)
    except socket.timeout:
        mensagem5 = input("Resposta3: ")
        socket_cliente.send(mensagem5.encode())

    try:
        print("")
        dado4a = socket_cliente.recv(1024).decode()
        print(dado4a)
        dado4b = socket_cliente.recv(1024).decode()
        print(dado4b)
        dado4c = socket_cliente.recv(1024).decode()
        print(dado4c)
        dado4d = socket_cliente.recv(1024).decode()
        print(dado4d)
        dado4e = socket_cliente.recv(1024).decode()
        print(dado4e)
    except socket.timeout:
        mensagem6 = input("Resposta4: ")
        socket_cliente.send(mensagem6.encode())

    try:
        print("")
        dado4aa = socket_cliente.recv(1024).decode()
        print(dado4aa)
        dado4bb = socket_cliente.recv(1024).decode()
        print(dado4bb)
        dado4cc = socket_cliente.recv(1024).decode()
        print(dado4cc)
        dado4dd = socket_cliente.recv(1024).decode()
        print(dado4dd)
        dado4ee = socket_cliente.recv(1024).decode()
        print(dado4ee)
    except socket.timeout:
        mensagem7 = input("Resposta5: ")
        socket_cliente.send(mensagem7.encode())
        print("")
        resultado = socket_cliente.recv(1024).decode()
        print(resultado)

cliente(host, porta)