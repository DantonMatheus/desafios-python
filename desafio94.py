print('===== DESAFIO 94 =====')
cadastro = []
pessoa = {}
somaid = 0
fem = []
acimaid = []
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F!')
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    pessoa['idade'] = int(input('Idade: '))
    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while continua not in 'SN':
        print('ERRO! Por favor, digite apenas S ou N')
        continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
    cadastro.append(pessoa.copy())
    somaid = (somaid + pessoa['idade'])
    if pessoa['sexo'] == 'F':
        fem.append(pessoa['nome'])
    if continua == 'N':
        break
print('=-' * 20)
mediaid = somaid / len(cadastro)
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')
print(f'B) A média de idade é de {mediaid:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for v in fem:
    print(v, ';', end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for p in cadastro:
    if p['idade'] >= mediaid:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<  ENCERRADO  >>')
