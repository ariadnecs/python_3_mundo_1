# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# recomendo a leitura e teste de outros módulos https://pythonbasics.org/python-play-sound/
# roda no interpretador virtualenv
from pydub import AudioSegment
from pydub.playback import play
# nesse exemplo a música deve estar no mesmo diretório do script
song = AudioSegment.from_mp3('mus_01.mp3') #from_extensao('musica.extensao'), ex.: from_ogg('sonic.ogg')
play(song)
# é possivel executar musicas que estão localizadas em um diretório diferente tb
# song = AudioSegment.from_mp3('/home/ariadnedcs/Música/soft_jazz/15_Europa.mp3')
# play(song)
