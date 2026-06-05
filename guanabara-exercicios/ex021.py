#Faça um programa que abra e reproduza o áudio de um arquivo mp3 (ver até aula 08)

'''import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait() #esperar o evento de tocar música terminar
## versão antiga, não funcionou'''

from playsound import playsound
playsound('ex021.mp3')
