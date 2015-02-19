import pygame, os, random
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode([1200,800])
font=pygame.font.SysFont("Courier New", 46)
fps=10
score=0
lives=5

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
    

class stars(pygame.sprite.Sprite):
    attribute = " ";

    def __init__(self, color, filename, location, face):
        pygame.sprite.Sprite.__init__(self)
        #converts pixel format and transforms image
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(color) 
        self.image = pygame.transform.scale(self.image, (60,60))
        
        self.rect = self.image.get_rect()
        #assigns x and y components to location of pac-man image
        self.location = location
        self.rect.x = location[0]
        self.rect.y = location[1]
        #self.counter = 0
        self.attribute = face
        
        
    def fallingStar(self, speed): 
        if self.location[1] > 810:
            self.location [1] = random.randrange(-400,-50)
            self.location[0] = random.randrange(0,560)
            #self.counter += 1

        #randomly assigns fruit a new coordinate
        else:
            self.location[1] = self.location[1] + speed
            
    def fallingStar2(self, speed): 
        if self.location[1] > 810:
            self.location [1] = random.randrange(-400,-50)
            self.location[0] = random.randrange(560,1160)
            #self.counter += 1
            
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



def collide(obj1, obj2):
    if pygame.sprite.collide_rect(obj1, obj2):
        return True


def play():
    player1=Player("stickfigure.png", 66,120,(275,525))
    player2=Player("stickfigure2.png", 66,120,(900,525))

    background=pygame.image.load("BackgroundTest.png")
    backgroundrec=background.get_rect() 
    seesaw=pygame.image.load("SeeSawHorizontal.png")
    seesawrec=seesaw.get_rect()
    speed = 1.5
    GameOver = 0
    n = 1
    morebstars = 7
    moreStars = 5
    gstars = []
    delList = []
    EndGame=0
    count = 0
    gstars.append(stars((255,255,255),"star.png",[random.randrange(0,560),random.randrange(-150,-50)], "good"))
    gstars.append(stars((255,255,255),"star.png",[random.randrange(600,1160),random.randrange(-400,-50)], "good"))
    screen.blit(background,backgroundrec)


    while EndGame==0: 
        global lives
        global score   
        if lives == 0:
            EndGame = 1

    	scoretext="SCORE: " + str(score)
    	scorewrite=font.render(scoretext, 1, [0,0,0])
    	
    	livetext="LIVES: " + str(lives)
    	liveswrite=font.render(livetext,1,[0,0,0])


        if score == n:
            speed += .25
            n+=5
        
        if score == morebstars:
            gstars.append(stars((255,255,255),"badstar.png",[random.randrange(0,560),random.randrange(-150,-50)], "bad"))

            gstars.append(stars((255,255,255),"badstar.png",[random.randrange(600,1160),random.randrange(-150,-50)], "bad"))
            morebstars += 7
            
      
        if score == moreStars:
            gstars.append(stars((255,255,255),"star.png",[random.randrange(0,560),random.randrange(-150,-50)], "good"))

            gstars.append(stars((255,255,255),"star.png",[random.randrange(600,1160),random.randrange(-150,-50)], "good"))
            moreStars += 5
            #star1 = goodstar((255,255,255),"star.png",[random.randrange(0,600),random.randrange(-150,-50)])
            #star2 = goodstar((255,255,255),"star.png",[random.randrange(600,1160),random.randrange(-150,-50)])
        #left screen stars
        for x in gstars:
            i = gstars.index(x)
            if(pygame.sprite.collide_rect(player1, gstars[i]) or pygame.sprite.collide_rect(player2, gstars[i])):
                screen.blit(background,(gstars[i].rect.x, gstars[i].rect.y-5),(gstars[i].rect.x, gstars[i].rect.y-5, 70, 70))
                gstars[i].location[1] = -150
                if i%2 == 0:
                	gstars[i].location[0] = random.randrange(0,560)
               	else:
               		gstars[i].location[0] = random.randrange(600, 1160)
                if gstars[i].attribute == "good":
                    score +=1
                if gstars[i].attribute == "bad":
                    lives -=1
                gstars[i].update()
                continue
            if i%2 == 0:
                gstars[i].fallingStar(speed)
                gstars[i].update()
                screen.blit(background,(gstars[i].rect.x, gstars[i].rect.y-5),(gstars[i].rect.x, gstars[i].rect.y-5, 70, 70))
                screen.blit(gstars[i].image, gstars[i])
            else:
                gstars[i].fallingStar2(speed)
                gstars[i].update()
                screen.blit(background,(gstars[i].rect.x, gstars[i].rect.y-5),(gstars[i].rect.x, gstars[i].rect.y-5, 70, 70))
                screen.blit(gstars[i].image, gstars[i])
    
        screen.blit(background,(player1.rect.x-10,player1.rect.y),(player1.rect.x-10,player1.rect.y,85,120))
        screen.blit(background,(player2.rect.x-10,player2.rect.y),(player2.rect.x-10,player2.rect.y, 85,120))
        screen.blit(seesaw,seesawrec)
        screen.blit(player1.image,player1)
        screen.blit(player2.image,player2)
        screen.blit(background, (0, 0), (0, 0, 300, 75))
    	screen.blit(scorewrite, (20,20))  
    	screen.blit(background, (950, 20), (950, 20, 250, 50))
    	screen.blit(liveswrite,(950,20))
    
        pygame.display.update()

        player1.move(1)
        player2.move(2)
    
    	count+=1

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                EndGame = 1

