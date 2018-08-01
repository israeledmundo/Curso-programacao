#coding: UTF-8

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} '.format(termo), end='-> ')
    termo = termo + razão
    cont = cont +1

print('ACABOU')
