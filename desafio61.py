'''print('===== DESAFIO 61 =====')
i = int(input('Digite o INÍCIO da Progressão Aritimética: '))
r = int(input('Digite a RAZÃO da Progrressão Aritimética: '))
c = 0
while c != 10:
    i += r
    c += 1
    print(i)
print('FIM!')
'''

# Solução do professor:

print('GERADOR DE P.A.')
print('-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da P.A.: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f' {termo} --> ', end='')
    termo += razao
    cont += 1
print('FIM')
