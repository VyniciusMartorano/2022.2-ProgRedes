import time, os

# ----------------------------------------------------------------------------------------------------
def carro_f1(nome_piloto, velocidade_carro):
    tempo_inicio = time.time()
    for volta in range(10):
        time.sleep(1/velocidade_carro)
        print(f'\t\tPILOTO: {nome_piloto} ....... volta {volta} em {1/velocidade_carro:.5f} segundos')
    tempo_fim = time.time()
    delta_tempo = tempo_fim - tempo_inicio
    print(f'\t{nome_piloto} concluiu a prova em {delta_tempo:.5f} segundos !!!')
# ----------------------------------------------------------------------------------------------------

os.system('cls')

print('-'*80)
print('Grande Prêmio Natal/RN 2023 de Fórmula 1')
print('-'*80)

try:
    print('\nÉ DADA A LARGADA...\n')
    
    piloto_1 = carro_f1('LEWIS HAMILTON', 25)
    piloto_2 = carro_f1('FERNANDO ALONSO', 5)
    piloto_3 = carro_f1('MAX VERSTAPPEN', 20)
    piloto_4 = carro_f1('KIMI RAIKKONEN', 10)
except:
    print('\nA CORRIDA NÃO PODE SER INICIADA...')
else:
    print('\n>>> BANDEIRA QUADRICULADA AGITADA....')
finally:
    print('\nÉ FIM DE CORRIDA...\n')
