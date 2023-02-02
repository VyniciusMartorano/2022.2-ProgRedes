import socket, threading, sys

HOST        = ''      # Definindo o IP do servidor
PORT        = 50000   # Definindo a porta
BUFFER_SIZE = 4096    # Definindo o tamanho do buffer
CODE_PAGE   = 'utf-8' # Definindo a página de codificação de caracteres

# ------------------------------------------------------------
def LerResponder(conexao, cliente):
   while True: 
      dados = conexao.recv(BUFFER_SIZE)
      dados = dados.decode(CODE_PAGE) 
      print(f'Recebi de {cliente[0]} os dados: {dados}')
      conexao.sendall(dados)
# ------------------------------------------------------------


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()
# precisa escutar, já que ele irá receber solicitações de 
# diversos clientes?
# é obrigatório ter o listen, porque é ele quem escuta, 
# porque ele precisa ficar ouvindo mas é o accept é quando 
# ele diz que quer tratar essa conexão.

while True:
   conexao, cliente = sock.accept()

   # agora eu preciso criar a função que as threads irão 
   # executar, tenho que passar como parametro essa conexão e 
   # o cliente. Para que depoisa thread saiba quem responder

   try:
      t1 = threading.Thread(target=LerResponder, args=(conexao, cliente))
      t1.start()
      print('O código principal terminou!!')
   except:
      print(f'Não deu certo...{sys.exc_info()[0]}') 

