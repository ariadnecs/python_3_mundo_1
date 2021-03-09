# Faça um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Mais um número inteiro '))
n3 = int(input('O último número inteiro: '))
print('Você digitou os números {}, {} e {}'.format(n1, n2, n3))
if n1 >= n2 and n1 >= n3:
    maior = n1
    if n3 <= n2:
       menor = n3
    else:
        menor = n2
elif n2 >= n1  and n2 >= n3:
    maior = n2
    if n1 <= n3:
        menor = n1
    else:
        menor = n3
else:
    maior = n3
    if n2 <= n1:
        menor = n2
    else:
        menor = n1
print('O maior número digitado foi {} e o menor número digitado foi {}.'.format(maior, menor))