nome = str(input('Qual é o seu nome? ')).strip().title()
cores = {'limpa':'\033[m',
         'azul': '\033[34m',
         'p&b': '\033[7;40m'}
print('Olá, {}{}{}!!!'.format(cores['p&b'], nome, cores['limpa']))