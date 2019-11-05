temp = []
princi = []
maior = 0
menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso:')))
    if len(princi) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princi.append(temp[:])
    temp.clear()

    perg = str(input('Deseja continuar? [S/N]: '))
    if perg in 'Nn':
        break
print('-='*20)
print(f'Ao todo, você cadastrou {len(princi)} pessoas.')
print(f'O maior peso foi {maior}Kg. Peso de ', end=' ')
for p in princi:
    if p[1] == maior:
        print(f'{p[0]}',end=' ')

print(f'O menor peso foi de {menor}Kg. Peso de ', end=' ')
for p in princi:
    if p[1] == menor:
        print(f'{p[0]}', end='')
