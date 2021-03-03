#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
#p = float(input('Preço do produto: R$'))
#v = p * 0.05
#d = p * 0.95
#print('O preço do produto era de R${:.2f}. \nO valor do desconto é de R${:.2f}. \nO valor do produto com o desconto é de R${:.2f}.'.format(p, v, d))

# é possível fazer algo mais genérico
p = float(input('Preço do produto: R$'))
desc = int(input('Qual é a porcentagem do desconto? '))
de = desc / 100 # para transformar em porcentagem
vd = float(p * de) # aqui calcula o valor do desconto
pd = float(p - vd) # e aqui o valor do  produto com o desconto
print('O preço do produto era R${:.2f}. Com o desconto de {}%, equivalente a R${:.2f}, o novo preço do produto é de R${:.2f}.'. format(p, desc, vd, pd))
