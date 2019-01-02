import pygame
import random
class Apfel:
	def __init__(self):
		self.rect = pygame.Rect(random.randint(50, 500), random.randint(50,500), 16, 16)
