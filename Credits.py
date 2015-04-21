import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode([1200,700])


def credits():
	background = pygame.image.load("CreditsScreen.png")
	backgroundrec = background.get_rect()
	while True:
		screen.blit(background, backgroundrec)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				return
			if event.type == MOUSEBUTTONDOWN:
				location = pygame.mouse.get_pos()
				if location[1] > 575 and location[1] < 675:
					if location[0] > 490 and location[0] < 710:
						return