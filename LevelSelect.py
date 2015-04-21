import pygame
from pygame.locals import *
import GameMech
import EndGame

pygame.init()

screen = pygame.display.set_mode([1200,700])

def selectLevel():
	background = pygame.image.load("LevelSelect.png")
	backgroundrec = background.get_rect()
	option = 0
	enteredGame = False
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and K_ESCAPE):
				return -1
			if event.type == MOUSEBUTTONDOWN:
				location = pygame.mouse.get_pos()
				if location[1] > 575 and location[1] < 675:
					if location[0] > 490 and location[0] < 710:
						return 1
				if location[1] > 300 and location[1] < 500:
					if location[0] > 25 and location[0] < 375:
						option = GameMech.play(1)
						enteredGame = True
					if location[0] > 425 and location[0] < 775:
						option = GameMech.play(2)
						enteredGame = True
					if location[0] > 825 and location[0] < 1175:
						option = GameMech.play(3)
						enteredGame = True

		if enteredGame:
			if option == 0:
				enteredGame = False
				return 0
			if option > 0:
				option = GameMech.play(option+1)
			if option < 0:
				EndGame.GameOver(option)
				enteredGame = False
				return 0
				
		if not enteredGame:
			screen.blit(background, backgroundrec)
			pygame.display.update()
