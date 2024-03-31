#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <fcntl.h>
#include <errno.h>

#define BUFFER_SIZE 4096

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Use: <./servidor 5000 /Downloads/SocketSistemaDistribuido/ATIVIDADE01/Servidor> para roda o servidor\n");
        return EXIT_FAILURE;
    }

    int PORT = atoi(argv[1]);
    const char *arquivo = argv[2];

    int servidor, cliente;
    struct sockaddr_in endereco;
    int tamanho_endereco = sizeof(endereco);
    char buffer[BUFFER_SIZE] = {0};

    if ((servidor = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("Erro ao criar o socket");
        exit(EXIT_FAILURE);
    }

    endereco.sin_family = AF_INET;
    endereco.sin_addr.s_addr = INADDR_ANY;
    endereco.sin_port = htons(PORT);

    if (bind(servidor, (struct sockaddr *)&endereco, sizeof(endereco)) < 0) {
        perror("Erro ao realizar o bind");
        exit(EXIT_FAILURE);
    }

    if (listen(servidor, 3) < 0) {
        perror("Erro ao escutar por conexões");
        exit(EXIT_FAILURE);
    }

    printf("Aguardando conexões...\n");

    if ((cliente = accept(servidor, (struct sockaddr *)&endereco, (socklen_t*)&tamanho_endereco)) < 0) {
        perror("Erro ao aceitar a conexão");
        exit(EXIT_FAILURE);
    }

    printf("Conexão estabelecida com sucesso.\n");

    ssize_t bytes_received = recv(cliente, buffer, BUFFER_SIZE, 0);
    if (bytes_received < 0) {
        perror("Erro ao receber o nome do arquivo");
        exit(EXIT_FAILURE);
    }

    buffer[bytes_received] = '\0';

    int file = open(buffer, O_RDONLY);


    send(cliente, "Arquivo OK", strlen("Arquivo OK"), 0);

    ssize_t bytes_sent, bytes_read;
    while ((bytes_read = read(file, buffer, BUFFER_SIZE)) > 0) {
        bytes_sent = send(cliente, buffer, bytes_read, 0);
        if (bytes_sent < 0) {
            perror("Erro ao enviar o arquivo");
            exit(EXIT_FAILURE);
        }
    }

    close(cliente);
    close(servidor);
    close(file);

    return 0;
}
