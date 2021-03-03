#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
cel = float(input('Temperatura em Celsius: '))
far = 1.8 * cel + 32
#far = ((9 * cel) / 5) + 32
print('{:.2f}ºC equivalem a {:.2f}ºF'.format(cel, far))
