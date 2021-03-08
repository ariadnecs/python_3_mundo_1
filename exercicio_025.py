# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Digite seu nome completo: ')).strip().upper().split()# upper para padronizar a busca
#eu add o split para que o programa procurasse pela palavra 'silva' e não desse um falo positivo em nomes como 'silvana'
print('Você tem *Silva* em seu nome? {}'.format('SILVA' in nome[:]))