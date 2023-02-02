import threading, time, os, random

# ----------------------------------------------------------------------------------------------------
def carro_f1(nome_piloto):
   tempo_inicio = time.time()
   for volta in range(45):
      velocidade = 1/random.randint(0, 300)
      time.sleep(velocidade)
      print(f'\t\tPILOTO: {nome_piloto} ....... volta {volta+1} em {velocidade:.5f} segundos')
   tempo_fim = time.time()
   delta_tempo = tempo_fim - tempo_inicio
   #print(f'\t{nome_piloto} concluiu a prova em {delta_tempo:.5f} segundos !!!')
# ----------------------------------------------------------------------------------------------------

os.system('cls')

print('-'*80)
print('Grande Prêmio Natal/RN 2021 de Fórmula 1')
print('-'*80)

try:
   print('\nÉ DADA A LARGADA...\n')
    
   # Instancia a THREAD na memória (solicita recursos ao SO)
   piloto_1 = threading.Thread(target=carro_f1, args=('LEWIS HAMILTON',) , name='p1')
   piloto_2 = threading.Thread(target=carro_f1, args=('FERNANDO ALONSO',), name='p2')
   piloto_4 = threading.Thread(target=carro_f1, args=('KIMI RAIKKONEN',) , name='p4')
   piloto_3 = threading.Thread(target=carro_f1, args=('MAX VERSTAPPEN',) , name='p3')

   # Iniciando a execução da THREAD
   piloto_1.start()
   piloto_2.start()
   piloto_4.start()
   piloto_3.start()

   # 'Unindo' os subprocessos ao processo principal
   piloto_1.join()
   piloto_2.join()
   piloto_4.join()
   piloto_3.join()
except:
   print('\nA CORRIDA NÃO PODE SER INICIADA...')
else:
   print('\n>>> BANDEIRA QUADRICULADA AGITADA....')
finally:
   print('\nÉ FIM DE CORRIDA...\n')