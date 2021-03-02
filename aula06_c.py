# para treinar metodos de teste de tipo
v = input('Digite algo: ')
print('É um número?', v.isnumeric())
print('É uma letra?', v.isalpha())
print('É um número ou uma letra?', v.isalnum())
print('Está escrito somente com letras maiúsculas?', v.isupper())
print('Está escrito somente com letras minúsculas?', v.islower())
# há mais formas de testar o tipo de uma variável, aqui foram apenas alguns exemplos