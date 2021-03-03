# parecido com aula07_b porém agora com float
n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um número: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
r = n1 % n2
print('Você digitou {:1.2f} e {:1.2f}'.format(n1, n2))
print('A soma vale {:>32.2f}'.format(s))
print('A subtração {:>32.2f}'.format(su))
print('A multiplicação {:28.2f}'.format(m))
print('A divisão {:>34.2f}'.format(d))
print('A exponenciação {:28.2f}'.format(e))
print('A divisão inteira {:26.2f}'.format(di))
print('O resto da divisão {:25.2f}'.format(r))
