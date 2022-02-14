print('===== DESAFIO 62 =====')
print('GERADOR DE P.A.')
print('-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da P.A.: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f' {termo} --> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Digite quantos termos você quer mostrar a mais: '))
print(f'Progressão finalizada com {total} termos mostrados')
