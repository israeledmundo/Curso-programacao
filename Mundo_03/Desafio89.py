ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    resp = str(input('Deseja continuar?[S/N]: '))
    if resp in 'Nn':
        break
print('-='* 20)
print(f'{"Nº":<5}{"NOME":<10}{"MÉDIA":>10}')
print('-'*30)
for i,n in enumerate(ficha):
    print(f'{i:<5} {n[0]:.<10} {n[2]:>8.1f}')
print('-'*30)
while True:
    opc = int(input('Deseja mostrar a nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO....')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
