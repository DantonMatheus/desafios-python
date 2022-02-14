from datetime import date
print('===== DESAFIO 54 =====')
totmaior = 0
totmenor = 0
for c in range(1, 8):
    n = int(input(f'Digite o ano de nascimentod da {c}ª pessoa: '))
    idade = date.today().year - n
    if idade > 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Existem {totmaior} pessoas maiores de 21 anos de idade!')
print(f'Existem {totmenor} pessoas menores de 21 anos de idade!')
