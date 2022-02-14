print('===== DESAFIO 44 =====')
preco = float(input('Digite o preço do produto: R$ '))
pag = int(input('Escolha qual será a condição de pagamento: \n'
                '[1] À vista no dinheiro ou cheque: 10% de desconto \n'
                '[2] À vista no cartão: 5% de desconto \n'
                '[3] Em até 2x no cartão: não tem desconto \n'
                '[4] Em 3x ou mais no cartão: 20% de juros \n'
                'Digite aqui sua opção: '))
if pag == 1:
    print(f'Você escolheu a primeira opção. O valor a ser pago é {preco * 0.9}')
elif pag == 2:
    print(f'Você escolheu a segunda opção. O valor a ser pago é {preco * 0.95}')
elif pag == 3:
    print(f'Você escolheu a terceira opção. O valor a ser pago é {preco}')
elif pag == 4:
    print(f'Você escolheu a quarta opção. O valor a ser pago é {preco * 1.2}')
else:
    print('ERRO! Você não escolheu uma opção válida. Por favor, tente novamente!')
