import pygame
class Score:
	def __init__(self):
		self.score = 0

	def texts(self,win,x,y,text):
		font=pygame.font.Font(None,30)
		scoretext=font.render(text+str(self.score), 1,(255,255,255))
		win.blit(scoretext, (x, y))