print('===== DESAFIO 22 =====')
nome = str(input('Digite seu nome Completo: ')).strip()
print(f'Seu nome com todas as letras maíusculas fica: {nome.upper()}')
print(f'Seu nome com todas as letras minúsculas fica: {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras')
