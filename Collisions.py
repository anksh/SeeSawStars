#This file handles the collision between the players and stars


def collide(obj1, obj2, score, lives):
	if pygame.sprite.collide_rect(obj1, obj2):
		if obj2.attribute == "good":
			#print True
			score += 1
		if obj2.attribute == "bad":
			lives -= 1
			#print "The Goalie got his hands to that!"