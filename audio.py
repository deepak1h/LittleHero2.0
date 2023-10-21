import pygame

def play():
    pygame.mixer.init()
    pygame.mixer.music.load("1.mp3")
    pygame.mixer.music.play()
