#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-' * 9, '\n Analisador de triângulos')
print('-=-' * 9)
r1 = float(input('Digite o valor do primeiro segmento de reta: '))
r2 = float(input('Digite o valor do segundo segmento de reta: '))
r3 = float(input('Digite o valor do terceiro segmento de reta: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('\nÉ possível formar um triângulo com os seguintes \nvalores de segmento de reta: {}, {} e {}.'.format(r1, r2, r3))
else:
    print('\nNão é possível formar um triângulos com os \nsegmentos de reta {}, {} e {}.'.format(r1, r2, r3))