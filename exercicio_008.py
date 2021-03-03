#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite uma distância em metros: '))
#cm = m * 100
#mm = m * 1000
#print('A distância digitada foi {}m. \nEla equivale a {:.2f}cm e a {:.2f}mm.'.format(m, cm, mm))
print('A distância digitada foi {}m. \nEla equivale a {:.2f}cm e a {:.2f}'.format(m, m * 100, m * 1000))
