from datetime import date
print('===== DESAFIO 39 =====')
nasc = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nasc
if idade < 18:
    print(f'Ainda não é hora de se alistar, faltam {18 - idade} anos!')
elif idade == 18:
    print('Está na hora de alistar, não perca o prazo!')
else:
    print(f'Já passou da hora de se alistar, você está {idade - 18} anos atrasado!')
