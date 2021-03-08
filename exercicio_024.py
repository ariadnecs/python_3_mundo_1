# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
city = str(input('Digite o nome de uma cidade: '))
cidade = city.strip()
cidade1 = cidade.upper()
print('Nome da cidade: {}.'.format(cidade1))
print('A cidade que vc digitou inicia com a palavra *Santo*? {}'.format('SANTO' in cidade1))
