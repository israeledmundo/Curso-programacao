from time import sleep
import emoji
print('Contagem regressiva em...')
sleep(1)
for c in range(10, 0, -1):

    print(c)
    sleep(1)
print(emoji.emojize(':fireworks:' ' ' ':sparkler:' * 5))
print('BUUMM!! FELIZ ANO NOVO')
