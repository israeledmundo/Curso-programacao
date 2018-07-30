#coding: UTF-8

from random import randint
from time import sleep
computador = randint(0, 10)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?  '))
print('PROCESSANDO...')
sleep(2)
chances = 0
while jogador != computador:
    jogador = int(input('Você errou, tente outra vez: '))
    print('PROCESSANDO...')
    sleep(2)
    chances = chances+1
print('PARABÉNS! Você conseguiu me vencer, mas precisou de {} tentativas para isso!'.format(chances))
