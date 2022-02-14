from random import shuffle
print('===== DESAFIO 20 =====')
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem de apresentação será {lista}')
