times = ('Palmeiras', 'Flamengo','Internacional','Grêmio', 'São Paulo',
         'Atlético', 'Atlético-PR', 'cruzeiro', 'Botafogo','Santos',
         'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará',
         'Vasco', 'Sport', 'América', 'Vitória', 'Paraná')

print(f'Lista dos times do brasileirão: {times}')
print('=='*15)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('=='*15)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('=='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=='*15)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª  posição.')