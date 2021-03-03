# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Valor do salário: '))
aum = float(input('Valor do aumento em porcentagem: '))
prcaum = aum / 100
valor_aum = sal * prcaum
novo_sal = sal + valor_aum
print('O salário do funcionário era de R${:.2f}, com o aumento de {}% o salário do funcionário passa a ser R${:.2f}.'.format(sal, aum, novo_sal))
