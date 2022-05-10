import pygame
import os
import random

class mapGen:

	def __init__(self, max):
		self.maps = ["map0", "map1", "map2", "map3", "map4", "map5", "map6", "map7", "map8", "map9", "map10", "map11", "map12", "map13", "map14", "map15", "map16", "map17", "map18", "map19", "map20"]
		self.board = [[None,None,None,None,None,None,None,None,None,None,],
			 	 	  [None,None,None,None,None,None,None,None,None,None,],
			 	 	  [None,None,None,None,None,None,None,None,None,None,],
			 	 	  [None,None,None,None,None,None,None,None,None,None,],
			 	 	  [None,None,None,None,None,None,None,None,None,None,],
			 	 	  [None,None,None,None,None,None,None,None,None,None,],
			 	 	  [None,None,None,None,None,None,None,None,None,None,],
			 	 	  [None,None,None,None,None,None,None,None,None,None,],
			 	 	  [None,None,None,None,None,None,None,None,None,None,],
			 	 	  [None,None,None,None,None,None,None,None,None,None,]]
		self.max = max

	def addDoorUp(self, row, col):
		self.board[row][col][2] = True

	def addDoorDown(self, row, col):
		self.board[row][col][3] = True

	def addDoorLeft(self, row, col):
		self.board[row][col][4] = True

	def addDoorRight(self, row, col):
		self.board[row][col][5] = True


	def generate(self):
		row = random.randint(0, 9)
		col = random.randint(0, 9)
		START_ROW = row
		START_COL = col
		i = 0
		self.board[row][col] = ["start", False, None, None, None, None] #make a board[][] = None or ["map", True, Door, Door, Door, Door] = [map, safe?, door?, door?, door?, door?]
		while i <= self.max:
			direction = random.randint(1, 4)
			if direction == 1: #up
				if(row - 1) >= 0:
					row -= 1
					if self.board[row][col] == None:
						mapi = random.randint(0, len(self.maps) - 1)
						self.board[row][col] = [self.maps[mapi], True, None, None, None, None] #make a board[][] = None or ["map", True, Door, Door, Door, Door] = [map, safe?, door?, door?, door?, door?]
						del self.maps[mapi]
						i += 1
					self.addDoorUp(row+1, col)
					self.addDoorDown(row, col)
			elif direction == 2:
				if(row + 1) <= 9:
					row += 1
					if self.board[row][col] == None:
						mapi = random.randint(0, len(self.maps) - 1)
						self.board[row][col] = [self.maps[mapi], True, None, None, None, None] #make a board[][] = None or ["map", True, Door, Door, Door, Door] = [map, safe?, door?, door?, door?, door?]
						del self.maps[mapi]
						i += 1
					self.addDoorDown(row-1, col)
					self.addDoorUp(row, col)
			elif direction == 3:
				if(col - 1) >= 0:
					col -= 1
					if self.board[row][col] == None:
						mapi = random.randint(0, len(self.maps) - 1)
						self.board[row][col] = [self.maps[mapi], True, None, None, None, None] #make a board[][] = None or ["map", True, Door, Door, Door, Door] = [map, safe?, door?, door?, door?, door?]
						del self.maps[mapi]
						i += 1
					self.addDoorLeft(row, col+1)
					self.addDoorRight(row, col)
			else:
				if(col + 1) <= 9:
					col += 1
					if self.board[row][col] == None:
						mapi = random.randint(0, len(self.maps) - 1)
						self.board[row][col] = [self.maps[mapi], True, None, None, None, None] #make a board[][] = None or ["map", True, Door, Door, Door, Door] = [map, safe?, door?, door?, door?, door?]
						del self.maps[mapi]
						i += 1
					self.addDoorLeft(row, col-1)
					self.addDoorRight(row, col)
		return START_ROW, START_COL

	def printBoard(self):
		for i in range(0, 10):
			print(self.board[i])
		print()

	def getRoom(self, row, col):
		return self.board[row][col]


class Object:

	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def getObject(self):
		return pygame.Rect(self.x, self.y, self.width, self.height)


	

width, height = 900, 500
WIN = pygame.display.set_mode((width, height))
FPS = 60
Player_width, Player_height = 50, 40
Vel = 5


