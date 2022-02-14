print('===== DESAFIO 51 =====')
i = int(input('Digite o INÍCIO da Progressão Aritimética: '))
r = int(input('Digite a RAZÃO da Progrressão Aritimética: '))
d = i + (10-1) * r
for c in range(i, d + r, r):
    print(c)
print('FIM!')
