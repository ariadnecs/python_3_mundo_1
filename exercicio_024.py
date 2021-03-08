# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
city = str(input('Digite o nome de uma cidade: ')).strip()
cidade = city.upper()
print('Nome da cidade: {}.'.format(cidade))
print('A cidade que vc digitou inicia com a palavra *Santo*? {}'.format('SANTO' in cidade))
