print('===== DESAFIO 90 =====')
aprov = {}
aprov['nome'] = str(input('Nome: '))
aprov['media'] = float(input(f'Média de {aprov["nome"]}: '))
print(f'Nome é igual a {aprov["nome"]}')
print(f'Média é igual a {aprov["media"]}')
if aprov['media'] >= 7:
    print('Situação é igual a APROVADO')
else:
    print('Situação é igual a REPROVADO')
