# Um cliente simples que se conecta a um servidor 
# de horário e responde com um horário atual
import socket

alvo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'time.nist.gov'
port = 13

alvo.connect((host, port))
alvo.sendall(b'')

print(str(alvo.recv(4096), 'utf-8'))

# Os servidores de horário vêm e vão, 
# então talvez seja necessário encontrar 
# um servidor que funcione em https://www.ntppool.org/en/