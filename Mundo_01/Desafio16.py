#import math
#n = float(input('Digite um número: '))
#print('A porção inteira deste número é {}'.format(math.trunc(n)))
from math import trunc
n = float(input('Digite um número:'))
print('A porção inteira do número {} é {}.'.format(n, trunc(n)))
