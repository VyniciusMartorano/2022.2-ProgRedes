# Importando a biblioteca socket e sys
import socket, sys

HOST = ''  #Definindo o IP do servidor
PORT = 50000 #Definindo a porta

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.bind((HOST, PORT)) # Ligando o socket a porta

print('Recebendo Mensagens...\n\n')

try:
    while True:
        # Recebendo os dados do cliente
        msg, cliente = udp_socket.recvfrom(512) #buffer de 512 bytes
        # Imprimindo a mensagem recebida convertendo de bytes para string
        print(cliente, msg.decode('utf-8'))
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
finally:    
    # Fechando o socket
    udp_socket.close()