p = float(input('Quanto custa o produto? R$'))
d = ((p*5)/100)
vf = p-d
print('Com 5% de desconto você irá pagar R${:.2f}'.format(vf))