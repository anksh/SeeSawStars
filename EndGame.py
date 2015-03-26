import pygame, time
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode([1200,700])
font = pygame.font.SysFont("Courier New", 96)
font2 = pygame.font.SysFont("Courier New", 36)
font.set_bold(True)

def GameOver(typeOf):
	# print "yoyo"
	text1 = "GAME OVER"
	text2 = "Press any key to return to the main menu"
	text3 = "You ran out of lives!"
	text4 = "The SeeSaw tilted too much!"
	text3_write = font2.render(text3, 1, [0,0,0])
	text4_write = font2.render(text4, 1, [0,0,0])
	text1_write = font.render(text1, 1, [0,0,0])
	text2_write = font2.render(text2, 1, [0,0,0])
	t0 = time.time()
	screen.fill([245,245,245])
	while True:
		screen.fill([245,245,245])
		screen.blit(text1_write, ((1200-text1_write.get_width())/2,100))
		screen.blit(text2_write, ((1200-text2_write.get_width())/2,400))
		if typeOf == -1:
			screen.blit(text3_write, ((1200-text3_write.get_width())/2,500))
		if typeOf == -2:
			screen.blit(text4_write, ((1200-text4_write.get_width())/2,500))
		pygame.display.update()
		if time.time()-t0>=1.5:
			for event in pygame.event.get():
				if event.type == QUIT or event.type == KEYDOWN:
					return
