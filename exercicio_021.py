#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init()
# não consegui executar com arqivo .mp3
# aqui explica o motivo: https://www.pygame.org/docs/ref/music.html?highlight=mp3
#pygame.mixer.music.load('mus02.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()

# tentei executar com outra extensão e mesmo assim não rolou...
pygame.mixer.music.load('sonic.ogg')
pygame.mixer.music.play()
pygame.event.wait()
# o programa rodou mas não executou nenhum áudio, no arquivo 'exercicio_021_v2' eu mostro uma solução