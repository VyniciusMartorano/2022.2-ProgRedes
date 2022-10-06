import os 

# Obtendo o diretório onde o programa .PY está salvo
diretorio_app   = os.path.dirname(os.path.abspath(__file__)) 

# Montando o diretório onde os dados fonte estão guardados
diretorio_dados = diretorio_app + '\\serie_historica_anp'

# Montando o diretório onde os dados estatisticos serão salvos
diretorio_estat = diretorio_app + '\\dados_estatisticos'

# Criando o diretório onde os dados serão salvos
try:
    os.mkdir(diretorio_estat)
except:
    print('Diretório já existe...')

# Montando uma lista com os arquivos do diretório de dados
lista_arquivos = os.listdir(diretorio_dados)

# Lendo os arquivos
lista_dados = list()
for arquivo in lista_arquivos:
    print('Lendo Arquivo: {0}'.format(arquivo))
    nome_arquivo = diretorio_dados + '\\' + arquivo
    arquivo_input = open(nome_arquivo, 'r', encoding='utf-8')
    linha = arquivo_input.readline()
    while True:
        linha = arquivo_input.readline()[:-1]
        if not linha: break
        linha = linha.split(';')
        lista_aux = [linha[0], linha[1], linha[10], 
                     int(linha[11][6:10]), 
                     float(linha[12].replace(',','.')), linha[15]]
        lista_dados.append(lista_aux)
    arquivo_input.close()


# Salvando os dados lidos
print('\nSalvando Arquivo:')
nome_arquivo = diretorio_estat + '\\dados_consolidados_anp.txt'
arquivo_output = open(nome_arquivo, 'w', encoding='utf-8') 
for dados in lista_dados:
    #linha = dados[0] + ';' + dados[1] + ';' + dados[2] + ';' + str(dados[3]) + ';' + str(dados[4]) + ';' + dados[5] + '\n'
    linha = ''
    for valor in dados: linha += str(valor) + ';'
    linha = linha[:-1] + '\n'
    arquivo_output.write(linha)
arquivo_output.close()