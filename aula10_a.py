nome = str(input('Qual é o seu nome? ')).strip().title()
if nome == 'Spok':
    print('Que bom te você aqui!')
else:
    print('Olá, {}.'.format(nome))
print('Vida longa e póspera!')