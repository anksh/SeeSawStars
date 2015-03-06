import pygame
from pygame.locals import * 
import GameMech

pygame.init()

screen = pygame.display.set_mode([1200,700])
font=pygame.font.SysFont("Courier New", 46)
font2=pygame.font.SysFont("Courier New", 32)
screen.fill([250,250,250])

def menu():    
    EndGame=0
    while EndGame==0:        
        
        screen.fill([250,250,250])
        
        playtext="PLAY"
        playwrite=font.render(playtext,1,[0,0,0])
        screen.blit(playwrite,(500,400))
        inst1Text = "Player one: move with 'A' and 'D'."
        inst2Text = "Player two: move with the left and right arrow keys."
        inst3Text = "Collect the Yellow stars and avoid the Red ones."
        inst1write = font2.render(inst1Text,1,[0,0,0])
        inst2write = font2.render(inst2Text,1,[0,0,0])
        inst3write = font2.render(inst3Text,1,[0,0,0])
        screen.blit(inst1write, (270,50))
        screen.blit(inst2write, (100,100))
        screen.blit(inst3write, (150,150))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                EndGame = 1
            if event.type==MOUSEBUTTONDOWN:
                EndGame=2
    
        if EndGame==2:
            location=pygame.mouse.get_pos()
            if location[0]>500 and location[0]<800 and location[1]>400 and location[1]<600:
                GameMech.play()
            menu()
 

if __name__ == '__main__':
    menu()    