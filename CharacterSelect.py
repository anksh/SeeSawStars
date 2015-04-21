import pygame
from pygame.locals import * 
import GameMech
import LevelSelect
pygame.init()

screen = pygame.display.set_mode([1200,700])
font=pygame.font.SysFont("Courier New", 46)
font2=pygame.font.SysFont("Courier New", 32)
screen.fill([250,250,250])



def characterselect(): 
    p1option=""
    p2option=""
    p1x=-100
    p2x=-100
    p1y=-100
    p2y=-100

    background=pygame.image.load("CharacterSelect.png")
    background=pygame.transform.scale(background, (1200,700))
    backgroundrec=background.get_rect() 
    p1rect=pygame.image.load("p1rect.png")
    p2rect=pygame.image.load("p2rect.png")
    screen.blit(background,backgroundrec)   
    EndGame=0
    enteredGame = False
    option = 0
    #defaults
    p1option = "FinalSpritev2RedCap.png"
    p2option = "FinalSpritev2RedCap.png"
    while EndGame!=1:
        screen.blit(background,backgroundrec) 
        screen.blit(p1rect,(p1x,p1y))
        screen.blit(p2rect,(p2x,p2y))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
            if event.type==MOUSEBUTTONDOWN:
                EndGame=2
    
        if EndGame==2:
            location=pygame.mouse.get_pos()
            if location[0]>30 and location [0]<92 and location[1]>60 and location[1]<176:
                p1x=30
                p1y=60
                p1option="FinalSpritev2RedCap.png"
                EndGame=0
                screen.blit(background,backgroundrec)
            if location[0]>209 and location[0]<278 and location[1]>60 and location[1]<176:
                p1x=209
                p1y=60
                p1option="FinalSpritev2NoHair.png"
                EndGame=0
                screen.blit(background,backgroundrec)
            if location[0]>392 and location[0]<468 and location[1]>60 and location[1]<176:
                p1x=392
                p1y=60
                p1option="FinalSpritev2GreenMohawk.png"
                EndGame=0
                screen.blit(background,backgroundrec)
            if location[0]>606 and location[0]<672 and location[1]>60 and location[1]<176:
                p1x=606
                p1y=60
                p1option="FinalSpritev2BlueCap.png"
                EndGame=0
                screen.blit(background,backgroundrec)
            if location[0]>830 and location[0]<900 and location[1]>60 and location[1]<176:
                p1x=830
                p1y=60
                p1option="FinalSpritev2Blonde.png"
                EndGame=0
                screen.blit(background,backgroundrec)
            if location[0]>1070 and location[0]<1142 and location[1]>60 and location[1]<176:
                p1x=1070
                p1y=60
                p1option="FinalSpritev2Basket.png"
                EndGame=0
                screen.blit(background,backgroundrec)
            if location[0]>32 and location[0]<100 and location[1]>383 and location[1]<546:
                p2x=32
                p2y=383
                p2option="FinalSpritev2RedCap.png"
                EndGame=0
                screen.blit(background,backgroundrec)
            if location[0]>201 and location[0]<262 and location[1]>396 and location[1]<546:
                p2x=201
                p2y=396
                p2option="FinalSpritev2NoHair.png"
                EndGame=0
                screen.blit(background,backgroundrec)
            if location[0]>399 and location[0]<462 and location[1]>390 and location[1]<546:
                p2x=399
                p2y=390
                p2option="FinalSpritev2GreenMohawk.png"
                EndGame=0
                screen.blit(background,backgroundrec)
            if location[0]>607 and location[0]<684 and location[1]>398 and location[1]<546:
                p2x=607
                p2y=398
                p2option="FinalSpritev2BlueCap.png"
                EndGame=0
                screen.blit(background,backgroundrec)
            if location[0]>842 and location[0]<900 and location[1]>398 and location[1]<546:
                p2x=842
                p2y=398
                p2option="FinalSpritev2Blonde.png"
                EndGame=0
                screen.blit(background,backgroundrec)
            if location[0]>1081 and location[0]<1142 and location[1]>396 and location[1]<546:
                p2x=1081
                p2y=396
                p2option="FinalSpritev2Basket.png"
                EndGame=0
                screen.blit(background,backgroundrec)
            if location[0]>900 and location[0]<1140 and location[1]>590 and location[1]<690:
                charFile=open("characters.txt","wb")
                charFile.write(p1option)
                charFile.write("\n")
                charFile.write(p2option)
                charFile.close()
                p1x=-100
                p1y=-100
                p2x=-100
                p2y=-100
                EndGame = 0
                option = LevelSelect.selectLevel()
                if option <=0:
                    return
            if location[0]>50 and location[0]<260 and location[1]>590 and location[1]<690:
                return
