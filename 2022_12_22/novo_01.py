import socket

host  = input('\nInforme o nome do HOST ou URL do site: ')

alvo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
alvo.connect((host , 80))

requisicao = f'HEAD / HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\n\r\n'
alvo.sendall(requisicao.encode())

print('-'*100)
print(str(alvo.recv(1024), 'utf-8'))
print('-'*100)
