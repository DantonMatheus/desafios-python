print('===== DESAFIO 70 =====')
print('-' *30)
print('        LOJA O BARATO     ')
print('-' * 30)
tot = caro = barato = cont = 0
nomebarato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preço: '))
    cont += 1
    tot += preco
    if preco >= 1000:
        caro += 1
    if cont == 1:
        barato = preco
        nomebarato = produto
    else:
        if preco < barato:
            barato = preco
            nomebarato = produto
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continua == "N":
        break
print('----- FIM DO PROGRAMA -----')
print(f'O total da compra foi R${tot}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R${barato}')
