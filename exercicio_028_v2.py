# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('-=-' * 20)
print('  Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
numusr = int(input('Em que número eu pensei? '))
numpc = randint(0, 5)
print('PROCESSANDO...')
sleep(2) # irá demorar 2 segundos para mostrar o resultado
if numusr != numpc:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(numpc, numusr))
else:
    print('PARABÉNS!!! Você conseguiu me vencer. Eu e você escolhemos o número {}.'.format(numpc))
