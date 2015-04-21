import pygame
from pygame.locals import *
import SeeSawStars
import LevelSelect

pygame.init()

screen = pygame.display.set_mode([1200,700])

def instructionsMenu():
    x=1
    background = pygame.image.load("instructions1.png")
    backgroundrec = background.get_rect()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and K_ESCAPE):
                return
            if event.type == MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                                            
                if x == 2:
                    if location[1] > 560 and location[1] < 650:
                        if location[0] > 20 and location[0] < 250:
                            background = pygame.image.load("instructions1.png")
                            backgroundrec = background.get_rect()
                            x = 1
                    if location[1] > 560 and location[1] < 650:
                        if location[0] > 930 and location[0] < 1180:
                            background = pygame.image.load("instructions3.png")
                            backgroundrec = background.get_rect()   
                            x = 3
                elif x == 1:
                    if location[1] > 560 and location[1] < 650:
                        if location[0] > 20 and location[0] < 250:
                            return
                    if location[1] > 560 and location[1] < 650:
                        if location[0] > 950 and location[0] < 1180:
                            background = pygame.image.load("instructions2.png")
                            backgroundrec = background.get_rect()   
                            x = 2
                            
                elif x==3:
                    if location[1] > 560 and location[1] < 650:
                        if location[0] > 20 and location[0] < 250:
                            background = pygame.image.load("instructions2.png")
                            backgroundrec = background.get_rect()
                            x = 2
                    if location[1] > 560 and location[1] < 650:
                        if location[0] > 950 and location[0] < 1180:
                            return

                            
                            
                    
        screen.blit(background, backgroundrec)
        pygame.display.update()