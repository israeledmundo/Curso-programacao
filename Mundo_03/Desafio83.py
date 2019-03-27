listaabre = []
listafecha = []
exp = str(input('Digite uma expressão: ')).strip()
for simb in exp:
    if simb == '(':
        listaabre.append('(')
    elif simb ==')':
        listafecha.append(')')
if len(listaabre) == len(listafecha):
    print('A expressão é VÁLIDA')
else:
    print('A expressão é INVÁLIDA')