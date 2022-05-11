print('===== DESAFIO 91 =====')
from random import randint
from time import sleep
from operator import itemgetter
sorteio = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
ranking = list()
print('VALORES SORTEADOS:')
for k, v in sorteio.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
print('RANKING DOS JOGADORES:')
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
