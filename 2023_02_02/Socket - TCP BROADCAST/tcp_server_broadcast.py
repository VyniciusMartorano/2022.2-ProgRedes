import socket, threading, sys

HOST        = ''      # Definindo o IP do servidor
PORT        = 50000   # Definindo a porta
BUFFER_SIZE = 4096    # Definindo o tamanho do buffer
CODE_PAGE   = 'utf-8' # Definindo a página de codificação de caracteres

clientes   = []
ipClientes = []

# ------------------------------------------------------------
def Ler(conexao):
   while True: 
      dados = conexao.recv(BUFFER_SIZE)
      t2 = threading.Thread(target=Responder, args=(clientes, ipClientes, dados))
      t2.start()
      # como ela vai mandar de volta para todo mundo, nesse 
      # momento para ela não importa de quem ela recebeu os 
      # dados
      #print("Eu recebi de " +  ipmeninos + "esses dados: " + dados.decode("utf-8"))

def Responder(clientes, ipClientes, dados):
   print(cliente, ipClientes, dados)
   for cliente in clientes:
      cliente.sendall(dados)
      print('Deu certo!')
# ------------------------------------------------------------

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()

while True:
   conexao, cliente = sock.accept()
   clientes.append(conexao)
   ipClientes.append(cliente[0])
   try:
      t1 = threading.Thread(target=Ler, args=(conexao,))
      t1.start()
      print('O código principal terminou!!')
   except:
      print(f'Não deu certo...{sys.exc_info()[0]}') 
