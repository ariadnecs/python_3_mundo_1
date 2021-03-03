# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
#aqui iremos trabalhar com métodos de teste de tipo
v = input('Digite algo:')
print('Você digitou um número?', v.isnumeric())
print('São números entre 0 e 9?', v.isdigit())
print('Um texto ou número?', v.isalnum())
print('Você digitou alguma letra/palavra?', v.isalpha())
print('O que você digitou tem somente letras maiúsculas?', v.isupper())
print('O que você digitou tem somente letras minúsculas?', v.islower())
print('É um título (capitalizada)?', v.istitle())
print('É um espaço???', v.isspace())
print('O tipo primitivo digitado é:', type(v)) #aqui sempre vai mostrar string, acho...
