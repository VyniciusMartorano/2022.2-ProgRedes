import sys

def ler_arquivo(strNomeArquivo: str, strSeparador: str, boolCabecalho: bool):
    lstValores    = list()
    try:
        arquivo_input = open(strNomeArquivo, 'r', encoding='utf-8')
        if boolCabecalho: linha = arquivo_input.readline()
        while True:
            linha = arquivo_input.readline()[:-1]
            if not linha: break
            linha = linha.split(strSeparador)
            lista_aux = [linha[0], linha[1], linha[10], 
                         int(linha[11][6:10]), 
                         float(linha[12].replace(',','.')), linha[15]]
            lstValores.append(lista_aux)
        arquivo_input.close()
    except ValueError:
        lstValores.clear()
        return False, lstValores, 'VALOR INCOMPATÍVEL'
    except:
        lstValores.clear()
        return False, lstValores, sys.exc_info()[0]
    else:
        return True, lstValores, None
