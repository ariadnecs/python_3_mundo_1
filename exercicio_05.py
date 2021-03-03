# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número inteiro: '))
#a = n - 1
#s = n + 1
#print('Você digitou {}. \nSeu antecessor é {} e seu sucessor é {}.'.format(n, a, s))
print('Você digitou {}. \nSeu antecessor é {} e seu sucessor é {}.'.format(n, n-1, n+1))