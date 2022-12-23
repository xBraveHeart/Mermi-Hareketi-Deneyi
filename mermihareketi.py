import pygame, sys
from pygame.locals import *
from math import *


# OYUN PENCERESİNİN KURULUMU 
DISPLAYSURF = pygame.display.set_mode((1280, 720), 0, 32)
pygame.display.set_caption('mermi hareketi')
FPS = 60 # kare/saniye ayarı
fpsClock = pygame.time.Clock()
