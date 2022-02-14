print('===== DESAFIO 72 =====')
num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
       'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um número entre 0 e 20: '))
while n not in (range(0, 20)):
       n = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {num[n]}')
