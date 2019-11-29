from time import sleep
def maior(*num):
    cont = maior = 0
    print('-=' * 30, end='')
    sleep(2)
    print('Analisando valores passados...')
    for v in num:
        print(f'{v} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont = cont + 1
    print(f'Foram os valores informados. {cont} valores ao todo;')
    print(f'O maior valor informado foi {maior}')
    print()

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
