import socket, sys

BUFFER = 512
host   = input('\nInforme o nome do HOST ou URL do site: ')

alvo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

alvo.connect((host , 80))

requisicao = f'GET / HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\n\r\n'
alvo.sendall(requisicao.encode())

while True:
    dados = alvo.recv(BUFFER)
    if not dados: break
    dados = dados.decode()
    print(dados[:dados.find('\r\n\r\n')])
    if '\r\n\r\n' in dados: break

print('\n'+'-'*100)
print('Fim dos dados')