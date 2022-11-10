# -------------------------------------------------------------------------
# Exemplos de usos 'avançados' de funções para tratamento de dados
# Por Galileu Batista - IFRN 2019
# Adaptado por Charles Freitas - IFRN 2019
# -------------------------------------------------------------------------

import sys
import os
import cartola_lib

lstFormacoes = [
                  ['3-4-3', [3,0,4,3]], ['3-5-2', [3,0,5,2]], 
                  ['4-3-3', [2,2,3,3]], ['4-4-2', [2,2,4,2]], 
                  ['4-5-1', [2,2,5,1]], ['5-3-2', [2,3,3,2]], 
                  ['5-4-1', [3,2,4,1]]
               ]

# -------------------------------------------------------------------------

# Cria um dicionário com os dados do mercado e extrai os quatro valores
dicCartolaFC = cartola_lib.jsonCartola()

# Limpando a tela
os.system('cls')

while True:
   print('')
   print('='*100)
   print('SELECIONE O ESQUEMA TÁTICO')
   print('-'*100)
   for i in range(0, len(lstFormacoes)):
      print(f'[ {i+1} ] - Esquema Tático {lstFormacoes[i][0]}')
   print('[ 0 ] - SAIR\n')

   try:
      while True:
         intEsquema = int(input('Informe o Esquema Tático: '))
         if (intEsquema >= 1) and (intEsquema <= len(lstFormacoes)): break
         if (intEsquema == 0): sys.exit()
   except SystemExit:
      print('Programa Encerrado...')
      break
   except ValueError:
      print('Valor Informado Inválido...')
      continue
   except:
      print(f'Houve um Erro...{sys.exc_info()[0]}')
      continue

   # Montando o time
   print('')
   print('-'*100)
   print(f'SELEÇÃO DO CartolaFC - Esquema Tático {lstFormacoes[intEsquema-1][0]}')
   print('-'*100)
   time = cartola_lib.escalacao(dicCartolaFC, lstFormacoes[intEsquema-1][1])
   for i in range(0, len(time)):
      for j in range(0, len(time[i])):
         posicao = time[i][j]['posicao_nome'].upper() + ('.'*(10-len(time[i][j]['posicao_nome']))) + ':'
         atleta  = time[i][j]['apelido'].upper() + ' (' + time[i][j]['nome'] + ')'
         atleta  = atleta + ('.'*(60-len(atleta))) + ':'
         clube   = time[i][j]['clube_nome']
         print(f'{posicao} {atleta} {clube}')
   print('-'*100)
