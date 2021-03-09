frase = '''I'll carry the load Heavy as a stone When the only thing I leave behind are weeds and broken bones 
Black trees lining the road Silent and secretly I stole I dug holes to feed my soul 
It was me It was me Slowly you fall asleep
And e fool got caught in the trap Just a glow in the night Oh you always strike the matches like a villain
It was me It was me Slowly you fall asleep
The venom I spread could kill a whole pack of wolves And your head is full of it Oh I swear you are so precious to me 
But this is as far as I can go my love This is as far as I can go my love
Rough cheeks rubbin' the cold white ground Shallow we're breathing in and out I sow the seeds of a rhizome
The ivy has grown up the walls of your house And I outline our story so as to make It sound like nothing really happened Things that you know to be true
It was me It was me Slowly you fall asleep
It was me It was me Slowly you fall asleep
This is as far as I can go my love
This is as far as I can go my love
Oh this is as far as I can go my love
Oh this is as far as I can go my love '''

print(frase.capitalize())
print('\n\n', frase.title())

frase.strip()# remove os espaços em excesso no início e no final da string
frase.split()# divide a string em palavras a partir dos espaços
print('\n\nHá', frase.count(' '), 'palavras neste texto.')
print('O texto contém', len(frase), 'caracteres.')
print('love' in frase)# verifica se há na string a palavra love, True/False
print('-love- is sawed', frase.count('love'), 'times in the sentence')
