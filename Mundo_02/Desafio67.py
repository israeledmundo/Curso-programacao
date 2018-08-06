#coding: UTF-8

while True:

    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if num < 0:
        print('PROGRAMA DE TABUADA ENCERRADO.')
        break

    for c in range(1,11):
        tab = num * c
        print(f'{num} x {c} = {tab}')
    print('-' * 40)
