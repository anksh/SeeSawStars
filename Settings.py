import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode([1200,700])


def settingsMenu():
	background = pygame.image.load("SettingsScreen.png")
	backgroundrec = background.get_rect()
	while True:
		screen.blit(background, backgroundrec)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				return
			if event.type == MOUSEBUTTONDOWN:
				location = pygame.mouse.get_pos()
				if location[1] > 270 and location[1] < 586:
					if location[0] > 91 and location[0] < 305:
						settingsFile = open("settings.txt", "wb")
						settingsFile.write("Background.png")
						settingsFile.close()
						return
					if location[0] > 493 and location[0] < 707:
						settingsFile = open("settings.txt", "wb")
						settingsFile.write("RainbowBackground.png")
						settingsFile.close()
						return
					if location[0] > 894 and location[0] < 1103:
						settingsFile = open("settings.txt", "wb")
						settingsFile.write("StarryBackground.png")
						settingsFile.close()
						return



