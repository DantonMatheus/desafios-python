print('===== DESAFIO 42 =====')
l1 = float(input('Digite o comprimento da reta 01: '))
l2 = float(input('Digite o comprimento da reta 02: '))
l3 = float(input('Digite o comprimento da reta 03: '))
tri = (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2)
if tri is True:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')
if l1 == l2 and l2 == l3:
    print('Este triângulo é EQUILÁTERO!')
elif tri is True and (l1 != l2) and (l2 != l3) and (l1 != l3):
    print('Este triângulo é ESCALENO')
elif (l1 == l2) or (l1 == l3) or (l2 == l3):
    print('Este triângulo é ISÓSCELES')
