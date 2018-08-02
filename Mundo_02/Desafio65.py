#coding: UTF-8

resp = 'S'
'''soma = 0 #Soma dos valores digitados
quant = 0 #quantos números foram digitados
media = 0
maior = 0
menor = 0'''
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).strip()[0].upper()
media = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
