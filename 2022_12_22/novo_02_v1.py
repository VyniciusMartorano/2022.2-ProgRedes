import socket, sys

host  = input('\nInforme o nome do HOST ou URL do site: ')

alvo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

alvo.connect((host , 80))

requisicao = f'GET / HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\n\r\n'
alvo.sendall(requisicao.encode())

while True:
    dados = alvo.recv(10240)

    if not dados: break

    print(dados.decode())

print('\n'+'-'*100)
print('Fim dos dados')