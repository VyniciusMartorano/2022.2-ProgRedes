# Importando a biblioteca socket
import socket

HOST = 'localhost'  #Definindo o IP do servidor
PORT = 50000 #Definindo a porta

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = input('Digite a mensagem: ')

# Convertendo a mensagem digitada de string para bytes
msg = msg.encode('utf-8')

# Enviando a mensagem ao servidor      
udp_socket.sendto(msg, (HOST, PORT))

# Fechando o socket
udp_socket.close()
