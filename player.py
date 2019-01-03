import pygame
class Player:
	def __init__(self,x,y):
		self.rect = pygame.Rect(x, y, 16, 16)
	
	def move(self,dx,dy):
		self.rect.x += dx
		self.rect.y += dy