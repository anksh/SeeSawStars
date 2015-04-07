import pygame, os, random, math, time
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode([1200,700])
font=pygame.font.SysFont("Courier New", 40)
levelFont = pygame.font.SysFont("Courier New", 96)
levelFont.set_bold(True)
fps=10
score=0
lives=5
gameClock = pygame.time.Clock()
FRAMERATE = 30
t0 = 0
alarm = 15
transition = 0
font_phrases=pygame.font.SysFont("Courier New", 25)
font_phrases.set_bold(True)
left_write = font_phrases.render(" ", 1,[0,0,0])
right_write = font_phrases.render(" ",1,[0,0,0])

ACTIONS = [' is happy.', ' is sad.', ' found his favorite hat.', ' lost his favorite hat.', 
                ' received a birthday present.', ' fell off his bike.',
                ' is eating pizza and icecream.', ' broke his toy.', 
                ' is playing with his toys.', ' lost his dog.']
ATTRIBUTES = ["happy", "sad"]

ACTIONS_DICT = {ACTIONS[0]:ATTRIBUTES[0], ACTIONS[1]:ATTRIBUTES[1],
                ACTIONS[2]:ATTRIBUTES[0], ACTIONS[3]:ATTRIBUTES[1],
                ACTIONS[4]:ATTRIBUTES[0], ACTIONS[5]:ATTRIBUTES[1],
                ACTIONS[6]:ATTRIBUTES[0], ACTIONS[7]:ATTRIBUTES[1],
                ACTIONS[8]:ATTRIBUTES[0], ACTIONS[9]:ATTRIBUTES[1]}

NAMES= ['Andy','Alex', 'Bob','Brian', 'Carl','Cary', 
             'Dave','Dan','Evan', 'Eric', 'Fred', 'Frank']
FILENAMES = [ "HappyStar.png", "SadStar.png"]

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
            if self.rect.x<535 and key_pressed[K_d]:
                self.x+=5
                self.y+=5*math.tan(math.radians(-seesaw.direction))

        self.y = 600+(self.distance*math.tan(math.radians(-seesaw.direction)))-self.height
        self.distance = self.x-600+(self.width/2)
        self.rect.x = self.x
        self.rect.y = self.y
    

