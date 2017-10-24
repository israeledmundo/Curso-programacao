from datetime import date
from time import sleep
ano = int(input('Qual ano você quer analisar? Digite 0 se for o ano atual:'))
print('ANALISANDO...')
if ano == 0:
    ano = date.today().year
sleep(1)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO.'.format(ano))