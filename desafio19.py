from random import choice
print('===== DESAFIO 19 =====')
aluno1 = str(input('Digite o nome do Primeiro Aluno: '))
aluno2 = str(input('Digite o nome do Segundo Aluno: '))
aluno3 = str(input('Digite o nome do Terceiro Aluno: '))
aluno4 = str(input('Digite o nome do Quarto Aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
print(f'O aluno escolhido foi {choice(lista)}')
