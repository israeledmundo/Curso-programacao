list =[]
#mai = 0
#men = 0
for c in range(0,5):
    list.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = list[c]
    else:
        if list[c] > mai:
            mai = list[c]
        if list[c] < men:
            men = list[c]

print(f'Você digitou os valores {list}')
print(f'O maior valor digitado é {mai} nas posições ', end='')
for i, v in enumerate(list):
    if v == mai:
        print(f'{i}...',end='')
print()
print(f'O menor valor digitado é {men} nas posições ',end='')
for i, v in enumerate(list):
    if v == men:
        print(f'{i}...',end='')
print()