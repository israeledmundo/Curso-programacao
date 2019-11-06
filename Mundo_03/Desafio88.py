from random import randint
from time import sleep
lista = []
jog = []
print('-'* 30)
print('    JOGOS DA MEGA SENA    ')
print('-'* 30)
jogos = int(input('Quantos jogos você deseja fazer? '))
tot = 1

while tot <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break

    lista.sort()
    jog.append(lista[:])
    lista.clear()
    tot = tot + 1
print('-='*3, f' SORTEANDO {jogos} JOGOS...', '-='*3)
sleep(1)
for i, l in enumerate(jog):
    print(f'O Jogo {i+1}: {l}')
    sleep(1)
print('='*12, 'BOA SORTE!!', '='*12)
