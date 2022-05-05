print('===== DESAFIO 82 =====')
val = []
pares = []
impares = []
while True:
    val.append(int(input('Digite um número: ')))
    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continua in 'N':
        break
print('=-' * 20)
print(f'A lista completa é {val}')
for c, p in enumerate(val):
    if p % 2 == 0:
        pares.append(p)
print(f'A lista de PARES é {pares}')
for c, i in enumerate(val):
    if i % 2 == 1:
        impares.append(i)
print(f'A lista de ÍMPARES é {impares}')
