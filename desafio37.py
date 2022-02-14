print('===== DESAFIO 37 =====')
num = int(input('Digite um número inteiro: '))
base = int(input('Qual será a base de conversão? Sendo: \n'
                 '[1] para binário \n'
                 '[2] para octal \n'
                 '[3] para hexadecimal \n'
                 'Digite aqui sua opção:'))
if base == 1:
    print(f'O número {num} convertido em binário é igual a {bin(num) [2:]}')
elif base == 2:
    print(f'O número {num} convertido em octal é igual a {oct(num) [2:]}')
elif base == 3:
    print(f'O número {num} convertido em hexadecimal é igual a {hex(num) [2:]}')
else:
    print('Erro! O número escolhido não está na lista. Favor digitar 1 para binário, 2 para octal ou 3 para hexadecimal')