class stars(pygame.sprite.Sprite):
    attribute = " "
    isOnScreen = False

    def __init__(self, color, filename, location, face):
        pygame.sprite.Sprite.__init__(self)
        #converts pixel format and transforms image
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80,80))
        self.image.set_colorkey([255,255,255]) 
        
        self.rect = self.image.get_rect()
        #assigns x and y components to location of star image
        self.location = location
        self.rect.x = location[0]
        self.rect.y = location[1]
        #self.counter = 0
        self.attribute = face

    def checkOverlap(self, starsList, screenLoc):
        clear = False
        while not clear:
            startOver = False
            for x in range(len(starsList)):
                print "here"
                if (starsList[x] is self):
                    print "same"
                    continue
                if pygame.sprite.collide_rect(self, starsList[x]):
                    print "gotem"
                    # 1 is the left hand side, 2 is the right hand side
                    if(screenLoc == 1):
                        print "left"
                        self.location[0] = random.randrange(0,520)
                        self.rect.x = self.location[0]
                    if(screenLoc == 2):
                        print "right"
                        self.location[0] = random.randrange(600,1100)
                        self.rect.x = self.location[0]
                    startOver = True
            print " "
            if (not startOver):
                clear = True

        
    def getHitBox(self):
        return self.rect.inflate(-30,-40)
        
    def fallingStar(self, speed, starsList): 
        global transition
        if transition == 1:
            if not self.isOnScreen:
                return
        if self.location[1] > 710:
            self.location[1] = random.randrange(-500,-50)
            self.location[0] = random.randrange(0,520)
            # self.rect.x = self.location[0]
            # self.rect.y = self.location[1]
            self.update()
            j = random.randrange(0,len(ATTRIBUTES))
            self.attribute = ATTRIBUTES[j]
            self.image = pygame.image.load(FILENAMES[j]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (80,80))
            self.checkOverlap(starsList, 1)  
            
        else:
            self.location[1] = self.location[1] + speed
            
    def fallingStar2(self, speed, starsList): 
        global transition
        if transition == 1:
            # print self.rect.y
            if not self.isOnScreen:
                # print "off screen"
                return
        if self.location[1] > 710:
            self.location[1] = random.randrange(-500,-50)
            self.location[0] = random.randrange(600,1100)
            # self.rect.x = self.location[0]
            # self.rect.y = self.location[1]
            self.update()
            j = random.randrange(0,len(ATTRIBUTES))
            self.attribute = ATTRIBUTES[j]
            self.image = pygame.image.load(FILENAMES[j]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (80,80))
            self.checkOverlap(starsList, 2)
        else:
            self.location[1] = self.location[1] + speed
    #updates screen images so you can see movement of objects
    def update(self):
        # print "updating"
        self.rect = self.image.get_rect()        
        self.rect.x = self.location[0]
        self.rect.y = self.location[1]
        if self.rect.y < 700 and self.rect.y > -80:
            self.isOnScreen = True
        else:
            self.isOnScreen = False
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
        # print self.direction
        self.amount = amount
        origCenter = self.rect.center
        self.direction += amount
        self.image = pygame.transform.rotate(self.origImage, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = origCenter
        # print self.direction
        #print self.rect.x
        #print self.rect.y

def phrases(phrase_num):
    global left_write
    global right_write
#     global font_phrases
    left_name = NAMES[random.randrange(0,12,1)]
    right_name = NAMES[random.randrange(0,12,1)]
    actions_tuple = ACTIONS[random.randrange(0,phrase_num,1)], ACTIONS[random.randrange(0,phrase_num,1)]

    phrase_left = left_name + actions_tuple[0]
    phrase_right = right_name + actions_tuple[1]
    left_write = font_phrases.render(phrase_left, 1, [0,0,0])
    right_write = font_phrases.render(phrase_right,1,[0,0,0])
    return actions_tuple

def play(level):
    player1=Player("FinalSpritev2GreenMohawk.png", 66,120,(240.0,475.0))
    player2=Player("FinalSpritev2Basket.png", 66,120,(900.0,475.0))
    gap = player2.distance+player1.distance
    # print gap
    background=pygame.image.load("Background.png")
    background = pygame.transform.scale(background, (1200, 700))
    backgroundrec=background.get_rect() 
    seesaw=SeeSaw((0.0,585.0))
    speed = 3+level
    GameOver = 0
    n = 1
    moreStars = 1
    lstars = []
    rstars = []
    EndGame=0
    starslimit = 1
    offscreenStars = 0

    levelTxt = "Level: " + str(level)
    writeLvl = levelFont.render(levelTxt, 1, [0,0,0])
    if level == 1:
        numPhrases = 2
    elif level == 2:
        numPhrases = 10
    else:
        numPhrases = 10

    global transition
    correct_tuple = phrases(numPhrases)
    correct_left = ACTIONS_DICT[correct_tuple[0]]
    correct_right = ACTIONS_DICT[correct_tuple[1]]
    # print correct_left
    # print correct_right
    for x in range(0,4):
        if x%2:
            lstars.append(stars((255,255,255),"HappyStar.png",
                [random.randrange(0,520),random.randrange(-300,-50)], ATTRIBUTES[0]))
            lstars[x].checkOverlap(lstars, 1)
            rstars.append(stars((255,255,255),"SadStar.png",
                [random.randrange(600,1100),random.randrange(-300,-50)], ATTRIBUTES[1]))
            rstars[x].checkOverlap(rstars, 2)
        else:
            lstars.append(stars((255,255,255),"SadStar.png",
                [random.randrange(0,520),random.randrange(-300,-50)], ATTRIBUTES[1]))
            lstars[x].checkOverlap(lstars, 1)
            rstars.append(stars((255,255,255),"HappyStar.png",
                [random.randrange(600,1100),random.randrange(-300,-50)], ATTRIBUTES[0]))
            rstars[x].checkOverlap(rstars, 2)

    screen.blit(background,backgroundrec)
    global left_write, right_write
    global t0
    t0 = time.time()
    t1 = t0

    global alarm
    if level < 8:
        alarm-=level/2
    else:
        alarm = 6


    while EndGame==0: 
        gameClock.tick(FRAMERATE)
        gap = player2.distance+player1.distance
        # print gap
#         if time.time()-t0 > 5:
#             print "time"
#             t0 = time.time()
        if abs(gap)>25:
            seesaw.rotation(-(gap/(3500-(level-1)*1000)))
        else:
            seesaw.amount = 0.0
        global lives
        global score
        if lives == 0:
            # EndGame = 1
            # global score
            # global lives
            lives = 5
            score = 0
            return -1

        scoretext= str(score)
        scorewrite=font.render(scoretext, 1, [0,0,0])
        
        livetext=str(lives)
        liveswrite=font.render(livetext,1,[0,0,0])
        
        if time.time()-t0 >= alarm:
            # print "transition"
            transition = 1

        if time.time()-t1 <= 2.5:
            screen.blit(background, ((1200-writeLvl.get_width())/2, 350),
                ((1200-writeLvl.get_width())/2, 350, writeLvl.get_width(), writeLvl.get_height()))
        if time.time()-t1 <= 2:
            screen.blit(writeLvl, ((1200-writeLvl.get_width())/2, 350))
            
        if score == n:
            speed += .25
            n+=5
      
        if score == moreStars and starslimit < len(lstars):
            starslimit += 1
            moreStars += 5

        # lXVals = []
        # rXVals = []
        for x in range(0,starslimit):
            screen.blit(background,(lstars[x].rect.x, lstars[x].rect.y-10),(lstars[x].rect.x, lstars[x].rect.y-10, 80, 90))
            # lXVals.append(lstars[x].rect.x)
            screen.blit(background,(rstars[x].rect.x, rstars[x].rect.y-10),(rstars[x].rect.x, rstars[x].rect.y-10, 80, 90))
            # rXVals.append(rstars[x].rect.x)

        screen.blit(background,(player1.rect.x-10,player1.rect.y),(player1.rect.x-10,player1.rect.y,85,120))
        screen.blit(background,(player2.rect.x-10,player2.rect.y),(player2.rect.x-10,player2.rect.y, 85,120))
        screen.blit(background, (15,120), (15, 120, 1200, left_write.get_height()))
        screen.blit(left_write, (15,120))
        screen.blit(right_write, (640, 120))
        
        screen.blit(background,(seesaw.rect.x-10, seesaw.rect.y-10), 
            (seesaw.rect.x-10, seesaw.rect.y-10, seesaw.rect.width+20, seesaw.rect.height+20))
        screen.blit(seesaw.image, seesaw)

        offscreenStars = 0
        for x in range(0,starslimit):
            if player1.rect.colliderect(lstars[x].getHitBox()): #actions of the left side stars
                lstars[x].location[1] = -200
                lstars[x].location[0] = random.randrange(0,520)
                lstars[x].rect.x = lstars[x].location[0]
                lstars[x].rect.y = lstars[x].location[1]
                lstars[x].checkOverlap(lstars, 1)

                if lstars[x].attribute == correct_left:
                    score +=1
                else:
                    lives -=1
                lstars[x].update()
                j = random.randrange(0,len(ATTRIBUTES))
                lstars[x].attribute = ATTRIBUTES[j]
                lstars[x].image = pygame.image.load(FILENAMES[j]).convert_alpha() 
                lstars[x].image = pygame.transform.scale(lstars[x].image, (80,80))


            if player2.rect.colliderect(rstars[x].getHitBox()): #actions of the right side stars
                rstars[x].location[1] = -200
                rstars[x].location[0] = random.randrange(600,1100) 
                rstars[x].rect.x = rstars[x].location[0]
                rstars[x].rect.y = rstars[x].location[1]
                rstars[x].checkOverlap(rstars, 2)   
                if rstars[x].attribute == correct_right:
                    score +=1
                else:
                    lives -=1
                rstars[x].update()
                j = random.randrange(0,len(ATTRIBUTES))
                rstars[x].attribute = ATTRIBUTES[j]
                rstars[x].image = pygame.image.load(FILENAMES[j]).convert_alpha() 
                rstars[x].image = pygame.transform.scale(rstars[x].image, (80,80))

            lstars[x].fallingStar(speed, lstars)
            lstars[x].update()
            screen.blit(lstars[x].image, lstars[x])
            
            rstars[x].fallingStar2(speed,rstars)
            rstars[x].update()
            screen.blit(rstars[x].image, rstars[x])
            
#             global alarm
#             if time.time()-t0 >= alarm:
#                 if lstars[x].location[1]<810:
#                     onscreenStars += 1
#                 if rstars[x].location[1]<810:
#                     offscreenStars += 1
#                 if onscreenStars == 0:
#                     transition = 1
#                     #re-randomize phrase
#                     offscreenStars = 0
            if transition == 1:
                if lstars[x].isOnScreen == False:
                    offscreenStars += 1
                if rstars[x].isOnScreen == False:
                    offscreenStars += 1
                if offscreenStars == 2*starslimit:
                    offscreenStars = 0
                    transition = 0
                    correct_tuple = phrases(numPhrases)
                    # print correct_tuple
                    correct_left = ACTIONS_DICT[correct_tuple[0]]
                    correct_right = ACTIONS_DICT[correct_tuple[1]]
                    # print time.time()-t0
                    t0 = time.time()
                    
    
        screen.blit(player1.image,player1)
        screen.blit(player2.image,player2)
        screen.blit(background, (0, 0), (0, 0, 175, 86))
        screen.blit(scorewrite, (110,21))  
        screen.blit(background, (1026, 0), (1026, 0, 174, 86))
        screen.blit(liveswrite,(1150, 21))

        pygame.display.update()

        player1.move(1, seesaw)
        player2.move(2, seesaw)
    
        # print offscreenStar
        # print "CL", correct_left
        # print "CR", correct_right

        if score >= 15:
            lives = 5
            score = 0
            # EndGame = 1
            return level 

        # print abs(seesaw.direction)
        
        if abs(seesaw.direction) >= 15:
            lives = 5
            score = 0
            # EndGame = 1
            return -2

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                # global score
                # global lives
                lives = 5
                score = 0
                # EndGame = 1
                return 0



