#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome: ')).strip().title().split()
print('Seu primeiro nome é {} e seu último nome é {}.'.format(nome[0], nome[len(nome) - 1]))
print('Olá {} {}! '.format(nome[0], nome[len(nome)-1])) # -1 pq o python conta a posição 0