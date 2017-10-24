km = float(input('Qual é a distância da sua viagem?  '))
p1 = km * 0.5
p2 = km * 0.45
if km <= 200:
        print('Sua passagem irá custar R${:.2f}.'.format(p1))
else:
    print('Sua passagem irá custar R${:.2f}.'.format(p2))
print('Faça uma boa viagem!')