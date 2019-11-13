pessoa = {}
galera = []
lista_feminina = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma = soma + pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar?[S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resp == 'N':
        break
print(galera)
print(f'O grupo tem {len(galera)} pessoas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos')
print('As mulheres cadastradas foram', end=' ')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}', end=', ')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['Idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
            print()
print('<<< ENCERRADO >>>')
