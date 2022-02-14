print('===== DESAFIO 66 =====')
n = s = c = 0
while True:
    n = int(input('Digite um número ou 999 para SAIR: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} números é {s}')
