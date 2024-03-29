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
        fprintf(stderr, "Uso: %s <porta> <caminho_do_arquivo>\n", argv[0]);
        return EXIT_FAILURE;
    }

    int PORT = atoi(argv[1]);
    const char *file_path = argv[2];

    int server_fd, new_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};

    // Criar um socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("Erro ao criar o socket");
        exit(EXIT_FAILURE);
    }

    // Configurar a estrutura do endereço
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // Vincular o socket a um endereço e porta
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("Erro ao realizar o bind");
        exit(EXIT_FAILURE);
    }

    // Escutar por conexões
    if (listen(server_fd, 3) < 0) {
        perror("Erro ao escutar por conexões");
        exit(EXIT_FAILURE);
    }

    printf("Aguardando conexões...\n");

    // Aceitar a conexão entrante
    if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0) {
        perror("Erro ao aceitar a conexão");
        exit(EXIT_FAILURE);
    }

    printf("Conexão estabelecida com sucesso.\n");

    ssize_t bytes_received = recv(new_socket, buffer, BUFFER_SIZE, 0);
    if (bytes_received < 0) {
        perror("Erro ao receber o nome do arquivo");
        exit(EXIT_FAILURE);
    }

    buffer[bytes_received] = '\0'; // Terminar a string recebida

    int file = open(buffer, O_RDONLY);


    // Enviar confirmação ao cliente
    send(new_socket, "Arquivo OK", strlen("Arquivo OK"), 0);

    // Enviar o conteúdo do arquivo para o cliente
    ssize_t bytes_sent, bytes_read;
    while ((bytes_read = read(file, buffer, BUFFER_SIZE)) > 0) {
        bytes_sent = send(new_socket, buffer, bytes_read, 0);
        if (bytes_sent < 0) {
            perror("Erro ao enviar o arquivo");
            exit(EXIT_FAILURE);
        }
    }

    // Fechar o socket e arquivo
    close(new_socket);
    close(server_fd);
    close(file);

    return 0;
}
