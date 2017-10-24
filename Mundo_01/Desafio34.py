salario = float(input('Qual é o salário do funcionário? R$ '))
if salario >= 1250:
    reajuste = salario + (salario * 10 / 100)
else:
    reajuste = salario + (salario * 15 / 100)
print('O funcionário ganhava {} e passará a ganhar {}'.format(salario, reajuste))