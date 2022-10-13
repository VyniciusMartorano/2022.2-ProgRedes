import os, sys 
from questao_anp_lib import *
from questao_anp_constantes import *

# Montando uma lista com os arquivos do diretório de dados
try:
    lista_arquivos = os.listdir(DIR_DADOS)
except:
    print(f'\n{COR_ERRO}ERRO: Leitura do Diretório...{sys.exc_info()[0]}{COR_PADRAO}\n')
    sys.exit()
else:
    if len(lista_arquivos) == 0:
        print(f'\n{COR_ERRO}ERRO: O Diretório está vazio...{COR_PADRAO}\n')
        sys.exit()

# Lendo os arquivos
lista_dados = list()
for arquivo in lista_arquivos:
    print(f'\nLendo Arquivo: {COR_MENSAGEM}{arquivo}{COR_PADRAO}')
    nome_arquivo = DIR_DADOS + '\\' + arquivo
    lido, lista_auxiliar, erro = ler_arquivo(nome_arquivo,SEPARADOR,True)
    if lido:
        print(f'{COR_ACERTO}Lido com Sucesso...{COR_PADRAO}')
        lista_dados.extend(lista_auxiliar) 
    else:
        print(f'{COR_ERRO}ERRO: Erro na Leitura do Arquivo...{erro}{COR_PADRAO}')

# Criando o diretório onde os dados serão salvos
try:
    os.mkdir(DIR_ESTAT)
except:
    print(f'\n{COR_ERRO}ERRO: Diretório já existe...{COR_PADRAO}')

# Salvando os dados lidos
print(f'\nSalvando Arquivo:')
nome_arquivo = DIR_ESTAT + '\\dados_consolidados_anp.txt'
salvo, erro  = salvar_arquivo(lista_dados, nome_arquivo, SEPARADOR) 
if salvo:
    print(f'{COR_ACERTO}Arquivo salvo com Sucesso...{COR_PADRAO}\n')
else:
    print(f'{COR_ERRO}ERRO: Erro no salvamento do arquivo...{erro}{COR_PADRAO}')