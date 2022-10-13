import os, sys 
from questao_anp_lib import *
from questao_anp_constantes import *

# ------------------------------------------------------------
# QUESTÃO 01
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

# ------------------------------------------------------------
# QUESTÃO 01 - Item B
# Lendo os arquivos
lista_dados    = list()
for arquivo in lista_arquivos:
    print(f'\nLendo Arquivo: {COR_MENSAGEM}{arquivo}{COR_PADRAO}')
    nome_arquivo = DIR_DADOS + '\\' + arquivo
    lido, lista_auxiliar, erro = ler_arquivo(nome_arquivo,SEPARADOR,True)
    if lido:
        print(f'{COR_ACERTO}Lido com Sucesso...{COR_PADRAO}')
        lista_dados.extend(lista_auxiliar) 
    else:
        print(f'{COR_ERRO}ERRO: Erro na Leitura do Arquivo...{erro}{COR_PADRAO}')

# ------------------------------------------------------------
# QUESTÃO 01 - Item A
# Criando o diretório onde os dados serão salvos
try:
    os.mkdir(DIR_ESTAT)
except:
    print(f'\n{COR_ERRO}ERRO: Diretório já existe...{COR_PADRAO}')

# ------------------------------------------------------------
# QUESTÃO 01 - Item C
# Salvando os dados lidos
print(f'\nSalvando Arquivo:')
nome_arquivo = DIR_ESTAT + '\\dados_consolidados_anp.txt'
salvo, erro  = salvar_arquivo(lista_dados, nome_arquivo, SEPARADOR) 
if salvo:
    print(f'{COR_ACERTO}Arquivo salvo com Sucesso...{COR_PADRAO}\n')
else:
    print(f'{COR_ERRO}ERRO: Erro no salvamento do arquivo...{erro}{COR_PADRAO}')

# ------------------------------------------------------------
# QUESTÃO 01 - Item D (i) e (ii)
# Arquivo: media_bandeira.txt
# Dados_1: bandeira;produto;ano;valor_medio_venda;quantidade_postos
# Dados_2: produto;região;ano;valor_medio;quantidade_postos
print(f'\nGerando as estatísticas:')
lista_bandeira = list()
lista_regiao   = list()
for dados in lista_dados:
    lista_temp_bandeira = [dados[5], dados[2], dados[3], 0, 0]
    lista_temp_regiao   = [dados[2], dados[0], dados[3], 0, 0]
    if lista_temp_bandeira not in lista_bandeira:
        lista_bandeira.append(lista_temp_bandeira)
    if lista_temp_regiao not in lista_regiao:
        lista_regiao.append(lista_temp_regiao)

for filtro in lista_bandeira:
    # Filtrando a BANDEIRA
    lista_filtro_1 = list(filter(lambda a:a[5] == filtro[0], lista_dados))
    # Filtrando o PRODUTO
    lista_filtro_2 = list(filter(lambda a:a[2] == filtro[1], lista_filtro_1))
    # Filtrando o ANO
    lista_filtro_3 = list(filter(lambda a:a[3] == filtro[2], lista_filtro_2))
    soma = 0
    for dados in lista_filtro_3: soma += dados[4] 
    filtro[3] = soma / len(lista_filtro_3)
    filtro[4] = len(lista_filtro_3)
    
print(f'\nSalvando Arquivo:')
nome_arquivo = DIR_ESTAT + '\\media_bandeira.txt'
salvo, erro  = salvar_arquivo(lista_bandeira, nome_arquivo, SEPARADOR) 
if salvo:
    print(f'{COR_ACERTO}Arquivo salvo com Sucesso...{COR_PADRAO}\n')
else:
    print(f'{COR_ERRO}ERRO: Erro no salvamento do arquivo...{erro}{COR_PADRAO}')
