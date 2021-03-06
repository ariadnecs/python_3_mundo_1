# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import sample, shuffle
a1 = input('Nome da aluna: ')
a2 = input('Nome da aluna: ')
a3 = input('Nome da aluna: ')
a4 = input('Nome da aluna: ')
lista = [a1, a2, a3, a4]
#ordem = sample(lista,4)
ordem1 = shuffle(lista)
#print('A ordem de apresentação será: \n{}'.format(ordem))
print('A ordem de apresentação será:')
print(lista)
