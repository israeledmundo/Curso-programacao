lista = []
while True:
    lista.append(int(input('Digite um valor: ')))

    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
listapar = []
listaimpar = []
for v in lista:
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print(f'A lista completa digitada é: {lista}.')
print(f'A lista de números PARES é: {listapar}.')
print(f'A lista de números ÍMPARES é: {listaimpar}.')