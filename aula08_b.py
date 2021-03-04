#gerar números aleatŕios
import random
num1 = random.random() #gera um num aleatório entre 0 e 1
num2 = random.randint(1, 1000) #geram um num aleatório inteiro em um intervalo prederteminado
print('Um número aleatŕio entre 0 e 1: {:.5f}'.format(num1))
print('Um número aleatŕio inteiro: {}'.format(num2))