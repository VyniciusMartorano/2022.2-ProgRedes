import os, sys 
import questao_anp_lib as anp_lib

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
    print('\nDiretório já existe...')

# Montando uma lista com os arquivos do diretório de dados
try:
    lista_arquivos = os.listdir(diretorio_dados)
except:
    print(f'\nErro na Leitura do Diretório...{sys.exc_info()[0]}\n')
    sys.exit()

# Lendo os arquivos
lista_dados = list()
for arquivo in lista_arquivos:
    print('\nLendo Arquivo: {0}'.format(arquivo))
    nome_arquivo = diretorio_dados + '\\' + arquivo
    lido, lista_auxiliar, erro = anp_lib.ler_arquivo(nome_arquivo,';',True)
    if lido:
        print('Lido com Sucesso...')
        lista_dados.extend(lista_auxiliar) 
    else:
        print(f'Erro na Leitura...{erro}')

# Salvando os dados lidos
print('\nSalvando Arquivo:')
nome_arquivo = diretorio_estat + '\\dados_consolidados_anp.txt'
salvo, erro  = anp_lib.salvar_arquivo(lista_dados, nome_arquivo, ';') 
if salvo:
    print('Arquivo salvo com Sucesso...\n')
else:
    print(f'Erro na Leitura...{erro}')
