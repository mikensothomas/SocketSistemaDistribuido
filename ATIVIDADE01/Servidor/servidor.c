#include<stdio.h>
#include<string.h>
#include<sys/socket.h>
#include<arpa/inet.h>
#include<unistd.h>

int main(int argc , char *argv[])
{
	int socket_desc , client_sock , c , read_size;
	struct sockaddr_in server , client;
	char client_message[2000];
	
	socket_desc = socket(AF_INET , SOCK_STREAM , 0);
	if (socket_desc == -1)
	{
		printf("O socket não pode ser criado");
	}
	puts("O Socket foi criado");
	
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = INADDR_ANY;
	server.sin_port = htons( 5000 );
	
	if( bind(socket_desc,(struct sockaddr *)&server , sizeof(server)) < 0)
	{
		perror("A escuta falhou");
		return 1;
	}
	puts("A escuta foi feito");
	
	listen(socket_desc , 3);
	
	puts("Esperando a conexão...");
	c = sizeof(struct sockaddr_in);
	
	client_sock = accept(socket_desc, (struct sockaddr *)&client, (socklen_t*)&c);
	if (client_sock < 0)
	{
		perror("Falha de aceitação");
		return 1;
	}
	puts("Conexão aceitada");
	
	while( (read_size = recv(client_sock , client_message , 2000 , 0)) > 0 )
	{
		write(client_sock , client_message , strlen(client_message));
	}
	
	if(read_size == 0)
	{
		puts("Cliente desconectado");
		fflush(stdout);
	}
	else if(read_size == -1)
	{
		perror("O recebimento falhou");
	}
	
	return 0;
}