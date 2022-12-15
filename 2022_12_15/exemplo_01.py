import socket

host = 'www.ifrn.edu.br'
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
   sock.connect((host, port))
except socket.gaierror:
   print('\nErro de Conexão')
else:
   print('\nConexão OK')
   sock.close()