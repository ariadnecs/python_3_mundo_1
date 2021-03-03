n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
r = n1 % n2
print('Você digitou {} e {}'.format(n1, n2))
print('A soma vale {:>16}'.format(s))
print('A subtração {:>16}'.format(su))
print('A multiplicação {:>12}'.format(m))
print('A divisão {:>18}'.format(d))
print('A exponenciação {:>12}'.format(e))
print('A divisão inteira {:>10}'.format(di))
print('O resto da divisão {:>9}'.format(r))