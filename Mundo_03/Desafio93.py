info = {}
partidas = []
info['Nome'] = str(input('Nome do jogador: '))
tot = int(input('Quantas partidas: '))
for g in range(0,tot):
    partidas.append(int(input(f'Quantos gols na partida {g+1}: ')))
info['Gols'] = partidas[:]
info['Total'] = sum(partidas)
print('=-'*30)
for k, v in info.items():
    print(f' O campo {k} tem valor {v}.')
print('=-'*30)
print(f'O jogador {info["Nome"]} jogou {len(info["Gols"])} partidas.')
for i, v in enumerate(info['Gols']):
    print(f'    => Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {info["Total"]} gols.')
