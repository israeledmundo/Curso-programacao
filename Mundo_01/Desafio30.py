num = int(input('\033[1;31mDigite um número qualquer:\033[m ')  )
resultado = num % 2
if resultado == 1:
    print('O número {} é um número {}IMPAR{}'.format(num, '\033[1;32m','\033[m'))
else:
    print('O número {} é um número {}PAR{}'.format(num, '\033[1;32m', '\033[m'))