print('===== DESAFIO 96 =====')
print(' CONTROLE DE TERRENOS')
print('--' * 11)

def area(a, b):
    mult = a * b
    print(f'A área de um terreno {a} x {b} é de {mult:.2f} m2.')


area(a=float(input('LARGURA (m): ')),
b=float(input('COMPRIMENTO (m): ')))
