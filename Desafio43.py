peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite sua altura (m)'))

imc = peso/altura**2
print('Seu IMC é de {:.2f}.'.format(imc))
if imc <= 18.5:
    print('Você está ABAIXO do peso!')
elif imc <= 25:
    print('Você está no peso IDEAL!')
elif imc <=30:
    print('Você está com SOBREPESO!')
elif imc <=40:
    print('Você está na faixa de OBESIDADE!')
else:
    print('Você vai morrer em breve, OBESIDADE MÓRBIDA!')