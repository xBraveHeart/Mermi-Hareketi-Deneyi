import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1152, 648))
pygame.display.set_caption("Mermi Hareketi Deneyi")

BG = pygame.image.load("resimler/Background.jpg")

def get_font(size): 
    return pygame.font.Font("resimler/font.ttf", size)

def play():
    import mermihareketi
    mermihareketi.start()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#035b52")





        AGA1_TEXT=get_font(20).render("EREN BARIN-032280032-github.com/erenbarin ", True, "White")
        AGA1_RECT=AGA1_TEXT.get_rect(center=(576, 200))
        SCREEN.blit(AGA1_TEXT,AGA1_RECT)



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
def main_menu():
    while True:
              
