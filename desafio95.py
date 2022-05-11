print('===== DESAFIO 95 =====')
team = []
jogador = {}
gols = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    if partidas != 0:
        for cont in range(0, partidas):
            gol = int(input(f'  Quantos gols na partida {cont + 1}?: '))
            gols.append(gol)
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    team.append(jogador.copy())
    gols.clear()
    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while continua not in 'SN':
        print('ERRO! Por favor, digite apenas S ou N')
        continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continua == 'N':
        break
print('=-' * 20)
print('COD ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('--' * 20)
for k, v in enumerate(team):
    print(f'{k:>3}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--' * 20)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
    if busca == 999:
        break
    if busca >= len(team):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f'  --LEVANTAMENTO DO JOGADOR {team[busca]["nome"]}: ')
        for i, g in enumerate(team[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
    print('--' * 20)
print('<< VOLTE SEMPRE! >>')
