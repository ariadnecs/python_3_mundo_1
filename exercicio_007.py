#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n0 = input('Digite o nome da(o) aluna(o): ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
#m = (n1+n2)/2
#print('A média da(o) aluna(o) {} é {:.1f}.'.format(n0, m))
print('Nota 1 = {} e nota 2 = {}. \nA média da(o) aluna(o) {} é {:.1f}.'.format(n1, n2, n0, (n1+n2)/2))