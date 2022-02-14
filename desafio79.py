print('===== DESAFIO 79 =====')
val = []
while True:
    num = int(input('Digite um número: '))
    if num not in val:
        val.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar!')
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continua == "N":
        break
print('=-' * 15)
val.sort()
print(f'Você digitou os valores: {val}')
