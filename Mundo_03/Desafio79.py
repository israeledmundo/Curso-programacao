list = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in list:
        print('Valor duplicado, valor NÃO adiconado!!!')
    else:
        list.append(valor)
        print('Valor adicionado com SUCESSO!!')
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if resp == 'N':
        break
print('-='*30)
print(f'Você digitou os valores {sorted(list)}')
