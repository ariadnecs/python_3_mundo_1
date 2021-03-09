# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
num = int(input('Digite um número inteiro entre 0 a 5 e tente adivinhar qual o número computador ecolheu: '))
numpc = randint(0, 5)
print(numpc)
if num == numpc:
    print('O computador escolheu o número {}. Parabéns, vocẽ venceu!'.format(numpc))
else:
    print('O computador esolheu o número {} e você escolheu o número {}. Tente novamente.'.format(numpc, num))
