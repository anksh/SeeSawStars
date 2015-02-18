import pygame
from pygame.locals import * 
import PlayerStart

pygame.init()

screen = pygame.display.set_mode([1200,800])
font=pygame.font.SysFont("Courier New", 46)
screen.fill([250,250,250])

def menu():    
    EndGame=0
    while EndGame==0:        
        
        screen.fill([250,250,250])
        
        playtext="PLAY"
        playwrite=font.render(playtext,1,[0,0,0])
        screen.blit(playwrite,(600,400))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                EndGame = 1
            if event.type==MOUSEBUTTONDOWN:
                EndGame=2
    
        if EndGame==2:
            location=pygame.mouse.get_pos()
            if location[0]>600and location[0]<800 and location[1]>400 and location[1]<600:
                PlayerStart.play()
            menu()
 
menu()       