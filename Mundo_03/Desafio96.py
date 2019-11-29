def area(a,b):
    area = a * b
    print(f'A área de um terreno de {a}x{b} é de {area}m².')


print('Controle de Terreno')
print('-'*20)
larg = float(input('LARGURA (m): '))
compr = float(input('COMPRIMENTO (m): '))
area(larg,compr)
