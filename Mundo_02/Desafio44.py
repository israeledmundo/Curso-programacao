from time import sleep

valor = float(input('Digite o valor do produto: R$ '))
pag = int(input('            \033[7m OPÇÕES DE PAGAMENTO:\033[m' 
                '\n[1] Pagamento à vista no dinheiro/cheque;'
                '\n[2] Pagamento à vista no cartão;'
                '\n[3] Pagamento em até 2x no cartão;'
                '\n[4] Pagamento em 3x ou mais no cartão.'
                '\n\033[1;33m Digite a opção de pagamento: \033[m'))

pg1 = valor - (valor*10/100)
pg2 = valor - (valor*5/100)
pg3 = valor
pg4 = valor + (valor*20/100)

print('ANALISANDO...')
sleep(1)

if pag == 1:
    print('\nNo dinheiro/cheque ganhar um desconto de 10% no produto, valor final é \033[1;32mR${:.0f}\033[m.'.format(pg1))
elif pag == 2:
    print('\nNo cartão, você terá um desconto de 5%, o valor final do produto é de \033[1;32mR${:.0f}\033[m'.format(pg2))
elif pag == 3:
    print('\nPagamento em 2x no cartão, o valor final do produto é de \033[1;32mR${:.0f}\033[m'.format(pg3))
elif pag == 4:
    print('\nPagamento em 3x ou mais no cartão, o valor final do produto é de \033[1;32mR${:.0f}\033[m'.format(pg4))
else:
    print('\n\033[1;31m\033[mOpção inválida, tente novamente.')

