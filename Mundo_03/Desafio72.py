# encoding: utf-8
cont = ('zero', 'um', 'dois', "tres","quatro",
        "cinco","seis","sete","oito","nove","dez")

while True:
    num = int(input('Digite um número entre 0 e 10: '))
    if 0 <= num <= 10:
        break
    print('Tente novamente.', end='')
print(f'Você digitou o número {cont[num]}')

while True:
    conti = str(input('Você quer continuar? [S/N]: ')).upper()
    if conti == 'S':
        num1 = int(input('Digite um número entre 0 e 10: '))
        print(f'Você digitou o número {cont[num1]}')
    elif conti == 'N':
        break