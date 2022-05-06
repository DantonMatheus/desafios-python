print('===== DESAFIO 84 =====')
galera = []
dado = []
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    galera.append(dado[:])
    dado.clear()
    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continua in 'N':
        break
print('=-' * 20)
print(f'Ao todo, você cadastrou {len(galera)} pessoas!')
for p in galera:
    if p[1] > maior:
        maior = p[1]
print(f'O maior peso foi de {maior}. Peso de ', end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
for p in galera:
    if p[1] < maior:
        menor = p[1]
print(f'\nO menor peso foi de {menor}. Peso de ', end='')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
