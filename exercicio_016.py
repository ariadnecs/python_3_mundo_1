#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import floor
#from math import trunc
n = float(input('Digite um número real: '))
nf = floor(n)
#nt = trunc(n)
# seria possivel resolver da seguinte maneira tb
#print('A porção inteira do número {} é {}.'.format(n, int(n)))
#print('A porção inteira do número {} é {}.'.format(n, nt))
print('A porção inteira do número {} é {}.'.format(n, nf))