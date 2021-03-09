# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número inteiro: '))
if num % 2 == 1:
    print('{} é um número ímpar!'.format(num))
else:
    print('{} é um número par!'.format(num))