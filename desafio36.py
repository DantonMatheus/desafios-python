print('===== DESAFIO 36 =====')
casa = float(input('Digite o valor da casa que você deseja comprar: R$ '))
salario = float(input('Digite o valor do seu salário: R$ '))
tempo = int(input('Digite em quantos anos você deseja pagar a casa: '))
parcela = casa / (tempo * 12)
if parcela >= (salario * 0.3):
    print('Seu empréstimo NÃO foi aprovado! O valor da parcela excede 30% do seu salário! Tente novamente!')
else:
    print(f'Seu empréstimo foi aprovado! O valor da sua parcela é de R$ {parcela}')
