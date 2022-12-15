import socket, sys

host = 'www.ifrn.edu.br'
port = 22

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)

try:
   erro = sock.connect_ex((host, port))
   if erro != 0: sys.exit()
except socket.gaierror:
   print('\nErro no HOST...')
else:
   print('\nConexão OK...')
   sock.close()

