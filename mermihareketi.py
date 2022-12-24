import pygame, sys
from pygame.locals import *
from math import *


# OYUN PENCERESİNİN KURULUMU 

DISPLAYSURF = pygame.display.set_mode((1152, 648), 0, 32)
pygame.display.set_caption('mermi hareketi')

# KARE/SANİYE AYARI

FPS = 60 
fpsClock = pygame.time.Clock()

