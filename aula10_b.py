nome = str(input('Digite o seu nome: ')).strip().title()
n1 = float(input('Nota da primeira prova: '))
n2 = float(input('Nota da segunda prova: '))
media = (n1 + n2)/2
print('Olá {}, a sua média é {:.2f}.'.format(nome, media))
if media >= 6: # condição simples
    print('Você foi aprovada(o).')
else: #condição composta
    print('Você foi reprovada(o).')
print('PARABÉNS!!!'if media>=6 else 'Sinto muito. \nProcure estudar em grupo, pode ajudar.')# condição cimplificada