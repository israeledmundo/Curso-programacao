from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente:'))
#h = (co**2 + ca**2)**(1/2)
#print('o comprimento da hipotenusa é de {:.2f}'.format(h))
h = hypot(co,ca)
print('O comprimento da hipotenusa é de {:.2f}'.format(h))