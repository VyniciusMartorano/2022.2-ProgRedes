import socket

HOST        = ''      # Definindo o IP do servidor
PORT        = 50000   # Definindo a porta
BUFFER_SIZE = 4096    # Definindo o tamanho do buffer
CODE_PAGE   = 'utf-8' # Definindo a página de codificação de caracteres

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while True:
   m = input('Digite a mensagem: ')
   if m != '':
      mcod = m.encode(CODE_PAGE)
      sock.send(mcod)
      # desse linha acima até a 11 ele está lendo as 
      # mensagens e enviando.

      data = sock.recv(BUFFER_SIZE)
      m = data.decode(CODE_PAGE)
      print(f'Echo recebido: {data}')
      # daqui para cima até a linha 18 ele está exibindo a 
      # mensagem que recebeu do servidor então dentro desse 
      # while ele lê do usuário, manda a mensagem e já recebe 
      # de volta mensagem enviada
