casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quanto anos de financiamento? '))
prestacao = casa / (anos * 12)
print ('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R$ {:.2f}.'.format(casa, anos, prestacao))
if prestacao <= ((salario*30)/100):
    print ('Empréstimo pode ser \033[1;32mCONCEDIDO!\033[m')
else:
    print ('O empréstimo foi \033[1;31mNEGADO!\033[m')


