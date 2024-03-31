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

    int servidor, cliente, file_size;
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

    char arquivo[armazena_dados_size];
    ssize_t dado_recebido = recv(cliente, arquivo, sizeof(arquivo), 0);
    if (dado_recebido < 0) {
        printf("Erro ao receber o nome do arquivo\n");
        exit(EXIT_FAILURE);
    } else {
        arquivo[dado_recebido] = '\0';
        FILE *file = fopen(arquivo, "r");
        if (file != NULL) {
            fclose(file);
            printf("Arquivo enviado com sucesso\n");
        } else {
            printf("Erro ao enviar o arquivo para o cliente\n");
        }
    }

    close(cliente);
    close(servidor);

    return 0;
}
