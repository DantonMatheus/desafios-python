print('===== DESAFIO 67 =====')
n = 0
while True:
    n = int(input('Digite qual valor você quer ver a tabuada: '))
    print('-' * 50)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 50)
print('PROGRAMA TABUADA ENCERRADO!')
