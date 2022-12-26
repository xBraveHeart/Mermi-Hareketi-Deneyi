import pygame, sys
from pygame.locals import *
from math import *


# OYUN PENCERESİNİN KURULUMU 

EKRAN = pygame.display.set_mode((1152, 648), 0, 32)
pygame.display.set_caption('mermi hareketi')

arkaplanImg = pygame.image.load('resimler/arkaplan.png')
yatakImg = pygame.image.load('resimler/yatak.png')
havanImg = pygame.image.load('resimler/havan.png')

# KARE/SANİYE AYARI

FPS = 60 
fpsClock = pygame.time.Clock()

# FİZİKSEL NİCELİKLERİN AYARLANMASI 

# ZAMAN
t = 0 

# UZAKLIK 
s = topPos

# BAŞLANGIÇ HIZI 
vm = 100

# TOPUN ATILMASI 
launched = False  
