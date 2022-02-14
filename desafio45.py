from random import choice
from time import sleep
print('===== DESAFIO 45 =====')
print('VAMOS JOGAR JOKENPÔ!')
print('Estou escolhendo entre PEDRA, PAPEL OU TESOURA. Você consegue me vencer?')
computador = ["PEDRA", "PAPEL", "TESOURA"]
jogador = str(input('Digite sua jogada: '))
jok = choice(computador)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print(f'Eu joguei {jok}')
print(f'Você jogou {jogador}')
if jok == "PEDRA" and jogador == "TESOURA":
    print('Eu GANHEI! Jogue novamente!')
elif jok == "TESOURA" and jogador == "PAPEL":
    print('Eu GANHEI! Jogue novamente!')
elif jok == "PAPEL" and jogador == "PEDRA":
    print('Eu GANHEI! Jogue novamente!')
elif jogador == "PEDRA" and jok == "TESOURA":
    print('Parabéns, você GANHOU! Quero revanche!')
elif jogador == "TESOURA" and jok == "PAPEL":
    print('Parabéns, você GANHOU! Quero revanche!')
elif jogador == "PAPEL" and jok == "PEDRA":
    print('Parabéns, você GANHOU! Quero revanche!')
elif jogador == jok:
    print('EMPATAMOS! Vamos jogar de novo!')
else:
    print('ERRO! Você não escolheu uma opção válida! Tente novamente!')
