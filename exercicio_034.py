# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Qual é o valor do seu salário? R$ '))
print('O salário digitado foi R${}.'.format(sal))
if sal > 1250:
    aum = (sal * (10/100)) + sal
else:
    aum = (sal * (15/100)) + sal
print('Seu salário atual é de R${}.'.format(aum))