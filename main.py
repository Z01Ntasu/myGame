import pygame
from player import Player
from apple import Apfel
from gameLogic import Logic

# Set up the Game
pygame.init()
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("First")

# Generate objects
player = Player()
apple = []
for i in range(0,20):
	apple.append(Apfel())
	
#Generate GameLogic
clock = pygame.time.Clock()	
game = Logic()
run = True


while run:
	clock.tick(120)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	win.fill((51,51,0))
	pygame.draw.rect(win, (255, 200, 0), player.rect)
	
	for ziel in apple:
		pygame.draw.rect(win, (255, 0, 0), ziel.rect)
	
	for i in range(0,len(apple)):
		if player.rect.colliderect(apple[i-1]):
			apple.remove(apple[i-1])
			game.score += 1
	
	
	
	
	game.keyDetection(player)
	game.texts(win)
	
	
	pygame.display.update()
	
	if len(apple) == 0:
		run = False
	
pygame.quit()
