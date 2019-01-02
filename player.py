import pygame
class Player:
	def __init__(self):
		self.rect = pygame.Rect(32, 32, 16, 16)
	
	def move(self,dx,dy):
		self.rect.x += dx
		self.rect.y += dy