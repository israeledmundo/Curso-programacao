cidade = str(input('Digite o nome de uma cidade: ')).upper()
separado = cidade.split()
id = separado[0]
p = 'SANTO' in id
print('Sua cidade começa com Santo? {}'.format(p))
