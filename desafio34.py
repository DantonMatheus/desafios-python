print('===== DESAFIO 34 =====')
salario = float(input('Digite seu salário: R$ '))
if salario <= 1250:
    print(f'Você receberá 15% de aumento, e seu novo salário será R$ {salario * 1.15}')
else:
    print(f'Você receberá 10% de aumento, e seu novo salário será R$ {salario * 1.10}')
