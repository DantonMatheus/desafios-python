print('===== DESAFIO 76 =====')
preco = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Trasferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.35,
         'Canetas', 22.30,
         'Livro', 34.90)
print('-' * 40)
print(f'{"TABELA DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(preco)):
    if pos % 2 == 0:
        print(f'{preco[pos]:.<30}', end='')
    else:
        print(f'R${preco[pos]:>8.2f}')
print('-' * 40)
