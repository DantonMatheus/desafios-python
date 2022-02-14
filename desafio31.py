print('===== DESAFIO 31 =====')
viagem = float(input('Digite a distância em Km da sua viagem: '))
if viagem <= 200:
    print(f'O custo da sua viagem será R$ {viagem * 0.5}')
else:
    print(f'O custo da sua viagem será R$ {viagem * 0.45}')
