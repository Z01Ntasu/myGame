import pygame
from player import Player
from apple import Apfel
from gameLogic import Logic
from score import Score

# Set up the Game
pygame.init()
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("First")

# Generate objects
player = Player(32,32)
gegner = Player(50,32)
apple = []
for i in range(0,30):
	apple.append(Apfel())
	

#Generate GameLogic
clock = pygame.time.Clock()	
game = Logic()
run = True
playerscore = Score()
enemiescore = Score()


#Apple Collison Checking
doppelte= True
while doppelte:
	doppelte = game.appleCollsion(apple)

#Game Schleife
while run:
	clock.tick(120)
	#Abbruch Bedingungen
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	if len(apple) == 0:
		run = False
	
	#Charakter zeichnen
	win.fill((51,51,0))
	pygame.draw.rect(win, (255, 200, 0), player.rect)
	pygame.draw.rect(win, (0, 0, 255), gegner.rect)
	for ziel in apple:
		pygame.draw.rect(win, (255, 0, 0), ziel.rect)
	
	#Collison Checking
	for i in range(0,len(apple)):
		if player.rect.colliderect(apple[i-1]):
			apple.remove(apple[i-1])
			playerscore.score += 1
			
	for i in range(0,len(apple)):
		if gegner.rect.colliderect(apple[i-1]):
			apple.remove(apple[i-1])
			enemiescore.score += 1
	
	#Game logic verwarlten
	game.keyDetection(player)
	playerscore.texts(win,5,5,"Player-Score : ")
	enemiescore.texts(win,600,5,"Enemy-Score : ")
	game.gegnerMove(gegner,apple)
	
	#Bild aktualisieren
	pygame.display.update()

print("You : ",playerscore.score,"\nEnemy : ",enemiescore.score)	
pygame.quit()
