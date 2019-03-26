from random import randint

num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Eu sorteei os valores: ', end='')
for n in num:
    print(f'{n} ',end='')
print(f'\nO MAIOR valor sorteado foi {max(num)}.')
print(f'O MENOR valor sorteado foi {min(num)}.')