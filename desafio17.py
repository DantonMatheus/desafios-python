from math import hypot
print('===== DESAFIO 17 =====')
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
print(f'O valor da Hipotenusa é {hypot(co,ca):.2f}')
