import os

# Obtendo o diretório onde o programa .PY está salvo
diretorio_app = os.path.dirname(os.path.abspath(__file__)) 

# Definindo as constantes de diretórios
DIR_DADOS = diretorio_app + '\\serie_historica_anp'
DIR_ESTAT = diretorio_app + '\\dados_estatisticos'

# Definindo a constante do separador de dados
SEPARADOR = ';'

# Definindo as constantes das cores de texto
COR_ERRO      = '\033[40;31;1m'
COR_ACERTO    = '\033[40;34;1m'
COR_PADRAO    = '\033[40;37m'
COR_MENSAGEM  = '\033[40;32m'
COR_TITULO    = '\033[43;30m'
COR_SUBTITULO = '\033[40;33m'