from random import randrange
print('===== DESAFIO 68 =====')
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
jog = c = tot = 0
teste = 'P'
while True:
    comp = randrange(0, 10)
    jog = int(input('Digite um valor: '))
    teste = str(input('PAR ou ÍMPAR? [P/I]: ')).strip().upper()
    tot = jog + comp
    print(f'Você jogou {jog} e o computador {comp}. Total de {tot}')
    if tot % 2 == 1 and teste == 'I':
        print('DEU ÍMPAR! Você VENCEU! VAMOS JOGAR NOVAMENTE...')
        print('-=' * 20)
        c += 1
    if tot % 2 == 0 and teste == 'P':
        print('DEU PAR! VOCÊ VENCEU! VAMOS JOGAR NOVAMENTE...')
        print('-=' * 20)
        c += 1
    if tot % 2 == 1 and teste == 'P':
        print('VOCÊ PERDEU!')
        break
    if tot % 2 == 0 and teste == 'I':
        print('VOCÊ PERDEU!')
        break
print(f'GAME OVER! VOCÊ VENCEU {c} VEZES!')
