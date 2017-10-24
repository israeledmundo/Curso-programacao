velo = int(input('Qual a velocidade atual do carro?  '))
multa = (velo-80)*7

if velo > 80:
    print('MULTADO!! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de R${}!'.format(multa))

print('Tenha um bom dia! Dirija com segurança!')