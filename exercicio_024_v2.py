#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cid = str(input('Digite o nome de uma cidade: ')).strip()
print('A cidade que você digitou inicia com a palavra Santo? {}'.format(cid[:5].upper() == 'SANTO'))
