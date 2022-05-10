print('===== DESAFIO 91 =====')
from random import randint
from time import sleep
sorteio = {'jogador1': '', 'jogador2': '', 'jogador3': '', 'jogador4': ''}
print('VALORES SORTEADOS:')
for k in sorteio.keys():
    dado = randint(1, 6)
    sorteio['jogador1'] = dado
    print(f'   O {k} tirou {dado}')
    sleep(1)
print(sorteio)
print('RANKING DOS JOGADORES:')
