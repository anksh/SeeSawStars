import pygame, os, random, math
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode([1200,700])
font=pygame.font.SysFont("Courier New", 46)
fps=10
score=0
lives=5
gameClock = pygame.time.Clock()
framerate = 30
EndGame = 0

class Player(pygame.sprite.Sprite):
    distance = 0.0
    # print distance
    width = 0
    height = 0
    def __init__(self, filename, width, height, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
                    
        self.image = pygame.transform.scale(self.image, (width,height))
        self.width=width
        self.height=height
                    
        self.rect = self.image.get_rect()
        self.x = location[0]
        self.y = location[1]
        self.rect.x = self.x
        self.rect.y = self.y
        self.width = width
        self.height
        self.distance = self.x-600+(self.width/2)

    def move(self, player, seesaw):
        key_pressed=pygame.key.get_pressed()
       	if self.rect.y >=650:
       		global lives
       		global score
       		global EndGame
       		lives = 5
       		score = 0
       		EndGame = 1
       		return -1
        
        if player==2:
            if self.rect.x>605 and key_pressed[K_LEFT]:
                self.x-=5
                self.y-=5*math.tan(math.radians(-seesaw.direction))
        if player==1:
            if self.rect.x>0 and key_pressed[K_a]:
                self.x-=5
                self.y-=5*math.tan(math.radians(-seesaw.direction))
        if player==2:
            if self.rect.x<1200-self.width and key_pressed[K_RIGHT]:
                self.x+=5
                self.y+=5*math.tan(math.radians(-seesaw.direction))
        if player==1:
            if self.rect.x<553 and key_pressed[K_d]:
                self.x+=5
                self.y+=5*math.tan(math.radians(-seesaw.direction))

        self.y = 600+(self.distance*math.tan(math.radians(-seesaw.direction)))-self.height
        self.distance = self.x-600+(self.width/2)
        self.rect.x = self.x
        self.rect.y = self.y
    

class stars(pygame.sprite.Sprite):
    attribute = " ";

    def __init__(self, color, filename, location, face):
        pygame.sprite.Sprite.__init__(self)
        #converts pixel format and transforms image
        self.image = pygame.image.load(filename).convert_alpha()
        # self.image.set_colorkey((255,255,255)) 
        self.image = pygame.transform.scale(self.image, (60,60))
        
        self.rect = self.image.get_rect()
        #assigns x and y components to location of star image
        self.location = location
        self.rect.x = location[0]
        self.rect.y = location[1]
        #self.counter = 0
        self.attribute = face
        
        
    def fallingStar(self, speed): 
        if self.location[1] > 810:
            self.location[1] = random.randrange(-400,-50)
            self.location[0] = random.randrange(0,560)
            #self.countter += 1

        #randomly assigns star a new coordinate
        else:
            self.location[1] = self.location[1] + speed
            
    def fallingStar2(self, speed): 
        if self.location[1] > 810:
            self.location[1] = random.randrange(-400,-50)
            self.location[0] = random.randrange(560,1160)
            #self.counter += 1
            
        #randomly assigns star a new coordinate
        else:
            self.location[1] = self.location[1] + speed
    #updates screen images so you can see movement of objects
    def update(self):
        self.rect = self.image.get_rect()        
        self.rect.x = self.location[0]
        self.rect.y = self.location[1]
        #draws an extra star
        #screen.blit(self.image, self)

class SeeSaw(pygame.sprite.Sprite):
    direction = 0.0
    amount = 0.0
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("SeeSaw.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (1200,10))
        self.origImage = self.image
                    
        self.rect = self.image.get_rect()
        self.x = location[0]
        self.y = location[1]
        self.rect.x = location[0]
        self.rect.y = location[1]

    def rotation(self, amount):
        # print amount
        self.amount = amount
        origCenter = self.rect.center
        self.direction += amount
        self.image = pygame.transform.rotate(self.origImage, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = origCenter
        # print self.rect.x
        # print self.rect.y


def play():
    player1=Player("stickfigure.png", 66,120,(275.0,475.0))
    player2=Player("stickfigure2.png", 66,120,(900.0,475.0))
    gap = player2.distance+player1.distance
    # print gap
    print "here"
    background=pygame.image.load("BackgroundTest.png")
    background = pygame.transform.scale(background, (1200, 750))
    backgroundrec=background.get_rect() 
    seesaw=SeeSaw((0.0,585.0))
    speed = 1.5
    n = 1
    morebstars = 7
    moreStars = 5
    gstars = []
    delList = []
    # EndGame=0
    count = 0
    gstars.append(stars((255,255,255),"star.png",[random.randrange(0,560),random.randrange(-150,-50)], "good"))
    gstars.append(stars((255,255,255),"star.png",[random.randrange(600,1160),random.randrange(-400,-50)], "good"))
    screen.blit(background,backgroundrec)

    global EndGame
    EndGame = 0
    while EndGame==0: 
    	gameClock.tick(framerate)
        gap = player2.distance+player1.distance
        # print gap
        if abs(gap)>25:
            seesaw.rotation(-(gap/5000))
        else:
            seesaw.amount = 0.0
        global lives
        global score
        if lives == 0:
            EndGame = 1
            # global score
            # global lives
            lives = 5
            score = 0
            return -1

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
            screen.blit(background,(gstars[i].rect.x, gstars[i].rect.y-5),(gstars[i].rect.x, gstars[i].rect.y-5, 70, 70))

        screen.blit(background,(player1.rect.x-10,player1.rect.y),(player1.rect.x-10,player1.rect.y,85,120))
        screen.blit(background,(player2.rect.x-10,player2.rect.y),(player2.rect.x-10,player2.rect.y, 85,120))
        
        screen.blit(background,(seesaw.rect.x-10, seesaw.rect.y-10), 
            (seesaw.rect.x-10, seesaw.rect.y-10, seesaw.rect.width+20, seesaw.rect.height+20))
        screen.blit(seesaw.image, seesaw)

        for x in gstars:
            i = gstars.index(x)
            if(pygame.sprite.collide_rect(player1, gstars[i]) or pygame.sprite.collide_rect(player2, gstars[i])):
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
                screen.blit(gstars[i].image, gstars[i])
            else:
                gstars[i].fallingStar2(speed)
                gstars[i].update()
                screen.blit(gstars[i].image, gstars[i])
    
        loopX = seesaw.rect.x
        loopY = seesaw.rect.y

        # for x in range(0,12):
        # 	# print loopX
        # 	# print loopY
        # 	offset = (600-loopX)*math.tan(math.radians(seesaw.direction))
        # 	y2 = loopY-(abs(offset))
        # 	screen.blit(background, (loopX, loopY), (loopX, loopY, 100, (offset))) #DOESNT WORK
        # 	loopX += 100
        # 	loopY = y2
        screen.blit(player1.image,player1)
        screen.blit(player2.image,player2)
        screen.blit(background, (0, 0), (0, 0, 300, 75))
    	screen.blit(scorewrite, (20,20))  
    	screen.blit(background, (950, 20), (950, 20, 250, 50))
    	screen.blit(liveswrite,(950,20))
    
        pygame.display.update()

        player1.move(1, seesaw)
        player2.move(2, seesaw)
    
    	count+=1
        print count
        if count == 50:
            return 1


        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                # global score
                # global lives
                lives = 5
                score = 0
                EndGame = 1
                return 0
