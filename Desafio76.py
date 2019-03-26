listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25.0, 'Transferidor', 4.20, 'Compasso', 9.99,'Mochila', 120.39)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for posicao in range(0,len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}',end='')
    else:
        print(f'R${listagem[posicao]:>7.2f}')
print('-'*40)