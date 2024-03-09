"""Colar o arquivo mp3 na pasta"""

import pygame
pygame.init()
pygame.mixer.music.load("""arquivo.mp3""")
pygame.mixer.music.play()
pygame.event.wait()