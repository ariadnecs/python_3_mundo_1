#: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
r = float(input('Quanto dinheiro você tem na carteira: R$'))
#d = r / 5.62
#e = r / 6.78
#l = r / 7.84
#print('Você tem R${:.2f} e isso equivale a US${:.2f}.'.format(r, d))
print('Você tem R${:.2f} e esse valor equivale: \na US${:.2f}, a €{:.2f} e a £{:.2f}. \nÉ...nossa moeda está desvalorizada!'.format(r, r / 5.62, r / 6.78, r / 7.84))