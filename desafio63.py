print('===== DESAFIO 63 =====')
print('SEQUÊNCIA DE FIBONACCI')
n = int(input('Digite quantos elementos você quer ver: '))
t1 = 0
t2 = 1
print(f'{t1} --> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' --> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' --> FIM')
