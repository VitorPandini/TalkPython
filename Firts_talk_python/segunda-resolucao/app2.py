from gtts import gTTS
import pygame
import os
from playsound import playsound

# Importação bibliotecas:gtts,pygame,os e playsound

#função para armazenar o audio, como o proprio nome sugere
def guardar_audio(text):
    var = gTTS(text = text, lang = 'pt-br')
    var.save('audio.mp3')

#função para tocar o audio em formato mp3, as linhas comentadas sugerem que pode ser feita tanto com a biblioteca pygame tanto quanto a playsound
def tocar_mp3():
    playsound('audio.mp3')
    #pygame.mixer.init()
    #pygame.init()
    #pygame.mixer.music.load('./audio.mp3')
    #pygame.mixer_music.play()
    #pygame.event.wait()
    os.remove('./audio.mp3')

text = ''
#text, inicia uma variavel vazia, abaixo utiização de um loop para efetuar as tarefas assim sugeridas
while text != 'sair':
    text = input(': ')
    guardar_audio(text)
    tocar_mp3()
