#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número inteiro: '))
# d = n * 2
# t = n * 3
# r = n ** (1/2) #ou pow(n,1/2)
# print('O número digitado foi {}. \nO dobro vale {}. \nO triplo vale {}. \nA raiz quadrada vale {:.3f}.'.format(n, d, t, r))
print('O número digitado foi {}. \nO dobro deste número vale {}. \nO triplo de {} vale {}. \nA raiz quadrada de {} é {:.3f}.'.format(n, n*2, n, n*3, n, n**(1/2)))