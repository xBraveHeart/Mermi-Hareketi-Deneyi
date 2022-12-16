# pygame_animation
from timeit import default_timer as timer
from os import listdir
from os.path import join
import pygame

__all__ = ("init","Animation","update","from_folder")

animasyonlar = []

def init(display):
    global dis
    dis = display

class Animation:
    def __init__(self,images : list,time_interval : float, loop = True):
        assert type(images) == list , "<images> parametresi <list> olmalıdır, <{}> değil.".format(type(images))
        assert type(time_interval) == float , "<time_interval> parametresi <float> olmalıdır, <{}> değil.".format(type(time_interval))
        self.images = images
        self.time_interval = time_interval
        self.pos = [0,0]
        self.is_running = False
        self.loop = loop
    
    def __call__(self):
        """Animasyonu başlatır."""
        self.start()

    def stop(self):
        """Animasyonun durdurur."""
        animasyonlar.remove(self)
        self.is_running = False

    def start(self):
        """Animasyonu başlatır."""
        animasyonlar.append(self)
        self.time = timer()
        self.is_running = True
    
    def jump(self,index=0):
        """Animasyona <index> sırasındaki resimden devam eder."""
        self.time = timer() - self.time_interval*index

    def set_pos(self,*,x=None,y=None):
        """Animasyonun çizileceği konumu değiştirir."""
        if x!=None:
            self.pos[0] = x
        if y!=None:
            self.pos[1] = y

    def __repr__(self):
        return "Animasyon <pos({},{})> <running={}> <index={}>".format(self.pos[0],self.pos[1],self.is_running,int((timer()-self.time)//self.time_interval))

def update():
    """Ana döngüde her defasında bir defa çağırılmalıdır.\npygame.display.update fonksiyonundan önce çağırılması\ntavsiye edilir."""
    time_now = timer()
    liste = animasyonlar[:]
    for a in liste:
        try:
            dis.blit(a.images[int((time_now-a.time)//a.time_interval)],a.pos)
        except IndexError:
            if a.loop:
                a.time = time_now
                dis.blit(a.images[0],a.pos)
            else:
                a.stop()

def from_folder(folder : str):
    """Dosyadaki resimlerden liste oluşturur."""
    dosyalar = listdir(folder)
    images = []
    for i in dosyalar:
        images.append(pygame.image.load(join(folder,i)))
    return images