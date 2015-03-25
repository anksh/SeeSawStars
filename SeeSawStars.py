import pygame
from pygame.locals import * 
import GameMech
import EndGame

pygame.init()

screen = pygame.display.set_mode([1200,700])
font=pygame.font.SysFont("Courier New", 46)
font2=pygame.font.SysFont("Courier New", 32)
# screen.fill([250,250,250])
def menu():
    endgame=0
    x=0
    level = 1
    background = pygame.image.load("MenuScreen.jpg")
    # background = pygame.transform.scale(background, (1200,700))
    backgroundrec = background.get_rect()
    screen.blit(background, backgroundrec)

    while endgame>=0:        
        # print endgame
        screen.blit(background, backgroundrec)
        if endgame == 3:
            if x>0:
                # if level< 3:
                level+=1
                x = GameMech.play(level)
                continue
            if x<0:
                EndGame.GameOver(x)
                endgame = 0
                level = 1
            else:
                level = 1
        # screen.fill([250,250,250])
        
        inst1Text = "Player one: move with 'A' and 'D'."
        inst2Text = "Player two: move with the left and right arrow keys."
        inst3Text = "Collect the stars with the correct emotions."
        inst1write = font2.render(inst1Text,1,[0,0,0])
        inst2write = font2.render(inst2Text,1,[0,0,0])
        inst3write = font2.render(inst3Text,1,[0,0,0])
        screen.blit(inst1write, (270,550))
        screen.blit(inst2write, (100,600))
        screen.blit(inst3write, (150,650))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                endgame = -1
                # print "hello"
            if event.type==MOUSEBUTTONDOWN:
                endgame=2
    
        if endgame==2:
            location=pygame.mouse.get_pos()
            if location[0]>700 and location[0]<1150 and location[1]>100 and location[1]<275:
                x = GameMech.play(level)
                endgame = 3
                print "hi"
            else:
                endgame = 0
        
        # print endgame


if __name__ == '__main__':
    menu()    