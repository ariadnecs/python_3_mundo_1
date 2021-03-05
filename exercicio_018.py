# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
an = float(input('Digite um ângulo qualquer em graus: '))
s = sin(radians(an)) # tem q converter de graus para radianos!
c = cos(radians(an))
t = tan(radians(an))
print('O ângulo digitado foi {}º, \no valor do seno é {:.2f}, \ndo cosseno é {:.2f}, \ne da tangente é {:.2f}.'.format(an, s, c, t))