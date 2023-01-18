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

        
        AGA2_TEXT=get_font(20).render("MERT NUHOGLU-032280058-github.com/xBraveHeart ", True, "White")
        AGA2_RECT=AGA2_TEXT.get_rect(center=(576, 250))
        SCREEN.blit(AGA2_TEXT,AGA2_RECT)
       
    
        AGA3_TEXT=get_font(20).render("EMIR TUTLU-032280034-github.com/emirtutlu ", True, "White")
        AGA3_RECT=AGA3_TEXT.get_rect(center=(576, 300))
        SCREEN.blit(AGA3_TEXT,AGA3_RECT)     
        
        
        
        
        
        
        
        
        
        
        OPTIONS_BACK = Button(image=None, pos=(576, 460), 
                            text_input="Geri", font=get_font(40), base_color="White", hovering_color="Yellow")
       
        
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                
        pygame.display.update()
        
                     
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()        
              
        MENU_TEXT = get_font(50).render("Mermi Hareketi Deneyi", True, "#035b52")
        MENU_RECT = MENU_TEXT.get_rect(center=(576, 100))        
        
        PLAY_BUTTON = Button(image=pygame.image.load("resimler/Play_Rect.png"), pos=(576, 250), 
                            text_input="Başlat", font=get_font(40), base_color="#d7fcd4", hovering_color="White")       
        OPTIONS_BUTTON = Button(image=pygame.image.load("resimler/Options_Rect.png"), pos=(576, 400), 
                            text_input="Emeği Geçenler", font=get_font(40), base_color="#d7fcd4", hovering_color="White")        
        QUIT_BUTTON = Button(image=pygame.image.load("resimler/Quit_Rect.png"), pos=(576, 550), 
                            text_input="Çıkış", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        
                SCREEN.blit(MENU_TEXT, MENU_RECT)

            
            
            
            
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()    
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
           pygame.display.update()

main_menu()
