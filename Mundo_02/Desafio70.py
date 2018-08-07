#coding: UTF-8

soma = cont1000 = menor = contmenor = 0
barato = ' '
print('-'*30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-'*30)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    resp = ' '
    contmenor = contmenor + 1
    if preco > 1000:
        cont1000 = cont1000 + 1
    if contmenor == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    soma = soma + preco
    print('-' * 40)
    while resp not in 'SN':
        resp = str(input('Quer contiuar? [S/N] ')).strip().upper()[0]

    if resp in 'N':
        print('{:-^40}'.format('FIM DO PROGRAMA'))
        break

print(f'O total da compra foi R${soma:.2f}.')
print(f'Temos {cont1000} produtos custando mais de R$1000.')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}.')
