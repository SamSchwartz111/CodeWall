import pygame
import os

width, height = 900, 500
WIN = pygame.display.set_mode((width, height))
FPS = 60
Player_width, Player_height = 60, 40
Vel = 5


BACKGROUND_IMAGE = pygame.image.load(os.path.join('assets', 'maptest.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (width, height))
PLAYER_IMAGE = pygame.image.load(os.path.join('assets', 'Player.png'))
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (Player_width, Player_height))
WHITE = (255, 255, 255)

def draw_window(Player):
	WIN.blit(BACKGROUND, (0,0))
	WIN.blit(PLAYER, (Player.x, Player.y))

	pygame.display.update()

def Player_walk_movement(keys_pressed, player):
	if keys_pressed[pygame.K_a] and player.x - Vel > 68: #left
		player.x -= Vel
	if keys_pressed[pygame.K_d] and player.x - Vel < width - 150: #right
		player.x += Vel
	if keys_pressed[pygame.K_w] and player.y - Vel > 55: #up
		player.y -= Vel
	if keys_pressed[pygame.K_s] and player.y - Vel < height - 110: #down
		player.y += Vel

def main():
	player = pygame.Rect(450 - (Player_width/2), 250 - (Player_height/2), Player_width, Player_height)
	box = pygame.Rect(690, 360, 20, 25)
	box2 = pygame.Rect(730, 340, 20, 50)
	objects = []
	objects.append(box)
	objects.append(box2)


	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False



		for i in objects:
			collide = pygame.Rect.colliderect(player, i)
			if collide:
				player.bottom = i.top
		keys_pressed = pygame.key.get_pressed()
		Player_walk_movement(keys_pressed, player)

		draw_window(player)

	pygame.quit()

if __name__ == "__main__":
	main()