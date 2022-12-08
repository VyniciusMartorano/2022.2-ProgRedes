import socket  

host = input('Digite o caminho no formato www.caminho.com: ')

alvo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
alvo.connect((host,80))

print('\nConexão estabelecida com sucesso...')

requisicao = f'GET / HTTP/1.1\r\nHost:{host}\r\n\r\n'
alvo.send(requisicao.encode())

resposta = alvo.recv(4096)
print(f'\n{resposta.decode()}')

print(f'\n{len(resposta)} Bytes Lidos')