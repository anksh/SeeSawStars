'''
Created on Jan 27, 2015

@author: ryanpifer
'''
import pygame, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode([1200,800])
pygame.display.set_caption("Discussion 3")


class stars(pygame.sprite.Sprite):
    attribute = " ";

    def __init__(self, color, filename, location, face):
        pygame.sprite.Sprite.__init__(self)
        #converts pixel format and transforms image
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(color) 
        self.image = pygame.transform.scale(self.image, (40,40))
        
        self.rect = self.image.get_rect()
        #assigns x and y components to location of pac-man image
        self.location = location
        self.rect.x = location[0]
        self.rect.y = location[1]
        self.counter = 0
        self.attribute = face
        
        
    def fallingStar(self): 
        if self.location[1] > 810:
            self.location [1] = random.randrange(-400,-50)
            self.location[0] = random.randrange(0,560)
            self.counter += 1

        #randomly assigns fruit a new coordinate
        else:
            self.location[1] = self.location[1] + speed
            
    def fallingStar2(self): 
        if self.location[1] > 810:
            self.location [1] = random.randrange(-400,-50)
            self.location[0] = random.randrange(560,1160)
            self.counter += 1
            
        #randomly assigns fruit a new coordinate
        else:
            self.location[1] = self.location[1] + speed
    #updates screen images so you can see movement of objects
    def update(self):
        self.rect = self.image.get_rect()        
        self.rect.x = self.location[0]
        self.rect.y = self.location[1]
        #draws an extra star
        #screen.blit(self.image, self)  
           



speed = 4
GameOver = 0
n = 1
morebstars = 7
moreStars = 5
gstars=[]
gstars.append(stars((0,0,0),"star.png",[random.randrange(0,600),random.randrange(-150,-50)], "good"))
gstars.append(stars((0,0,0),"star.png",[random.randrange(600,1160),random.randrange(-400,-50)], "good"))
#star3 = goodstar((255,255,255),"star.png",[random.randrange(600,1160),random.randrange(-150,-50)])
#star4 = goodstar((255,255,255),"star.png",[random.randrange(0,600),random.randrange(-150,-50)])
#star5 = badstar((255,255,255),"badstar.png",[random.randrange(600,1160),random.randrange(-150,-50)])
#star6 = badstar((255,255,255),"badstar.png",[random.randrange(0,600),random.randrange(-150,-50)])
#keeps game screen open as long as you do not press the exit button in top left corner

while GameOver != 1:
    
    #creates white background
    screen.fill([255,255,255])
    
    if gstars[0].counter == n or gstars[1].counter == n:
        speed += .25
        n+6
    
    if gstars[0].counter == morebstars or gstars[1].counter >= morebstars :
        gstars.append(stars((0,0,0),"badstar.png",[random.randrange(0,600),random.randrange(-150,-50)], "bad"))

        gstars.append(stars((0,0,0),"badstar.png",[random.randrange(600,1160),random.randrange(-150,-50)], "bad"))
        morebstars += 7
        
  
    if gstars[0].counter == moreStars:
        gstars.append(stars((0,0,0),"star.png",[random.randrange(0,600),random.randrange(-150,-50)], "good"))

        gstars.append(stars((0,0,0),"star.png",[random.randrange(600,1160),random.randrange(-150,-50)], "good"))
        moreStars += 5
        #star1 = goodstar((255,255,255),"star.png",[random.randrange(0,600),random.randrange(-150,-50)])
        #star2 = goodstar((255,255,255),"star.png",[random.randrange(600,1160),random.randrange(-150,-50)])
    #left screen stars
    for x in gstars:
        print gstars.index(x)
        if gstars.index(x)%2 == 0:
            screen.blit(gstars[gstars.index(x)].image, gstars[gstars.index(x)])
            gstars[gstars.index(x)].fallingStar()
            gstars[gstars.index(x)].update()
        else:
            screen.blit(gstars[gstars.index(x)].image, gstars[gstars.index(x)])
            gstars[gstars.index(x)].fallingStar2()
            gstars[gstars.index(x)].update()
            
    
    pygame.display.update()
    
    

    
    #tests user commands
    for event in pygame.event.get():
        if event.type == QUIT:#if you press the 'x' in the top left corner game play will stop
            GameOver = 1