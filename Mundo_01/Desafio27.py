n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
#u = nome[len(nome)-1]
print('O primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))