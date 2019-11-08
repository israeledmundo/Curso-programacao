aluno = {}

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {"nome"}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} do aluno é {v}')
