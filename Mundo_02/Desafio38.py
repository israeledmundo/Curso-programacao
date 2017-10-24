v1 = int(input('Digite um valor: '))
v2 = int(input('Digite um outro valor:'))
cores = {'limpa':'\033[m',
         'amarelo':'\033[1;33m',
         'verde':'\033[1;32m',
         'branco':'\033[1;30m'}
if v1 > v2:
    print('O {}PRIMEIRO\033[m valor é maior!'.format(cores['amarelo']))
elif v1 < v2:
    print('O {}SEGUNDO\033[m valor é maior!'.format(cores['verde']))
else:
    print('Não existe valor maior, os dois são {}IGUAIS!'.format(cores['branco']))