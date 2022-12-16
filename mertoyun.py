print("hello world")
from pygame import *
from random import randint
#yazı tipiyle çalışmak için işlevleri ayrı olarak yükleyin.
font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
 
font2 = font.Font(None, 36)
 
#arka plan müziği
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
 
#böyle resimlere ihtiyacımız var:
img_back = "galaxy.jpg" #oyunun arka planı
img_bullet = "bullet.png" #mermi
img_hero = "rocket.png" #kahraman
img_enemy = "ufo.png" #düşman
score = 0 #düşmüş gemiler
goal = 10 #Kazanmak için kaç gemiyi vurman gerekiyor
lost = 0 #kaçırılan gemiler
max_lost = 3 #Bu kadar çok şeyi kaçırırsanız kaybettiniz.
#sprite'lar için ebeveyn sınıfı
class GameSprite(sprite.Sprite):
 #Sınıf kurucusu
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #sınıf kurucusunu çağırıyoruz (Sprite):
       sprite.Sprite.__init__(self)
 
       # Her sprite image - resim özelliğini depolamalıdır
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       # Her sprite, içine yazıldığı dikdörtgenin  rect özelliğini saklamalıdır
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #pencereye kahraman çizen yöntem
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
#ana oyuncunun sınıfı
class Player(GameSprite):
   #Sprite'ı klavye oklarıyla kontrol etme yöntemi
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
 # atış yöntemi (orada bir mermi oluşturmak için oyuncunun yerini kullanırız)
   def fire(self):
       bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
       bullets.add(bullet)
 
#sprite-düşman sınıfı  
class Enemy(GameSprite):
   #düşmanın hareketi
   def update(self):
       self.rect.y += self.speed
       global lost
       #ekranın kenarına ulaştığında kaybolur
       if self.rect.y > win_height:
           self.rect.x = randint(80, win_width - 80)
           self.rect.y = 0
           lost = lost + 1
#mermi sprite sınıfı  
class Bullet(GameSprite):
   #düşmanın hareketi
   def update(self):
       self.rect.y += self.speed
       #ekranın kenarına ulaştığında kaybolur
       if self.rect.y < 0:
           self.kill()
#Bir pencere oluşturuyoruz
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
#sprite oluşturuyoruz
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
#bir grup düşman sprite oluşturun
monsters = sprite.Group()
for i in range(1, 6):
   monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
   monsters.add(monster)
bullets = sprite.Group()
# "oyun bitti" değişkeni: True olduğunda, sprite ana döngüde çalışmayı durdurur
finish = False
#Ana oyun döngüsü:
run = True #bayrak pencereyi kapat düğmesiyle sıfırlanır
while run:
   #Kapat düğmesindeki olayı tıklayın
   for e in event.get():
       if e.type == QUIT:
           run = False
       #space'e basılma durumunda sprite ateş ediyor
       elif e.type == KEYDOWN:
           if e.key == K_SPACE:
               fire_sound.play()
               ship.fire()
 #oyunun kendisi: sprite eylemleri, oyunun kurallarını kontrol etme, yeniden çizme
   if not finish:
       # arka planı güncelliyoruz
       window.blit(background,(0,0))
 
       #sprite hareketleri üretiyoruz
       ship.update()
       monsters.update()
       bullets.update()
 
       #Döngünün her yinelenmesinde onları yeni bir konumda güncelliyoruz
       ship.reset()
       monsters.draw(window)
       bullets.draw(window)
       #mermi ve canavarların çarpışmasını kontrol etme (hem canavar hem de mermi dokunulduğunda kaybolur)
       collides = sprite.groupcollide(monsters, bullets, True, True)
       for c in collides:
           #Bu döngü, canavarlar vurulduğu kadar tekrarlanır
           score = score + 1
           monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
           monsters.add(monster)
 
       #Muhtemel kaybetme durumu: kahramanın ya fazla kaçırması, ya da düşmanla karşılaşmasıdır.
       if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
           finish = True#kaybettik, arka planı koyduk ve artık spriteları yönetmiyoruz.
           window.blit(lose, (200, 200))
 
       #kazancınızı kontrol edin: kaç puan aldınız?
       if score >= goal:
           finish = True
           window.blit(win, (200, 200))
 
       #ekrana metin yazıyoruz
       text = font2.render("Score: " + str(score), 1, (255, 255, 255))
       window.blit(text, (10, 20))
 
       text_lose = font2.render("Missed: "+ str(lost), 1, (255, 255, 255))
       window.blit(text_lose, (10, 50))
 
       display.update()
   #bonus: otomatik oyun yeniden başlatma
   else:
       finish = False
       score = 0
       lost = 0
       for b in bullets:
           b.kill()
       for m in monsters:
           m.kill()
 
       time.delay(3000)
       for i in range(1, 6):
           monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
           monsters.add(monster)
      
 
   time.delay(50)

   