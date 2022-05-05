print('===== DESAFIO 72 =====')
num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
       'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
       n = int(input('Digite um número entre 0 e 20: '))
       if 0 <= n <= 20:
              print(f'Você digitou o número {num[n]}')
              continua = ' '
              while continua not in 'SN':
                     continua = str(input('QUER CONTINUAR? [S/N]: ')).strip().upper()
              if continua == 'N':
                     break
       else:
              print('Tente novamente!')