BACKGROUND_IMAGE = pygame.image.load(os.path.join('assets', 'maptest2.png')).convert_alpha()
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (width, height))
TOPDOOD_IMAGE = pygame.image.load(os.path.join('assets', 'TopDoor.png')).convert_alpha()
TOPDOOR = pygame.transform.scale(TOPDOOD_IMAGE, (width, height))
BOTTOMDOOR_IMAGE = pygame.image.load(os.path.join('assets', 'BottomDoor.png')).convert_alpha()
BOTTOMDOOR = pygame.transform.scale(BOTTOMDOOR_IMAGE, (width, height))
LEFTDOOR_IMAGE = pygame.image.load(os.path.join('assets', 'LeftDoor.png')).convert_alpha()
LEFTDOOR = pygame.transform.scale(LEFTDOOR_IMAGE, (width, height))
RIGHTDOOR_IMAGE = pygame.image.load(os.path.join('assets', 'RightDoor.png')).convert_alpha()
RightDOOR = pygame.transform.scale(RIGHTDOOR_IMAGE, (width, height))
PLAYER_IMAGE = pygame.image.load(os.path.join('assets', 'Player.png')).convert_alpha()
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (Player_width, Player_height))
PLAYER_IMAGE_COPY = pygame.transform.scale(PLAYER_IMAGE.copy(), (Player_width, Player_height))
PLAYER_IMAGE_FLIP = pygame.transform.flip(PLAYER_IMAGE_COPY, True, False)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)






'''
PLAYER_IMAGE = pygame.image.load(os.path.join('assets', 'Player.png')).convert_alpha()
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (Player_width, Player_height))
PLAYER_IMAGE_COPY = pygame.transform.scale(PLAYER_IMAGE.copy(), (Player_width, Player_height))
PLAYER_IMAGE_FLIP = pygame.transform.flip(PLAYER_IMAGE_COPY, True, False)
'''

#right frames
SPRINT1_IMAGE = pygame.image.load(os.path.join('assets', 'sprint1.png')).convert_alpha()
SPRINT1 = pygame.transform.scale(SPRINT1_IMAGE, (Player_width, Player_height))
SPRINT2_IMAGE = pygame.image.load(os.path.join('assets', 'sprint2.png')).convert_alpha()
SPRINT2 = pygame.transform.scale(SPRINT2_IMAGE, (Player_width, Player_height))
SPRINT3_IMAGE = pygame.image.load(os.path.join('assets', 'sprint3.png')).convert_alpha()
SPRINT3 = pygame.transform.scale(SPRINT3_IMAGE, (Player_width, Player_height))
SPRINT4_IMAGE = pygame.image.load(os.path.join('assets', 'sprint4.png')).convert_alpha()
SPRINT4 = pygame.transform.scale(SPRINT4_IMAGE, (Player_width, Player_height))
SPRINT5_IMAGE = pygame.image.load(os.path.join('assets', 'sprint5.png')).convert_alpha()
SPRINT5 = pygame.transform.scale(SPRINT5_IMAGE, (Player_width, Player_height))
SPRINT6_IMAGE = pygame.image.load(os.path.join('assets', 'sprint6.png')).convert_alpha()
SPRINT6 = pygame.transform.scale(SPRINT6_IMAGE, (Player_width, Player_height))
SPRINT7_IMAGE = pygame.image.load(os.path.join('assets', 'sprint7.png')).convert_alpha()
SPRINT7 = pygame.transform.scale(SPRINT7_IMAGE, (Player_width, Player_height))
SPRINT8_IMAGE = pygame.image.load(os.path.join('assets', 'sprint8.png')).convert_alpha()
SPRINT8 = pygame.transform.scale(SPRINT8_IMAGE, (Player_width, Player_height))

SPRINT = [SPRINT1, SPRINT1, 
		  SPRINT2, SPRINT2, 
		  SPRINT3, SPRINT3, 
		  SPRINT4, SPRINT4, 
		  SPRINT5, SPRINT5, 
		  SPRINT6, SPRINT6, 
		  SPRINT7, SPRINT7, 
		  SPRINT8, SPRINT8]


