import pygame, os
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode([1200,800])
font=pygame.font.SysFont("Courier New", 46)
fps=10

class Player(pygame.sprite.Sprite):
    def __init__(self, filename, width, height, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
                    
        self.image = pygame.transform.scale(self.image, (width,height))
        self.width=width
        self.height=height
                    
        self.rect = self.image.get_rect()

        self.rect.x = location[0]
        self.rect.y = location[1]

    def move(self, player):
        key_pressed=pygame.key.get_pressed()
        
        if player==2:
            if self.rect.x>605 and key_pressed[K_LEFT]:
                self.rect.x-=10
        if player==1:
            if self.rect.x>0 and key_pressed[K_a]:
                self.rect.x-=10
        if player==2:
            if self.rect.x<1200-self.width and key_pressed[K_RIGHT]:
                self.rect.x+=10
        if player==1:
            if self.rect.x<553 and key_pressed[K_d]:
                self.rect.x+=10
            
def play():
    player1=Player("stickfigure.png", 44,80,(275,560))
    player2=Player("stickfigure2.png", 44,80,(900,560))

    background=pygame.image.load("BackgroundTest.png")
    backgroundrec=background.get_rect() 
    seesaw=pygame.image.load("SeeSawHorizontal.png")
    seesawrec=seesaw.get_rect()

    screen.blit(background,backgroundrec)
    score=0
    lives=5
    EndGame=0
    while EndGame==0:    
    
        scoretext="SCORE: "+str(score)
        scorewrite=font.render(scoretext, 1, [0,0,0])
    
        livetext=str(lives)
        liveswrite=font.render(livetext,1,[0,0,0])
    
        screen.blit(background,(player1.rect.x-5,player1.rect.y),(player1.rect.x-5,player1.rect.y,60,80))
        screen.blit(background,(player2.rect.x-10,player2.rect.y),(player2.rect.x-10,player2.rect.y,60,80))
        screen.blit(seesaw,seesawrec)
        screen.blit(player1.image,player1)
        screen.blit(player2.image,player2)   
        screen.blit(scorewrite, (20,20))  
        screen.blit(liveswrite,(610,745))
    
        pygame.display.update()

        player1.move(1)
        player2.move(2)
    
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                EndGame = 1

