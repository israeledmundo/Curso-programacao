#coding: UTF-8

from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('-=-=-=-= O que deseja fazer? -=-=-=-=')
    print('[ 1 ] Somar \n[ 2 ] Multiplicar \n[ 3 ] Saber o maior \n[ 4 ] Novos números \n[ 5 ] Sair do programa')
    opcao = int(input('Qual é a sua opção?' ))
    if opcao == 1:
        soma = v1 + v2
        print('\033[1;30mA soma de {} + {} é igual a {}.\033[m'.format(v1,v2,soma))
    elif opcao == 2:
        multip = v1 * v2
        print('\033[1;30mA multiplicação de {} vezes {} é igual a {}.\033[m'.format(v1,v2,multip))
    elif opcao == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('\033[1;30mEntre {} e {} o maior valor é {}.\033[m'.format(v1,v2,maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('\033[1;33mFinalizando...\033[m')

    else:
        print('\033[1;31mOpção inválida, tente outra vez.\033[m')
    sleep(2)

print('\033[1;32mFim do programa.\033[m')
