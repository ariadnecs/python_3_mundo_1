#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
#import random
from random import choice
a1 = input('Nome da(o) primeira(o) aluna(o): ')
a2 = input('Nome da(o) segunda(o) aluna(o): ')
a3 = input('Nome da(o) terceira(o) aluna(o); ')
a4 = input('Nome da(o) quarta(o) aluna(o): ')
lista = [a1, a2, a3, a4]
#escolhida = random.choice(lista)
escolhida = choice(lista)
print('A aluna sorteada foi {}!'.format(escolhida))
