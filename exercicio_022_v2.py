# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras no total sem considerar espaços. Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome: ')).strip() #a variável ficará guardada sem os espaços excedentes no início e no fim
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))# contagem do nome len() - espaços encontrados
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
