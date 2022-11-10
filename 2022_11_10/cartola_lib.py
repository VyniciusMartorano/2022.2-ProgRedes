import requests
import json

strURL = 'https://api.cartolafc.globo.com/atletas/mercado'

# ----------------------------------------------------------------------------------------
# Retorna um dicionário com os dados do mercado do Cartola (2019.1)
# O dicionário está ordenado pela pontuação do atleta deforma decrescente
def jsonCartola():
   dic_cartola = requests.get(strURL, verify=True).json()
   dic_atletas = dic_cartola['atletas']
   dic_atletas = sorted(dic_atletas, key=lambda a: a['jogos_num'] * a['media_num'], reverse=True)

   global dic_clubes   
   global dic_posicoes 
   dic_clubes   = dic_cartola['clubes']
   dic_posicoes = dic_cartola['posicoes']
   #dic_status  = dic_cartola['status']
   return dic_atletas


# ----------------------------------------------------------------------------------------
# Retorna uma lista com os dados do atleta
def atleta(dicCartola, intPosicao, intQtDados=1):
   tupla_filtro = list(filter(lambda a: a['posicao_id'] == intPosicao, dicCartola))[0:intQtDados]

   # Transformando a tupla em lista. cada posição da lista é um dicionário
   lst_auxiliar = []
   for i in range(0, intQtDados): lst_auxiliar.append(tupla_filtro[i])
   
   # Definindo os dados que serão retornados
   lst_dados_retorno = ['nome', 'apelido', 'clube_id', 'posicao_id', 'media_num', 'jogos_num']
   lst_retorno = []
   for i in range(0,len(lst_auxiliar)):
      dic_auxiliar = {}
      for key, value in lst_auxiliar[i].items():
         if (key in lst_dados_retorno): dic_auxiliar[key] = value
      # Adicionando o nome do clube
      dic_auxiliar['clube_nome'] = clube(str(dic_auxiliar['clube_id']))
      # Adicionando a descrição da posição
      dic_auxiliar['posicao_nome'] = posicao(str(dic_auxiliar['posicao_id']))
      lst_retorno.append(dic_auxiliar)
   
   return lst_retorno

# ----------------------------------------------------------------------------------------
# Retorna o nome do clube
def clube(strClubeID):
   strNomeClube = dic_clubes[strClubeID]['nome']
   return strNomeClube

# ----------------------------------------------------------------------------------------
# Retorna a Descrição da Posiçao
def posicao(strPosicaoID):
   strNomePosicao = dic_posicoes[strPosicaoID]['nome']
   return strNomePosicao

# ----------------------------------------------------------------------------------------
def escalacao(dicCartola, lstFormacao):   
   # Montando a escalação
   escalacao = []
   escalacao.append(atleta(dicCartola, 6)) # Técnico
   escalacao.append(atleta(dicCartola, 1)) # Goleiro
   escalacao.append(atleta(dicCartola, 3, lstFormacao[0])) # Zagueiros
   escalacao.append(atleta(dicCartola, 2, lstFormacao[1])) # Laterais
   escalacao.append(atleta(dicCartola, 4, lstFormacao[2])) # Meias
   escalacao.append(atleta(dicCartola, 5, lstFormacao[3])) # Atacantes

   return escalacao

