import pygame
from player import Player
from apple import Apfel
pygame.init()

win = pygame.display.set_mode((800,600))
pygame.display.set_caption("First")


player = Player()
apple = []
for i in range(0,8):
	apple.append(Apfel())

clock = pygame.time.Clock()	


run = True
while run:
	
	clock.tick(120)
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			run = False
	
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		player.move(-1,0)
	if keys[pygame.K_RIGHT]:
		player.move(1,0)
	if keys[pygame.K_UP]:
		player.move(0,-1)
	if keys[pygame.K_DOWN]:
		player.move(0,1)
	
	win.fill((51,51,0))
	pygame.draw.rect(win, (255, 200, 0), player.rect)
	
	for ziel in apple:
		pygame.draw.rect(win, (255, 0, 0), ziel.rect)
	
	
	for i in range(0,len(apple)):
		if player.rect.colliderect(apple[i-1]):
			apple.remove(apple[i-1])
			print("alarm")
			
	if len(apple) == 0:
		run = False
	
	
	pygame.display.update()
	
pygame.quit()



