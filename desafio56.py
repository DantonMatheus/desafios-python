print('===== DESAFIO 56 =====')
totid = 0
totm = 0
older = 0
nolder = ''
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = (str(input('NOME: '))).strip().upper()
    idade = (int(input('IDADE: ')))
    sexo = (str(input('SEXO [M/F]: '))).strip().upper()
    totid += idade
    if sexo == 'F' and idade <= 20:
        totm += 1
    if sexo == 'M' and idade > older:
        older = idade
        nolder = nome
print(f'A média de IDADE do grupo é de {totid / c} anos')
print(f'O homem mais velho tem {older} anos e se chama {nolder}')
print(f'Ao todo são {totm} mulheres com menos de 20 anos')
