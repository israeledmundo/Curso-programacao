#coding: UTF-8

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    nasc = int(input('Em que a no a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('Ao todo tivemos {} pessoas MAIORES de idade.'.format(totmaior))
print('E também tivemos {} pessoas MENORES de idade.'.format(totmenor))
