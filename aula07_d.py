c = input('Em qual cidade você mora? ')
e = input('E em qual estado? ')

# para unir 2 prints basta digitar end=' '
print('Você mora na cidade {}'.format(c), end=' ')
print('no estado {}'.format(e))

#para quebra de linha \n
print('Você mora na cidade {} \nno estado {}'.format(c, e))