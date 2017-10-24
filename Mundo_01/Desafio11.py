la = float(input('Digite a largura da parede em metros:'))
al = float(input('Digite a altura da parede em metros:'))
a = al*al
print('Para sua parede de {}m² você precisará de {.:2f} litros de tinta.'.format(a, (a/2)))