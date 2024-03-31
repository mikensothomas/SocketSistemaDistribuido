#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <fcntl.h>
#include <errno.h>

#define armazena_dados_size 4096

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
    char armazena_dados[armazena_dados_size] = {0};

    if ((servidor = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        printf("Erro ao criar o socket\n");
        exit(EXIT_FAILURE);
    } else {
        endereco.sin_family = AF_INET;
        endereco.sin_addr.s_addr = INADDR_ANY;
        endereco.sin_port = htons(PORT);
    }

    if (bind(servidor, (struct sockaddr *)&endereco, sizeof(endereco)) < 0) {
        printf("Erro ao configurar o socket\n");
        exit(EXIT_FAILURE);
    }

    if (listen(servidor, 3) < 0) {
        printf("Erro ao escutar por conexões\n");
        exit(EXIT_FAILURE);
    } else {
        printf("Aguardando conexões...\n");
    }

    if ((cliente = accept(servidor, (struct sockaddr *)&endereco, (socklen_t*)&tamanho_endereco)) < 0) {
        printf("Erro ao aceitar a conexão\n");
        exit(EXIT_FAILURE);
    } else{
        printf("Conexão estabelecida com sucesso.\n");
    }

    ssize_t dado_recebido = recv(cliente, armazena_dados, armazena_dados_size, 0);
    if (dado_recebido < 0) {
        printf("Erro ao receber o nome do arquivo\n");
        exit(EXIT_FAILURE);
    } else {
        if (open(arquivo, 'r')) {
            armazena_dados[dado_recebido] = '\0';
            printf("Arquivo enviado com sucesso\n");
        } else {
            printf("Erro ao enviar o arquivo");
        }
    }

    int file = open(armazena_dados, O_RDONLY);
    send(cliente, "Arquivo OK", strlen("Arquivo OK"), 0);

    ssize_t bytes_sent, bytes_read;
    while ((bytes_read = read(file, armazena_dados, armazena_dados_size)) > 0) {
        bytes_sent = send(cliente, armazena_dados, bytes_read, 0);
        if (bytes_sent < 0) {
            printf("Erro ao enviar o arquivo\n");
            exit(EXIT_FAILURE);
        }
    }

    close(cliente);
    close(servidor);
    close(file);

    return 0;
}
