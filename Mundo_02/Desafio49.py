#coding: utf-8

n = int(input('Digite um número para saber sua tabuada: '))

print('\033[1;31;40mA tabuada de {} é:\033[m '.format(n))
print('='*12)
for c in range(1, 11):
        print('{} x {} = {} '.format(n, c, n*c))
print('='*12)