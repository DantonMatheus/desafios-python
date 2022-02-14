print('===== DESAFIO 29 =====')
vel = float(input('Qual é a velocidade do carro em Km/h? '))
if vel <= 80:
    print('Você está dentro do limite de velocidade e não foi multado!')
else:
    print(f'Você está acima do limite de velocidade e foi multado em R$ {(vel-80)*7}!')
