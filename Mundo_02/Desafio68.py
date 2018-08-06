#coding: UTF-8

from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')


cont = soma = 0
computador = randint(0,10)

while True:
    print('=-' * 15)
    jogador = int(input('Diga um valor: '))
    opcao = str(input('Par ou Ímpar? [P/I]')).upper().split()[0]
    result = (jogador + computador) % 2
    soma = jogador + computador
    cont = cont +1
    print('-' * 20)
    if result == 1:
        print(f'Você colocou {jogador} e o computador colocou {computador}. Total {soma}, DEU ÍMPAR!')
        if opcao in 'Pp':
            print('Você PERDEU!!')
            print(f'GAME OVER! Você venceu {cont} vezes.')
            break
        elif opcao in 'Im':
            print('Você GANHOU')
    else:
        print(f'Você colocou {jogador} e o computador colocou {computador}. Total {soma}, DEU PAR!')
        if opcao in 'Pp':
            print('Você GANHOU!!')
        elif opcao in 'Im':
            print('Você PERDEU')
            print('GAME OVER! Você venceu {cont} vezes.')
            break





