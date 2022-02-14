print('===== DESAFIO 35 =====')
r1 = float(input('Digite o comprimento da reta 01: '))
r2 = float(input('Digite o comprimento da reta 02: '))
r3 = float(input('Digite o comprimento da reta 03: '))
if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')
