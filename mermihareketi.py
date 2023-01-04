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

#RESİM DOSYALARININ DEĞİŞKEN OLARAK TANIMLANMASI 

EKRAN.blit(arkaplanImg, (0,0))
EKRAN.blit(havanMovImg, havanPos  )
EKRAN.blit(topImg, topPos)



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
topPos = (22,428)

# BAŞLANGIÇ HAVAN POZİYONU

havanImg = pygame.transform.rotate(havanImg, -15)

# BAŞLANGIÇ TOP AÇISI AYARI

ang = 45


 #  EKRAN YAZILARININ AYARLANMASI

font = pygame.font.Font(None, 30)

text_ang = font.render("açı = %d" % ang, 1, (10, 10, 10))

text_ang_pos = (0, 460)


text_vm = font.render("hız = %.1f m/s" % vm, 1, (10, 10, 10))

text_vm_pos = (0, 480)


text_vx = font.render("yatay hız = %.1f m/s" % v[0], 1, (10, 10, 10))

text_vx_pos = (0, 500)


text_vy = font.render("dikey hız = %.1f m/s" % v[1], 1, (10, 10, 10))

text_vy_pos = (0, 520)


text_x = font.render("yatay konum = %.1f m" % s[0], 1, (10, 10, 10))

text_x_pos = (0, 540)


text_y = font.render("dikey konum = %.1f m" % s[1], 1, (10, 10, 10))

text_y_pos = (0, 560)








# YENİ SAHNE KURULUMU 

EKRAN.blit(arkaplanImg, (0,0))

EKRAN.blit(havanMovImg, havanPos  )

EKRAN.blit(topImg, s)
