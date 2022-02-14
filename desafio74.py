from random import randrange
print('===== DESAFIO 74 =====')
num = (randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10))
menor = maior = sorted(num)
print(f'Os valores sorteados foram: {num}')
print(f'O menor valor sorteado foi: {menor[0]}')
print(f'O maior valor sorteado foi: {maior[4]}')
