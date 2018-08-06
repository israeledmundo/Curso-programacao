#coding: UTF-8

cont = v = soma = 0
while True:
    v = int(input('Digite um valor (999 para parar): '))
    if v == 999:
        break
    soma = soma + v
    cont = cont +1
print(f'A soma dos {cont} valores foi {soma}!')
