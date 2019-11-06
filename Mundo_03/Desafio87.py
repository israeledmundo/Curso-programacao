matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
pares = 0
somacol = 0
maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Preencha o valor na posição [{l}, {c}]: '))
print('-='*20)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            pares = pares + matriz[l][c]
    print()
print('-='*20)
print(f'A soma dos valores pares é {pares}')
for l in range(0,3):
    somacol = somacol + matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somacol}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
