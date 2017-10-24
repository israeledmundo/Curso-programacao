#coding: utf-8

s = 0
for c in range(1, 501):
    if c % 3 == 0:
        s += c
print('A soma dos números múltiplos de 3 entre 1 e 500 é {}.'.format(s))


