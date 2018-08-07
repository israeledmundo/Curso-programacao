#coding: UTF-8

from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
cont = 0

while True:
    print('=-' * 15)
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar? [P/I]')).upper().split()[0]
    result = (jogador + computador) % 2
    print('-' * 20)
    if result == 1:
        print(f'Você colocou {jogador} e o computador colocou {computador}. Total {soma}, DEU ÍMPAR!')
        if opcao in 'Pp':
            print('Você PERDEU!!')
            print(f'GAME OVER! Você venceu {cont} vezes.')
            break
        elif opcao in 'Im':
            print('Você GANHOU\n'
                  'Vamos jogar novamente...')
            cont = cont + 1
    else:
        print(f'Você colocou {jogador} e o computador colocou {computador}. Total {soma}, DEU PAR!')
        if opcao in 'Pp':
            print('Você GANHOU!!\n'
                  'Vamos jogar novamente...')
            cont = cont + 1
        elif opcao in 'Im':
            print('Você PERDEU')
            print(f'GAME OVER! Você venceu {cont} vezes.')
            break
