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
        fprintf(stderr, "Uso: %s <porta> <diretório_do_servidor>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    int port = atoi(argv[1]); // Porta que o servidor usará
    const char *file_directory = argv[2]; // Diretório onde os arquivos do servidor estão localizados

    int server_fd, new_socket, valread;
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
    address.sin_port = htons(port);

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

    // Receber o nome do arquivo do cliente
    valread = read(new_socket, buffer, BUFFER_SIZE);
    if (valread < 0) {
        perror("Erro ao receber o nome do arquivo");
        exit(EXIT_FAILURE);
    }
    buffer[valread] = '\0';

    printf("Solicitação recebida: %s\n", buffer);

    // Verificar se o arquivo solicitado existe
    char file_path[BUFFER_SIZE + strlen(file_directory) + 1];
    snprintf(file_path, sizeof(file_path), "%s%s", file_directory, buffer);

    int file = open(file_path, O_RDONLY);
    if (file < 0) {
        perror("Arquivo não exixte");
        send(new_socket, "Erro: Arquivo não encontrado", strlen("Erro: Arquivo não encontrado"), 0);
        close(new_socket);
        close(server_fd);
        exit(EXIT_FAILURE);
    }

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
