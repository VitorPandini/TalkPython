from gtts import gTTS
import pygame
import os
from playsound import playsound


def guardar_audio(text):
    var = gTTS(text = text, lang = 'pt-br')
    var.save('audio.mp3')

def tocar_mp3():
    playsound('audio.mp3')
    #pygame.mixer.init()
    #pygame.init()
    #pygame.mixer.music.load('./audio.mp3')
    #pygame.mixer_music.play()
    #pygame.event.wait()
    os.remove('./audio.mp3')

text = ''
while text != 'sair':
    text = input(': ')
    guardar_audio(text)
    tocar_mp3()
