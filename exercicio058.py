# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
#  mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
print('-' * 45)
print('Adivinhe o número no qual estou pensando...')
print('-' * 45)

computer = randint(0, 10)
user = int(input('Digite um número entre 0 e 5: '))

print('Processando...')
sleep(1)
n = 1

while user != computer:
    sleep(1)
    print('Errou! \nEu escolhi o número {} e você o {}. \nTente novamente.'.format(computer, user))
    sleep(1)
    user = int(input('Digite um número entre 0 e 10: '))
    computer = randint(0, 10)
    n += 1

print('\nParabéns, você acertou! Nós escolhemos o número {}.\nVocê tentou acertar o número que eu escolhi {} vez(es).'.format(computer, n))