from random import randrange
from time import sleep
print('===== DESAFIO 28 =====')
print('Estou pensando um número inteiro entre 0 e 5, você consegue adivinhar qual número eu pensei?')
n = randrange(0, 5)
num = int(input('Digite o número que você acha que o computador escolheu: '))
print('PROCESSANDO...')
sleep(3)
if num == n:
    print('Você acertou! Parabéns!')
else:
    print('Não foi dessa vez! Tente novamente!')
