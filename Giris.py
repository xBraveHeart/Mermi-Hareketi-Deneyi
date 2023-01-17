import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1152, 648))
pygame.display.set_caption("Mermi Hareketi Deneyi")

BG = pygame.image.load("resimler/Background.jpg")

def get_font(size): 
    return pygame.font.Font("resimler/font.ttf", size)












def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#035b52")
