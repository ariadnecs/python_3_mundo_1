# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos km foram rodados? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
valor_dias = dias * 60
valor_km = km * 0.15
total = valor_km + valor_dias
print('O valor a pagar por {:.2f}km percorridos em {} dias é de R${:.2f}.'.format(km, dias, total))