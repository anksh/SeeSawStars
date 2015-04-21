
import pygame, os, random, math, string
from pygame.locals import *
from pygame.tests.base_test import pygame_quit
pygame.init()
cheattext = None
screen = pygame.display.set_mode([1200,700])
import SeeSawStars

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return (event.key, event.unicode)
  
    else:
      pass

def display_box(screen, message):
  "Print a message in the middle of the screen"
  fontobject = pygame.font.SysFont("Courier New", 32)
  pygame.draw.rect(screen, (0,211,224),((screen.get_width() / 2) - 200,(screen.get_height() / 2) - 10, 800,50), 0)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (0,0,0)),
                ((screen.get_width() / 2) - 200, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + string.join(current_string,""))
  while 1:
    (inkey, unichr) = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    else:
        current_string += unichr
    display_box(screen, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")
  
def main():
 global cheattext
 
 background = pygame.image.load("CheatCode1.png")
 backgroundrec = background.get_rect()

 Done = False
 while True:
     
     
              
     
     for event in pygame.event.get():
         
         if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                Done = True
                return
            
         if event.type == MOUSEBUTTONDOWN:
            location = pygame.mouse.get_pos()
            if location[1] > 575 and location[1] < 675:
                if location[0] > 490 and location[0] < 710:
                    Done = True
                    return
                    
         if not Done:
             
             screen.blit(background, backgroundrec)
             cheattext = ask(screen, "Cheatcode")
             
             fo = open("cheatfile.txt", "wb")
             fo.write(cheattext)  
             pygame.display.update()
             fo.close()
             return
 

     
     
     
if __name__ == '__main__':
    main()              
     
 

 

#if __name__ == '__main__': main()