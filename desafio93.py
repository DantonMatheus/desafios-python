print('===== DESAFIO 93 =====')
jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
if partidas != 0:
    for cont in range(0, partidas):
        gol = int(input(f'Quantos gols na partida {cont}?: '))
        gols.append(gol)
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('=-' * 30)
print(jogador)
print('=-' * 30)
for i, v in jogador.items():
    print(f'O campo {i} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas!')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols!')
