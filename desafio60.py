print('===== DESAFIO 60 =====')
num = int(input('Digite um número inteiro para calcular seu FATORIAL: '))
fat = 1
i = 2
while i <= num:
    fat = fat * i
    i += 1
print(f'O FATORIAL de {num} é {fat}')


# Solução do professor:
'''
from math import factorial
n = int(input('Digite um número inteiro: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')

#################################################

n = int(input('Digite um número inteiro: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
'''