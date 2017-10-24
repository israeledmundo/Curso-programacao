n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('Sua média foi {}, você foi \033[1;31m REPROVADO!!!'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi {}, você ficou de \033[1;33mRECUPERAÇÃO.'.format(media))
else:
    print('Parabéns, sua média foi {} e você foi \033[1;32mAPROVADO!'.format(media))
