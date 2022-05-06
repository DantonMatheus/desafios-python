print('===== DESAFIO 85 =====')
valores = [[], []]
for cont in range(0, 7):
    val = (int(input(f'Digite o {cont+1}º valor: ')))
    if val % 2 == 0:
        valores[0].append(val)
    else:
        valores[1].append(val)
print('=-' * 20)
print(f'Os valores PARES digitados foram {sorted(valores[0])}')
print(f'Os valores ÍMPARES digitados foram {sorted(valores[1])}')
