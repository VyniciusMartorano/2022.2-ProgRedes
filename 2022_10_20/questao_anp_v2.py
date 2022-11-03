# Contribuições de Galileu Batista - IFRN - out/2022
import os, sys
from datetime import datetime
from questao_anp_lib import *
from questao_anp_constantes import *

# ------------------------------------------------------------
# Limpando a tela
os.system('cls')

# ------------------------------------------------------------
# QUESTÃO 01
# Montando uma lista com os arquivos do diretório de dados
print(f'\n{COR_TITULO}Lendo o Diretório de Dados...{COR_PADRAO}')
t_inicial = datetime.now()
try:
    lista_arquivos = os.listdir(DIR_DADOS)
except FileNotFoundError:
    print(f'{COR_ERRO}ERRO: Diretório Não Existe...{COR_PADRAO}\n')
    sys.exit()
except:
    print(f'{COR_ERRO}ERRO: Leitura do Diretório...{sys.exc_info()[0]}{COR_PADRAO}\n')
    sys.exit()
else:
    if len(lista_arquivos) == 0:
        print(f'{COR_ERRO}ERRO: O Diretório está vazio...{COR_PADRAO}')
        sys.exit()
    else:
        print(f'{COR_ACERTO}Criado com Sucesso...{COR_PADRAO}')
t_final = datetime.now()
delta_t = t_final - t_inicial
print(f'\nTempo Decorrido: {COR_MENSAGEM}{delta_t}{COR_PADRAO}\n')

# ------------------------------------------------------------
# QUESTÃO 01 - Item B
# Lendo os arquivos
print(f'\n{COR_TITULO}Lendo os Arquivos de INPUT...{COR_PADRAO}')
t_inicial   = datetime.now()
lista_dados   = list()
for arquivo in lista_arquivos:
    print(f'Lendo Arquivo: {COR_MENSAGEM}{arquivo}{COR_PADRAO} ... ', end=' ')
    nome_arquivo = DIR_DADOS + '\\' + arquivo
    lido, lista_auxiliar, erro = ler_arquivo(nome_arquivo,SEPARADOR,True)
    if lido:
        print(f'{COR_ACERTO}Lido com Sucesso...{COR_PADRAO}')
        lista_dados.extend(lista_auxiliar)
    else:
        print(f'{COR_ERRO}ERRO: Erro na Leitura do Arquivo...{erro}{COR_PADRAO}')
t_final = datetime.now()
delta_t = t_final - t_inicial
print(f'\nTempo Decorrido: {COR_MENSAGEM}{delta_t}{COR_PADRAO}\n')

# ------------------------------------------------------------
# QUESTÃO 01 - Item A
# Criando o diretório onde os dados serão salvos
print(f'\n{COR_TITULO}Criando o Diretório de Estatísticas...{COR_PADRAO}')
t_inicial = datetime.now()
try:
    os.mkdir(DIR_ESTAT)
except:
    print(f'{COR_ERRO}ERRO: Diretório já existe...{COR_PADRAO}')
else:    
    print(f'{COR_ACERTO}Criado com Sucesso...{COR_PADRAO}')
t_final = datetime.now()
delta_t = t_final - t_inicial
print(f'\nTempo Decorrido: {COR_MENSAGEM}{delta_t}{COR_PADRAO}\n')

# ------------------------------------------------------------
# QUESTÃO 01 - Item C
# Salvando os dados lidos
print(f'\n{COR_TITULO}Salvando Arquivo de Consolidação...{COR_PADRAO}')
t_inicial = datetime.now()
nome_arquivo = DIR_ESTAT + '\\dados_consolidados_anp.txt'
salvo, erro  = salvar_arquivo(lista_dados, nome_arquivo, SEPARADOR) 
if salvo:
    print(f'{COR_ACERTO}Arquivo salvo com Sucesso...{COR_PADRAO}')
else:
    print(f'{COR_ERRO}ERRO: Erro no salvamento do arquivo...{erro}{COR_PADRAO}')
t_final = datetime.now()
delta_t = t_final - t_inicial
print(f'\nTempo Decorrido: {COR_MENSAGEM}{delta_t}{COR_PADRAO}\n')

# ------------------------------------------------------------
# QUESTÃO 01 - Item D (i) - 
print(f'\n{COR_TITULO}Gerando as Estatísticas...{COR_PADRAO}')

