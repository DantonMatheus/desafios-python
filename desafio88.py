print('================ DESAFIO 88 ================')
from random import randrange
from time import sleep
print('-' * 44)
print(f'             JOGA NA MEGA SENA')
print('-' * 44)
mega = []
jogos = int(input('Quantos jogos você quer que eu sorteie?: '))
print(f'-=-=-=-=-=-= SORTEANDO {jogos} JOGOS -=-=-=-=-=-=')
for c in range(0, jogos):
    for cont in range(0, 6):
        sorteio = randrange(1, 60)
        if sorteio not in mega:
            mega.append(sorteio)
    print(f'Jogo {c + 1}: {sorted(mega)}')
    mega.clear()
    sleep(1)
print('================ BOA SORTE! ================')
