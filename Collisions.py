#This file handles the collision between the players and stars


def collide(obj1, obj2, score, lives):
	if pygame.sprite.collide_rect(obj1, obj2):
		if type(obj1) is goodstar:
			#print True
			score += 1
		if type(obj1) is badstar:
			lives -= 1
			#print "The Goalie got his hands to that!"