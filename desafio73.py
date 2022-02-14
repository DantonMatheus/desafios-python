print('===== DESAFIO 73 =====')
br = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
      'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio',
      'Bahia', 'Sport Recife', 'Chapecoense')
print(f'Os 5 PRIMEIROS colocados no Brasileirão 2021 foram: {br[0:5]}')
print(f'Os 4 ÚLTIMOS colocador no Brasileirão 2021 foram: {br[16:20]}')
print(f'Os times do Brasileirão 2021 em ORDEM ALFABÉTICA: {sorted(br)}')
print(f"Meu time {br[13]} ficou na {br.index('Athletico-PR') + 1}ª posição no Brasileirão 2021")
