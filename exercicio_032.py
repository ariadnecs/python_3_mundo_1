#  Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Digite o ano que deseja saber se é bissexto: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))
