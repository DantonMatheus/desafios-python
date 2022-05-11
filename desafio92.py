print('===== DESAFIO 92 =====')
from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = datetime.now().year - int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contr'] = int(input('Ano de Contratação: '))
    pessoa['sal'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contr'] + 35) - datetime.now().year)
print('=-' * 20)
for i, v in pessoa.items():
    print(f'  - {i} tem o valor {v}')