#left frames
SPRINT1_IMAGE_LEFT = pygame.image.load(os.path.join('assets', 'sprint1.png')).convert_alpha()
SPRINT1_LEFT = pygame.transform.flip(pygame.transform.scale(SPRINT1_IMAGE, (Player_width, Player_height)), True, False)
SPRINT2_IMAGE_LEFT = pygame.image.load(os.path.join('assets', 'sprint2.png')).convert_alpha()
SPRINT2_LEFT = pygame.transform.flip(pygame.transform.scale(SPRINT2_IMAGE, (Player_width, Player_height)), True, False)
SPRINT3_IMAGE_LEFT = pygame.image.load(os.path.join('assets', 'sprint3.png')).convert_alpha()
SPRINT3_LEFT = pygame.transform.flip(pygame.transform.scale(SPRINT3_IMAGE, (Player_width, Player_height)), True, False)
SPRINT4_IMAGE_LEFT = pygame.image.load(os.path.join('assets', 'sprint4.png')).convert_alpha()
SPRINT4_LEFT = pygame.transform.flip(pygame.transform.scale(SPRINT4_IMAGE, (Player_width, Player_height)), True, False)
SPRINT5_IMAGE_LEFT = pygame.image.load(os.path.join('assets', 'sprint5.png')).convert_alpha()
SPRINT5_LEFT = pygame.transform.flip(pygame.transform.scale(SPRINT5_IMAGE, (Player_width, Player_height)), True, False)
SPRINT6_IMAGE_LEFT = pygame.image.load(os.path.join('assets', 'sprint6.png')).convert_alpha()
SPRINT6_LEFT = pygame.transform.flip(pygame.transform.scale(SPRINT6_IMAGE, (Player_width, Player_height)), True, False)
SPRINT7_IMAGE_LEFT = pygame.image.load(os.path.join('assets', 'sprint7.png')).convert_alpha()
SPRINT7_LEFT = pygame.transform.flip(pygame.transform.scale(SPRINT7_IMAGE, (Player_width, Player_height)), True, False)
SPRINT8_IMAGE_LEFT = pygame.image.load(os.path.join('assets', 'sprint8.png')).convert_alpha()
SPRINT8_LEFT = pygame.transform.flip(pygame.transform.scale(SPRINT8_IMAGE, (Player_width, Player_height)), True, False)

SPRINT_LEFT = [SPRINT1_LEFT, SPRINT1_LEFT,
		  		SPRINT2_LEFT, SPRINT2_LEFT,
		  		SPRINT3_LEFT, SPRINT3_LEFT,
		  		SPRINT4_LEFT, SPRINT4_LEFT, 
		  		SPRINT5_LEFT, SPRINT5_LEFT, 
		  		SPRINT6_LEFT, SPRINT6_LEFT, 
		  		SPRINT7_LEFT, SPRINT7_LEFT, 
		  		SPRINT8_LEFT, SPRINT8_LEFT]


#idle frames
IDLE1_IMAGE = pygame.image.load(os.path.join('assets', 'idle1.png')).convert_alpha()
IDLE1 = pygame.transform.scale(SPRINT1_IMAGE, (Player_width, Player_height))
IDLE2_IMAGE = pygame.image.load(os.path.join('assets', 'idle2.png')).convert_alpha()
IDLE2 = pygame.transform.scale(SPRINT2_IMAGE, (Player_width, Player_height))
IDLE3_IMAGE = pygame.image.load(os.path.join('assets', 'idle3.png')).convert_alpha()
IDLE3 = pygame.transform.scale(SPRINT3_IMAGE, (Player_width, Player_height))
IDLE4_IMAGE = pygame.image.load(os.path.join('assets', 'idle4.png')).convert_alpha()
IDLE4 = pygame.transform.scale(SPRINT4_IMAGE, (Player_width, Player_height))
IDLE5_IMAGE = pygame.image.load(os.path.join('assets', 'idle5.png')).convert_alpha()
IDLE5 = pygame.transform.scale(SPRINT5_IMAGE, (Player_width, Player_height))
IDLE6_IMAGE = pygame.image.load(os.path.join('assets', 'idle6.png')).convert_alpha()
IDLE6 = pygame.transform.scale(SPRINT6_IMAGE, (Player_width, Player_height))
IDLE7_IMAGE = pygame.image.load(os.path.join('assets', 'idle7.png')).convert_alpha()
IDLE7 = pygame.transform.scale(SPRINT7_IMAGE, (Player_width, Player_height))
IDLE8_IMAGE = pygame.image.load(os.path.join('assets', 'idle8.png')).convert_alpha()
IDLE8 = pygame.transform.scale(SPRINT8_IMAGE, (Player_width, Player_height))

IDLE = [IDLE1, IDLE1,
		IDLE2, IDLE2,
		IDLE3, IDLE3,
		IDLE4, IDLE4,
		IDLE5, IDLE5,
		IDLE6, IDLE6,
		IDLE7, IDLE7,
		IDLE8, IDLE8,]





#drawing
def Fade_to_black(width, height, CURRENT_PLAYER, Player, map, row, col): 
    fade = pygame.Surface((width, height))
    fade.fill(BLACK)
    for alpha in range(0, 255):
        fade.set_alpha(alpha)
        Draw_window(CURRENT_PLAYER, Player, map, row, col)
        WIN.blit(fade, (0,0))
        pygame.display.update()

