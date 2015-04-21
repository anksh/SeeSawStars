import pygame
from pygame.locals import * 
import GameMech, EndGame, CharacterSelect, display, Instructions, Settings, Credits
import os

pygame.init()

screen = pygame.display.set_mode([1200,700])
font=pygame.font.SysFont("Courier New", 46)
font2=pygame.font.SysFont("Courier New", 32)
# screen.fill([250,250,250])
def menu():
    
    endgame=0
    x=0
    level = 1
    background = pygame.image.load("MenuScreen+2.png")
    # background = pygame.transform.scale(background, (1200,700))
    backgroundrec = background.get_rect()
    screen.blit(background, backgroundrec)
    fo = open("cheatfile.txt", "wb")
    fo.write("No code entered")
    fo.close()
    if not os.path.isfile("settings.txt"):
        fo = open("settings.txt", "wb")
        fo.write("Background.png")
        fo.close()

    while endgame>=0:        
        
        screen.blit(background, backgroundrec)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
                # print "hello"
            if event.type == MOUSEBUTTONDOWN:
                endgame = 1
    
        if endgame==1:
            location=pygame.mouse.get_pos()
            if location[0]>725 and location[0]<1165 and location[1]>35 and location[1]<220:
                CharacterSelect.characterselect()
                endgame = 2
            elif location[0]>725 and location[0]<1165 and location[1]>270 and location[1]<375:
                Instructions.instructionsMenu()
                endgame = 2
                # print "hi"
            elif location[0]>35 and location[0]<475 and location[1]>525 and location[1]<625:
                display.main()
                endgame = 2
            elif location[0]>725 and location[0]<1165 and location[1]>399 and location[1]<501:
                Settings.settingsMenu()
                endgame = 2
            elif location[0]>725 and location[0]<1165 and location[1]>525 and location[1]<630: 
                Credits.credits()
                endgame = 2
            else:
                endgame = 2
        
        # print endgame


if __name__ == '__main__':
    menu()    