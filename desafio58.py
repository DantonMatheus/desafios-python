from random import randrange
print('===== DESAFIO 58 =====')
print('Estou pensando em um número interio entre 0 e 10, você consegue adivinhar em qual eu pensei?')
n = randrange(0, 10)
num = -1
tot = 0
while num != n:
    num = int(input('Digite aqui o seu palpite: '))
    tot += 1
    if num == n:
        print('PARABÉNS! VOCÊ ACERTOU')
        print(f'Eu escolhi o número {n}, você escolheu o número {num} e levou {tot} tentativas!')


# Solução do professor:

'''from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar um número entre 0 e 10')
print('Você consegue adivinhar?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Digite aqui seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente!')
        elif jogador > computador:
            print('Menos... Tente novamente!')
print(f'Acertou com {palpite} tentativas. Parabéns!')'''

