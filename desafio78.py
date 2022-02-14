print('===== DESAFIO 78 =====')
valores = []
maior = posmaior = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('=-' * 20)
print(f'Você digitou os valores {valores}')
for c, v in enumerate(valores):
    if v > maior:
        maior = v
        posmaior = c
menor = valores[:]
menor.sort()
print(f'O maior valor digitado foi {maior} na posição {posmaior}')
print(f'O menor valor digitado foi {menor[0]} na posição {valores.index(menor[0])}')

'''
# SOLUÇÃO DO PROFESSOR:

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
'''
