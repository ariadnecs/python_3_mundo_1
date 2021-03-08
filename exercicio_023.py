# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('Digite um número inteiro entre 0 e 9999: '))
u = num // 1 % 10#divisão inteira por 1 e resto da divisão / 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Você digitou {}.'.format(num))
print('A unidade é {}.'.format(u))
print('A dezena é {:>2}.'.format(d))
print('A centena é {}.'.format(c))
print('O milhar é {:>2}.'.format(m))