def Draw_window(CURRENT_PLAYER, Player_object, map, row, col):
	WIN.blit(BACKGROUND, (0,0))
	Draw_doors(map, row, col)
	WIN.blit(CURRENT_PLAYER, (Player_object.x, Player_object.y))
	pygame.display.update()

def Draw_doors(map, row, col):
	if map.getRoom(row, col)[2] == True:
		WIN.blit(TOPDOOR, (0,0))
	if map.getRoom(row, col)[3] == True:
		WIN.blit(BOTTOMDOOR, (0,0))
	if map.getRoom(row, col)[4] == True:
		WIN.blit(LEFTDOOR, (0,0))
	if map.getRoom(row, col)[5] == True:
		WIN.blit(RightDOOR, (0,0))

def Player_walk_movement(keys_pressed, player):
	if (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]) and player.x - Vel > 68: #left
		player.x -= Vel
	if (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]) and player.x - Vel < width - 130: #right
		player.x += Vel
	if (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]) and player.y - Vel > 50: #up
		player.y -= Vel
	if (keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]) and player.y - Vel < height - 105: #down
		player.y += Vel

def Determine_collsion_side(player, Object):
    if player.midtop[1] > Object.midtop[1]:
        return "top"
    elif player.midleft[0] > Object.midleft[0]:
        return "left"
    elif player.midright[0] < Object.midright[0]:
        return "right"
    else:
        return "bottom"
    return

def Collision_movement(player, Objects, direction):
	if direction == "top":
		player.top = Objects.bottom
	elif direction == "left":
		player.left = Objects.right
	elif direction == "right":
		player.right = Objects.left
	elif direction == "bottom":
		player.bottom = Objects.top

def Door_collision(CURRENT_PLAYER, Player, map, row, col):
	if Player.y <= 60 and (Player.x > 415 and Player.x < 460):
		if map.getRoom(row, col)[2] == True:
			row -= 1
			Fade_to_black(width, height, CURRENT_PLAYER, Player, map, row, col)
			Player.x = 450 - (Player_width/2)
			Player.y = 250 - (Player_height/2)
	elif Player.y >= 400 and (Player.x > 415 and Player.x < 460):
		if map.getRoom(row, col)[3] == True:
			row += 1
			Fade_to_black(width, height, CURRENT_PLAYER, Player, map, row, col)
			Player.x = 450 - (Player_width/2)
			Player.y = 250 - (Player_height/2)
	elif Player.x <= 70 and (Player.y > 195 and Player.y < 235):
		if map.getRoom(row, col)[4] == True:
			col -= 1
			Fade_to_black(width, height, CURRENT_PLAYER, Player, map, row, col)
			Player.x = 450 - (Player_width/2)
			Player.y = 250 - (Player_height/2)
	elif Player.x >= 775 and (Player.y > 195 and Player.y < 235):
		if map.getRoom(row, col)[5] == True:
			col += 1
			Fade_to_black(width, height, CURRENT_PLAYER, Player, map, row, col)
			Player.x = 450 - (Player_width/2)
			Player.y = 250 - (Player_height/2)

def Walk_left_animation():
	pass

def Walk_right_animation():
	pass

#player?

#object creation:
box = Object(695, 338, 20, 30)
box2 = Object(735, 318, 20, 50)
objects = []
objects.append(box.getObject())
objects.append(box2.getObject())




def main():
	#Player
	player = pygame.Rect(450 - (Player_width/2), 250 - (Player_height/2), Player_width, Player_height)
	value = 0
	image = SPRINT[value]
	moving = False
	left = False
	right = True

	#mapGen
	map = mapGen(17) #consider moving this up and making it a global variable?
	row, col = map.generate()

	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					moving = False
					value = 0

		for i in objects:
			collide = pygame.Rect.colliderect(player, i)
			if collide:
				direction = Determine_collsion_side(player, i)
				Collision_movement(player, i, direction)

		keys_pressed = pygame.key.get_pressed() #gets the pressed keys
		if keys_pressed[pygame.K_ESCAPE]:
			run = False
		Player_walk_movement(keys_pressed, player)
		if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]: #need to flip model?
			image = PLAYER_IMAGE_FLIP
			moving = True
			left = True
			right = False
		elif keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
			image = PLAYER
			moving = True
			right = True
			left = False


		if moving:
			value  += 1
			if value >= len(SPRINT):
				value = 0
			if right:
				image = SPRINT[value]
			elif left:
				image = SPRINT_LEFT[value]
		else:
			value += 1
			if value >= len(IDLE):
				value = 0
			image = IDLE[value]

		Door_collision(image, player, map, row, col) #check door collision
		Draw_window(image, player, map, row, col)

	pygame.quit()

if __name__ == "__main__":
	main()