# Conectando a um servidor QOTD (Quote Of The Day)
import socket

alvo = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = b''
addr = ("djxmmx.net", 17)

alvo.sendto(message, addr)

data, address = alvo.recvfrom(1024)

print(data.decode())