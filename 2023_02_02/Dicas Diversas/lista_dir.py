import os

# Obtem o caminho completo (diretorio + arquivo) corrente
caminho = os.path.abspath(__file__)

# Extrai apenas o diretorio do arquivo corrente
caminho = os.path.dirname(caminho)

# Adiciono um subdiretorio ao caminho obtido
caminho += '\\server_files'

# Obtenho a relação dos arquivos do caminho especificado
# O retorno é uma lista
arquivos = os.listdir(caminho)
print(arquivos)

# Obtendo o tamanho de cada arquivo da lista
tamanhos = list()
for arquivo in arquivos:
    tamanho = os.path.getsize(caminho + '\\' + arquivo)
    tamanhos.append(tamanho)
print(tamanhos)