#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().upper() #upper para padronizar a busca, poderia ser lower tb
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
#print('A letra "A" aparece pela primeira vez na posição {}\ne pela útilma vez na posição {}.'.format(frase.find('A'), frase.rfind('A')))
print('A letra "A" aparece pela primeira vez na posição {}.'.format(frase.find('A') + 1))# nesse caso eu adiciono 1 à posição pois o pyhton inicia a contagem a partir do zero
print('"A" aparece pela última vez na posição {}.' .format(frase.rfind('A') + 1))