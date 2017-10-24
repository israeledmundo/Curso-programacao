frase = str(input('Digite uma frase: ')).upper().strip()
qa = frase.count('A')
pp = frase.find('A')+1
up = frase.rfind('A')+1


print('A letra A aparece {} vezes na frase.'.format(qa))
print('A primeira letra A esta na posição {}.'.format(pp))
print('A ultima letra A esta na posição {}'.format(up))