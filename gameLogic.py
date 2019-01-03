import pygame
from apple import Apfel
class Logic:

	def keyDetection(self,player):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			player.move(-1,0)
		if keys[pygame.K_RIGHT]:
			player.move(1,0)
		if keys[pygame.K_UP]:
			player.move(0,-1)
		if keys[pygame.K_DOWN]:
			player.move(0,1)
	
	def gegnerMove(self,gegner,apple):
		if len(apple) == 0:
			print()
		else:
			if gegner.rect.x > apple[0].rect.x:
				gegner.move(-1,0)
			if gegner.rect.x < apple[0].rect.x:
				gegner.move(1,0)
			if gegner.rect.y > apple[0].rect.y:
				gegner.move(0,-1)
			if gegner.rect.y < apple[0].rect.y:
				gegner.move(0,1)
	
		
	def appleCollsion(self,apple):
		for i in range (0,len(apple)-1):
			for j in range (i+1,len(apple)-1):
				if apple[i].rect.colliderect(apple[j]):
					apple.remove(apple[i])
					apple.append(Apfel())
					return True	
		return False