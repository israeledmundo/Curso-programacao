#coding: utf-8

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1

if cont == 0:
    print('Você não digitou nenhum número par, sua soma é 0.')
elif cont == 1:
    print('Você digitou {} número par, é o número {}.'.format(cont, soma))
else:
    print('Você digitou {} números pares, a soma total deles é de {}.'.format(cont, soma))