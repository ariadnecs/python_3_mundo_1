# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
#from math import sqrt
#from math import pow
from math import hypot
co = float(input('Qual é o comprimento do cateto oposto? '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
# h = sqrt(pow(co, 2)+pow(ca, 2))
h = hypot(co, ca)
print('A hipotenusa de um triângulo retângulo \ncom os valores do cateto oposto equivalente a {:.2f} \ne do cateto ajacente a {:.2f} é de {:.2f}.'.format(co, ca, h))