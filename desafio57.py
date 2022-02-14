print('===== DESAFIO 57 =====')
s = 'M'
while s != '':
    s = str(input('Qual seu sexo? [M/F]: ')).strip().upper()
    if s != 'F' and s != 'M':
        print('Opção Inválida! Digite novamente!')
    if s == 'F':
        print('Sexo FEMININO registrado com sucesso!')
    if s == 'M':
        print('Sexo MASCULINO registrado com sucesso!')


# Solução do Professor:
'''
sexo = str(input('informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos. Por favor, informe seu sexo: ')). strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
'''
