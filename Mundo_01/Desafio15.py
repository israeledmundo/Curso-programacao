d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados?' ))
da = d * 60
kmr = km * 0.15
print('O total a pagar é de R${}'.format(da+kmr))