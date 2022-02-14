print('===== DESAFIO 69 =====')
maiorid = homem = mulher = 0
while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA     ')
    print('-' * 30)
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()
    continua = ' '
    while continua not in 'SN':
        continua = str(input('QUER CONTINUAR? [S/N]: ')).strip().upper()
    if idade >= 18:
        maiorid += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade <= 20:
        mulher += 1
    if continua == 'N':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {maiorid}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'Temos {mulher} mulheres com menos de 20 anos de idade')
