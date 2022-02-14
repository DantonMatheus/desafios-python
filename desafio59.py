print('===== DESAFIO 59 =====')
menu = 0
n1 = int(input('Digite o 1º número inteiro: '))
n2 = int(input('Digite o 2º número interio: '))
while menu != '':
    menu = int(input('''===== MENU =====
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR VALOR
    [4] NOVOS NÚMEROS
    [5] SAIR
    Digite aqui sua opção: '''))
    if menu == 1:
        print(f'O número {n1} SOMADO ao número {n2} é igual a {n1 + n2}')
    elif menu == 2:
        print(f'O número {n1} MULTIPLICADO ao número {n2} é igual a {n1 * n2}')
    elif menu == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'O maior valor entre {n1} e {n2} é {maior}')
    elif menu == 4:
        n1 = int(input('Digite o 1º número inteiro: '))
        n2 = int(input('Digite o 2º número interio: '))
    elif menu == 5:
        menu = ''
    else:
        print('Digite um OPÇÃO VÁLIDA!')
print('FIM!')
