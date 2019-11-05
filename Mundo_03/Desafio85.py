lista = [[],[]]
for v in range(0,7):
    valor = int(input(f'Digite o {v+1}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        if valor % 2 == 1:
            lista[1].append(valor)
print(f'Os valores digitados pares foram: {sorted(lista[0])}')
print(f'Os valores digitados ímpares foram: {sorted(lista[1])})')
