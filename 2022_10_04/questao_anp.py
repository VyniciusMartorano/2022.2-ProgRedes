import os 

# Obtendo o diretório onde o programa .PY está salvo
diretorio_app   = os.path.dirname(os.path.abspath(__file__)) 

# Montando o diretório onde os dados fonte estão guardados
diretorio_dados = diretorio_app + '\\serie_historica_anp'

# Montando o diretório onde os dados estatisticos serão salvos
diretorio_estat = diretorio_app + '\\dados_estatisticos'

# Montando uma lista com os arquivos do diretório de dados
lista_arquivos = os.listdir(diretorio_dados)

