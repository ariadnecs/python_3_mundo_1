# Faça um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Mais um número inteiro '))
n3 = int(input('O último número inteiro: '))
print('Você digitou os números {}, {} e {}.'.format(n1, n2, n3))
maior = n1 # essa linha elimina um if para veriificar
menor = n3
if n2 >= n3 and n2 >= n1:
    maior = n2
elif n3 >= n2 and n3 >= n1:
    maior = n3
if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n3 and n2 <= n1:
    menor = n2
print('O maior número digitado foi {} e o menor número digitado foi {}.'.format(maior, menor))
