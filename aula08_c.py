# para instalar este módulo eu tive que mudar o interpretador conda para o pip e instalar o módulo emogi,
# file> settings> pasta_do_projeto> python interpreter e cliquei no +, digitei 'emoji' e selecionei 'install package'
import emoji
print(emoji.emojize('Olá mundo :earth_americas:', use_aliases=True))