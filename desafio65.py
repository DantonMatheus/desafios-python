print('===== DESAFIO 65 =====')
resp = 'S'
media = 0
soma = 0
quant = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média é {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
