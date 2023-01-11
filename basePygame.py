
import sys, pygame
pygame.init()
w,h = 1024, 768
screen = pygame.display.set_mode((w,h))
screen.fill((0,0,255))



pygame.draw.aaline(screen, (255,100,100), (100,100), (150,100))
pygame.draw.aaline(screen, (255,100,100), (150,100), (200,50))
pygame.draw.aaline(screen, (255,100,100), (200,50), (250,100))
pygame.draw.aaline(screen, (255,100,100), (250,100), (300,100))





play = True
clock = pygame.time.Clock()

while play:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			play = False
		if event.type == pygame.KEYUP:
			print(event.key, event.unicode, event.scancode)
			if event.key == pygame.K_ESCAPE:
				play = False

	clock.tick(60)
	pygame.display.flip()




