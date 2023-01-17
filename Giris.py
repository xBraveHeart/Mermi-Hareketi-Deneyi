import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1152, 648))
pygame.display.set_caption("Mermi Hareketi Deneyi")














def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#035b52")
