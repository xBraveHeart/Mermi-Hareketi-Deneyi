import pygame, sys
from pygame.locals import *
from math import *
# OYUNA ARKA PLAN MÜZİĞİ EKLEME 

pygame.init()

arkaplansesi = pygame.mixer.Sound("arkaplansesi.mp3")

arkaplansesi.play()


# OYUN PENCERESİNİN KURULUMU 

EKRAN = pygame.display.set_mode((1152, 648), 0, 32)
pygame.display.set_caption('mermi hareketi')

arkaplanImg = pygame.image.load('resimler/arkaplan.png')
yatakImg = pygame.image.load('resimler/yatak.png')
havanImg = pygame.image.load('resimler/havan.png')
topImg = pygame.image.load('resimler/mermi.png')

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

#ANA OYUN DÖNGÜSÜ

while True:
  dt = fpsClock.tick(FPS) # dt = t_SON - t_İLK
  if launched:
    t = t + dt/250.0 # GÜNCELLENEN ZAMAN 
    #BURADA BULUNAN 250.0 TOPUN HAVADA KALMA SÜRESİNİ ETKİLEMİYOR FPS AYARLARI İLE MERMİNİN AĞIR ÇEKİMDE VEYA HIZLI OLARAK GİDECEĞİNE KARAR VERİYORUZ.

# HAVAN PARÇALARININ KONUM BİLGİLERİ 

yatakPos = (15,428)
havanPos = (-5, 400)
