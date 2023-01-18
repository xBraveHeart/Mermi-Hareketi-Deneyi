import pygame, sys
from pygame.locals import *
from math import *

# OYUNA ARKA PLAN MÜZİĞİ EKLEME 

pygame.init()

arkaplansesi = pygame.mixer.Sound("arkaplansesi.mp3")

arkaplansesi.play()

#top resminin uç kısımdan dönmesi 
def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

pygame.init()

# KARE/SANİYE AYARI

FPS = 60 
fpsClock = pygame.time.Clock()

# OYUN PENCERESİNİN KURULUMU 

EKRAN = pygame.display.set_mode((1152, 648), 0, 32)
pygame.display.set_caption('mermi hareketi')

arkaplanImg = pygame.image.load('resimler/arkaplan.png')
yatakImg = pygame.image.load('resimler/yatak.png')
havanImg = pygame.image.load('resimler/havan.png')
topImg = pygame.image.load('resimler/mermi.png')

# HAVAN PARÇALARININ KONUM BİLGİLERİ 

yatakPos = (15,428)
havanPos = (-5, 400)
topPos = (22,428)

# BAŞLANGIÇ HAVAN POZİYONU

havanImg = pygame.transform.rotate(havanImg, -15)


# BAŞLANGIÇ TOP AÇISI AYARI

ang = 45

havanMovImg = rot_center(havanImg, ang)

#RESİM DOSYALARININ DEĞİŞKEN OLARAK TANIMLANMASI 

EKRAN.blit(arkaplanImg, (0,0))

EKRAN.blit(havanMovImg, havanPos  )

EKRAN.blit(topImg, topPos)

EKRAN.blit(yatakImg, yatakPos)


# FİZİKSEL NİCELİKLERİN AYARLANMASI 

# ZAMAN

t = 0 

# UZAKLIK

s = topPos

# HIZ
v = (0, 0)

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
    
     a = (0.0, 10.0) 
     v =  (v0[0] + a[0]*t, v0[1] + a[1]*t) # İVME VE HIZ DEĞERLERİNİN TANIMLANMASI 
    
     vm = sqrt(v[0]*v[0] + v[1]*v[1])
     s0 = topPos # BAŞLANGIÇ POZİYONU
   
     s = (s0[0] + v0[0]*t + a[0]*t*t/2, s0[1] + v0[1]*t + a[1]*t*t/2) #FİZİK FORMULÜ
     if s[1] >= 436: # YERE VURMA
    
                launched = False

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


text_t = font.render("zaman = %.1f s" % t, 1, (10, 10, 10))

text_t_pos = (0, 580)







# YENİ SAHNE KURULUMU 

EKRAN.blit(arkaplanImg, (0,0))

EKRAN.blit(havanMovImg, havanPos  )

EKRAN.blit(topImg, s)

EKRAN.blit(yatakImg, yatakPos)

EKRAN.blit(text_t, text_t_pos)

EKRAN.blit(text_vx, text_vx_pos)

EKRAN.blit(text_vy, text_vy_pos)

EKRAN.blit(text_vm, text_vm_pos)

EKRAN.blit(text_x, text_x_pos)

EKRAN.blit(text_y, text_y_pos)

EKRAN.blit(text_ang, text_ang_pos)

# TUŞ ATAMALARI 
for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:    
        # BOŞLUK İLE BAŞLATMA 
        if event.key == K_SPACE:
            #topun atıldığında çıkarttığı patlama sesi 
            havansesi = pygame.mixer.Sound("patlama.mp3")
            havansesi.play()
            #Bu sesi bir Türk filmi olan Fetih 1453'ün ses efekt bölümünden aldık.
            
            topPos = (22,428)
            s = topPos
            t = 0
            launched = True
            
            # başlangıç hızını ayarlama 
            v0 = (vm*cos(radians(ang)), -vm*sin(radians(ang)))            
        
    keystate = pygame.key.get_pressed()
    
     # saat yönünün tersine çevirme

    if keystate[K_LEFT]: 
        ang+=2
        if ang > 90:
            ang = 90
        havanMovImg = rot_center(havanImg, ang)
        
        # saat yönüne çevirme 

    if keystate[K_RIGHT]: 
        ang-=2

        if ang < 0:
            ang = 0
        havanMovImg = rot_center(havanImg, ang)
        
        # ilk hızı artır

    if keystate[K_UP]: 

        vm+=2
         # ilk hızı düşür

    if keystate[K_DOWN]:
        vm-=2

      # asıl sahneyi göster 

    pygame.display.flip()                  
