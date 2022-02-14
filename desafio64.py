print('===== DESAFIO 64 =====')
num = 0
cont = 0
soma = 0
num = int(input('Digite um número [999 para SAIR]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para SAIR]: '))
print(f'Você digitou {cont} números! A soma entre eles é {soma}')
