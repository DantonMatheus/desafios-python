print('===== DESAFIO 75 =====')
num = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 not in num:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {num.index(3) +1}ª posição')
print(f'Os valores PARES digitados foram: ', end='')
for cont in range(0, len(num)):
    if num[cont] % 2 == 0:
        print(num[cont], end=' ')
