print('===== DESAFIO 43 =====')
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura * altura)
if imc <= 18.5:
    print(f'Seu IMC é {imc:.2f} e sua classificação é ABAIXO DO PESO IDEAL!')
elif imc >= 18.6 and imc <= 25:
    print(f'Seu IMC é {imc:.2f} e sua classificação é PESO IDEAL!')
elif imc >= 25.1 and imc <= 30:
    print(f'Seu IMC é {imc:.2f} e sua classificação é SOBREPESO!')
elif imc >= 30.1 and imc <= 40:
    print(f'Seu IMC é {imc:.2f} e sua classificação é OBESIDADE!')
else:
    print(f'Seu IMC é {imc:.2f} e sua classificação é OBESIDADE MÓRBIDA!')
