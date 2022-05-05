print('===== DESAFIO 81 =====')
val = []
while True:
    val.append(int(input('Digite um número: ')))
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).strip().upper()
    if continua == 'N':
        break
print('=-' * 15)
print(f'Você digitou {len(val)} elementos!')
val.sort(reverse=True)
print(f'Os valores em ordem decrescente são {val}')
if 5 not in val:
    print('O valor 5 não foi encontrado em nenhuma posição!')
else:
    print(f'O valor 5 faz parte da lista na posição {val.index(5)}')