# Montando o conjunto de dados base
print(f'{COR_SUBTITULO}Montando o conjunto de dados base...{COR_PADRAO}')
t_inicial      = datetime.now()
set_regioes   = set([dados[0] for dados in lista_dados])
set_produtos  = set([dados[2] for dados in lista_dados])
set_anos      = set([dados[3] for dados in lista_dados])
set_bandeiras = set([dados[5] for dados in lista_dados])
t_final = datetime.now()
delta_t = t_final - t_inicial
print(f'\nTempo Decorrido: {COR_MENSAGEM}{delta_t}{COR_PADRAO}\n')

# Dados: bandeira;produto;ano;valor_medio_venda;quantidade_postos
print(f'{COR_SUBTITULO}\nBandeira x Produto x Ano x Valor Médio x Qt. Postos{COR_PADRAO}')
t_inicial      = datetime.now()
lista_bandeira = list()
for bandeira in set_bandeiras:
    for produto in set_produtos:
        for ano in set_anos:
            lista_filtro = list(filter(lambda filtro: (bandeira == filtro[5] and
                                            produto == filtro[2] and
                                            ano == filtro[3]), lista_dados))
            if len(lista_filtro) == 0: continue 
            soma_valor = 0
            for filtro in lista_filtro: soma_valor += filtro[4]
            lista_bandeira.append([bandeira, produto, ano, soma_valor/len(lista_filtro), len(lista_filtro)])
t_final = datetime.now()
delta_t = t_final - t_inicial
print(f'\nTempo Decorrido: {COR_MENSAGEM}{delta_t}{COR_PADRAO}\n')

# Arquivo: media_bandeira.txt
print(f'\n{COR_TITULO}Salvando Arquivo...{COR_PADRAO}')
t_inicial    = datetime.now()
nome_arquivo = DIR_ESTAT + '\\media_bandeira.txt'
salvo, erro  = salvar_arquivo(lista_bandeira, nome_arquivo, SEPARADOR) 
if salvo:
    print(f'{COR_ACERTO}Arquivo salvo com Sucesso...{COR_PADRAO}\n')
else:
    print(f'{COR_ERRO}ERRO: Erro no salvamento do arquivo...{erro}{COR_PADRAO}')
t_final = datetime.now()
delta_t = t_final - t_inicial
print(f'\nTempo Decorrido: {COR_MENSAGEM}{delta_t}{COR_PADRAO}\n')

# Dados: produto;região;ano;valor_medio;quantidade_postos
print(f'{COR_SUBTITULO}\nProduto x Região x Ano x Valor Médio x Qt. Postos{COR_PADRAO}')
t_inicial    = datetime.now()
lista_regiao = list()
for produto in set_produtos:
    for regiao in set_regioes:
        for ano in set_anos:
            lista_filtro = list(filter(lambda filtro: (filtro[2] == produto and
                                            filtro[0] == regiao and
                                            filtro[3] == ano), lista_dados))
            if len(lista_filtro) == 0: continue 
            soma_valor = 0
            for filtro in lista_filtro: soma_valor += filtro[4]
            lista_bandeira.append([produto, regiao, ano, soma_valor/len(lista_filtro), len(lista_filtro)])
t_final = datetime.now()
delta_t = t_final - t_inicial
print(f'\nTempo Decorrido: {COR_MENSAGEM}{delta_t}{COR_PADRAO}\n')

# Arquivo: media_produto_regiao.txt
print(f'\n{COR_TITULO}Salvando Arquivo...{COR_PADRAO}')
t_inicial    = datetime.now()
nome_arquivo = DIR_ESTAT + '\\media_produto_regiao.txt'
salvo, erro  = salvar_arquivo(lista_bandeira, nome_arquivo, SEPARADOR) 
if salvo:
    print(f'{COR_ACERTO}Arquivo salvo com Sucesso...{COR_PADRAO}\n')
else:
    print(f'{COR_ERRO}ERRO: Erro no salvamento do arquivo...{erro}{COR_PADRAO}')
t_final = datetime.now()
delta_t = t_final - t_inicial
print(f'\nTempo Decorrido: {COR_MENSAGEM}{delta_t}{COR_PADRAO}\n')
