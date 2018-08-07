#coding: UTF-8

contI = contH = contM = 0
while True:
    print("-" * 20)
    print('CADASTRE UMA PESSOA')
    print("-" * 20)
    idade = int(input('Idade: '))
    if idade > 18:
        contI = contI + 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo in 'M':
        contH = contH + 1
    elif sexo in 'F' and idade < 20:
        contM = contM + 1
    resp = ' '
    while resp not in 'SN':
        print("-" * 20)
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        print('{:=^40}'.format('FIM DO PROGRAMA'))
        break
print(f'Total de pessoas com mais de 18 anos: {contI}')
print(f'Ao todo temos {contH} homens cadastrados')
print(f'E temos {contM} mulheres com menos de 20 anos.')
