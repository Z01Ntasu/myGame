import pygame
class Logic:
	def __init__(self):
		self.score = 0
		
		
	def texts(self,win):
		font=pygame.font.Font(None,30)
		scoretext=font.render("Score:"+str(self.score), 1,(255,255,255))
		win.blit(scoretext, (5, 5))
	
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