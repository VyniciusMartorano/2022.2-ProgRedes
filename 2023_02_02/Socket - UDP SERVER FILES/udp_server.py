# Importando a biblioteca socket e sys
import sys, socket

# Definindo as constantes do programa
HOST        = ''            # Definindo o IP do servidor
PORT        = 60000         # Definindo a porta
CODE_PAGE   = 'utf-8'       # Definindo a página de código de caracteres
BUFFER_SIZE = 512           # Definindo o tamanho do buffer

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular o socket a tupla (host, port)
udp_socket.bind((HOST, PORT)) 

print(f'\nSERVIDOR ATIVO: {udp_socket.getsockname()}')
print('\nRecebendo Mensagens...\n\n')

try:
    while True:
        # Recebendo os dados do cliente
        mensagem, ip_cliente = udp_socket.recvfrom(BUFFER_SIZE)
        # Convertendo a mensagem recebida de bytes para string
        mensagem = mensagem.decode(CODE_PAGE)
        # Imprimindo a mensagem recebida 
        if mensagem.upper() == 'EXIT':
            print(f'\nO {ip_cliente} SE DESCONECTOU DO SERVIDOR...\n')
        else:
            print(f'{ip_cliente}->  {mensagem}')
            # Devolvendo uma mensagem (echo) ao cliente
            mensagem_volta = 'DEVOLVENDO... ' + mensagem
            udp_socket.sendto(mensagem_volta.encode(CODE_PAGE), ip_cliente)
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
finally:    
    # Fechando o socket
    udp_socket.close()