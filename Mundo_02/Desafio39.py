from datetime import date

ano = int(input('Digite o ano do seu nascimento: '))
data = date.today().year
idade = data - ano

if idade > 18:
    print('Você passou o tempo de alistamento em {} anos!!'.format(idade - 18))
elif idade < 18:
    print('Você ainda vai se alistar, faltam(m) {} ano(s).'.format(18 - idade))
else:
    print('É hora de se alistar no serviço militar!!')
