print('===== DESAFIO 71 =====')
print('=' * 20)
print('       BANCO     ')
print('=' * 20)
saque = int(input('Qual valor você quer sacar? R$ '))
tot = saque
nota = 50
totnota = 0
while True:
    if tot >= nota:
        tot -= nota
        totnota += 1
    else:
        if totnota > 0:
            print(f'Total de {totnota} cédulas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totnota = 0
        if tot == 0:
            break
print('Obrigado por usar o CAIXA ELETRÔNICO. Volte sempre!')
