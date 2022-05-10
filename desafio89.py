print('===== DESAFIO 89 =====')
boletim = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 01: '))
    nota2 = float(input('Nota 02: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continua in 'N':
        break
print('=-' * 20)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('--' * 20)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.2f}')
while True:
    print('--' * 20)
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        print('FINALIZANDO...')
        break
    if aluno <= len(boletim) - 1:
        print(f'Notas de {boletim[aluno][0]} são {boletim[aluno][1]}')
print('<<< VOLTE SEMPRE >>>')
