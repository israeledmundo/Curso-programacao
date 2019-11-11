from datetime import datetime
data = datetime.now().year
info = {}
info['Nome'] = str(input('Nome: '))
info['Idade'] = data - int(input('Ano de Nascimento: '))
info['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if info['CTPS'] != 0:
    info['Contratação'] = int(input('Ano de contratação: '))
    info['Salário'] = float(input('Salário R$: '))
    info['Aposentadoria'] = info['Idade'] + ((info['Contratação'] + 35) - data)
print('=-'*30)
for k, v in info.items():
    print(f'{k} tem o valor {v}')
