#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
lar = float(input('Qual é a largura da parede, em metros? '))
alt = float(input('Qual é a altura da parede, em metros? '))
area = lar * alt
lit = area / 2
print('Para pintar uma parede de {:.2f}m² será necessário utilizar {:.2f}L de tinta.'.format(area, lit))
