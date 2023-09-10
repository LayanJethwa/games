import pygame # Module imports
import os
import sys
import time
import pyganim
import math

pygame.init() # Initialise PyGame

black = (0,0,0) # Colour variables
white = (255,255,255)
purple = (108,0,216)
red = (255,0,0)

instruction_loop = True # Main loops initialise
main_room_loop = False
puzzle_room_loop = False
computer_room_loop = False
memory_room_loop = False
hall_room_loop = False
logic_room_loop = False
trivia_room_loop = False
boss_room_loop = False
developer_mode_loop = False
running = True
clock = time.time()
boss_clock = time.time()
tile_clock = time.time()
move = 0.3
developer_mode = False
lives = 3
stop = False

password_active = False # Developer mode variables
password_text = ''
input_rect = pygame.Rect(350, 375, 100, 50)
password_font = pygame.font.SysFont(None, 40)
password_complete = False
lines_true = False

screen = pygame.display.set_mode((800, 800)) # Main screen
pygame.display.set_caption("Secrets of the Altar")

b_main_room = pygame.image.load(os.path.join("Textures", "Main Room", "main_room.png")).convert() # Import textures
character = pygame.image.load(os.path.join("Textures", "character1.png")).convert_alpha()
characterleft = pygame.image.load(os.path.join("Textures", "character1left.png")).convert_alpha()
characterright = pygame.image.load(os.path.join("Textures", "character1right.png")).convert_alpha()
circle = pygame.image.load(os.path.join("Textures", "Main Room", "altar_circle.png")).convert()
cross = pygame.image.load(os.path.join("Textures", "Main Room", "altar_cross.png")).convert()
square = pygame.image.load(os.path.join("Textures", "Main Room", "altar_square.png")).convert()
triangle = pygame.image.load(os.path.join("Textures", "Main Room", "altar_triangle.png")).convert()
circle_lit = pygame.image.load(os.path.join("Textures", "Main Room", "altar_circle_lit.png")).convert()
cross_lit = pygame.image.load(os.path.join("Textures", "Main Room", "altar_cross_lit.png")).convert()
square_lit = pygame.image.load(os.path.join("Textures", "Main Room", "altar_square_lit.png")).convert()
triangle_lit = pygame.image.load(os.path.join("Textures", "Main Room", "altar_triangle_lit.png")).convert()
mid1 = pygame.image.load(os.path.join("Textures", "Main Room", "altar_mid1.png")).convert()
mid2 = pygame.image.load(os.path.join("Textures", "Main Room", "altar_mid2.png")).convert()
mid3 = pygame.image.load(os.path.join("Textures", "Main Room", "altar_mid3.png")).convert()
mid4 = pygame.image.load(os.path.join("Textures", "Main Room", "altar_mid4.png")).convert()
mid1_on = pygame.image.load(os.path.join("Textures", "Main Room", "altar_mid1_on.png")).convert()
mid2_on = pygame.image.load(os.path.join("Textures", "Main Room", "altar_mid2_on.png")).convert()
mid3_on = pygame.image.load(os.path.join("Textures", "Main Room", "altar_mid3_on.png")).convert()
mid4_on = pygame.image.load(os.path.join("Textures", "Main Room", "altar_mid4_on.png")).convert()
arrow = pygame.image.load(os.path.join("Textures", "arrow.png")).convert_alpha()
arrow1 = arrow.get_rect()
b_puzzle_room = pygame.image.load(os.path.join("Textures", "Puzzle Room", "puzzle_room.png")).convert()
puzzle_boss_1 = pygame.image.load(os.path.join("Textures", "Puzzle Room", "puzzle_boss-1.png")).convert_alpha()
puzzle_boss_2 = pygame.image.load(os.path.join("Textures", "Puzzle Room", "puzzle_boss-2.png")).convert_alpha()
puzzle_boss_3 = pygame.image.load(os.path.join("Textures", "Puzzle Room", "puzzle_boss-3.png")).convert_alpha()
puzzle_boss_4 = pygame.image.load(os.path.join("Textures", "Puzzle Room", "puzzle_boss-4.png")).convert_alpha()
puzzle_boss_5 = pygame.image.load(os.path.join("Textures", "Puzzle Room", "puzzle_boss-5.png")).convert_alpha()
puzzle_boss_6 = pygame.image.load(os.path.join("Textures", "Puzzle Room", "puzzle_boss-6.png")).convert_alpha()
b_computer_room = pygame.image.load(os.path.join("Textures", "Computer Room", "computer_room.png")).convert()
b_memory_room = pygame.image.load(os.path.join("Textures", "Memory Room", "memory_room.png")).convert()
tile_off = pygame.image.load(os.path.join("Textures", "Memory Room", "tile_off.png")).convert_alpha()
tile_on = pygame.image.load(os.path.join("Textures", "Memory Room", "tile_on.png")).convert()
collision_tile = pygame.image.load(os.path.join("Textures", "Memory Room", "collision_tile.png")).convert_alpha()
tile_off_cut = pygame.image.load(os.path.join("Textures", "Memory Room", "tile_off_cut.png")).convert_alpha()
tile_on_cut = pygame.image.load(os.path.join("Textures", "Memory Room", "tile_on_cut.png")).convert()
memory_button_g = pygame.image.load(os.path.join("Textures", "Memory Room", "green_button.png")).convert()
memory_button_r = pygame.image.load(os.path.join("Textures", "Memory Room", "red_button.png")).convert()
b_hall_room = pygame.image.load(os.path.join("Textures", "Hall Room", "hall_room.png")).convert()
b_logic_room = pygame.image.load(os.path.join("Textures", "Logic Room", "logic_room.png")).convert()
gamer = pygame.image.load(os.path.join("Textures", "Logic Room", "gamer.png")).convert_alpha()
b_trivia_room = pygame.image.load(os.path.join("Textures", "Trivia Room", "trivia_room.png")).convert()
a_image = pygame.image.load(os.path.join("Textures", "Trivia Room", "A.png")).convert()
b_image = pygame.image.load(os.path.join("Textures", "Trivia Room", "B.png")).convert()
c_image = pygame.image.load(os.path.join("Textures", "Trivia Room", "C.png")).convert()
d_image = pygame.image.load(os.path.join("Textures", "Trivia Room", "D.png")).convert()
red_cross = pygame.image.load(os.path.join("Textures", "Trivia Room", "cross.png")).convert_alpha()
green_tick = pygame.image.load(os.path.join("Textures", "Trivia Room", "tick.png")).convert_alpha()
bar1 = pygame.image.load(os.path.join("Textures", "Trivia Room", "bar1.png")).convert()
bar2 = pygame.image.load(os.path.join("Textures", "Trivia Room", "bar2.png")).convert()
bar3 = pygame.image.load(os.path.join("Textures", "Trivia Room", "bar3.png")).convert()
bar4 = pygame.image.load(os.path.join("Textures", "Trivia Room", "bar4.png")).convert()
bar5 = pygame.image.load(os.path.join("Textures", "Trivia Room", "bar5.png")).convert()
bar6 = pygame.image.load(os.path.join("Textures", "Trivia Room", "bar6.png")).convert()
bar7 = pygame.image.load(os.path.join("Textures", "Trivia Room", "bar7.png")).convert()
bar8 = pygame.image.load(os.path.join("Textures", "Trivia Room", "bar8.png")).convert()
bar9 = pygame.image.load(os.path.join("Textures", "Trivia Room", "bar9.png")).convert()
bar10 = pygame.image.load(os.path.join("Textures", "Trivia Room", "bar10.png")).convert()
bar11 = pygame.image.load(os.path.join("Textures", "Trivia Room", "bar11.png")).convert()
b_boss_room = pygame.image.load(os.path.join("Textures", "Boss Room", "boss_room.png")).convert()
rock = pygame.image.load(os.path.join("Textures", "Boss Room", "rock.png")).convert_alpha()
dwayne = pygame.image.load(os.path.join("Textures", "Boss Room", "dwayne.png")).convert_alpha()
bomb1 = pygame.image.load(os.path.join("Textures", "Boss Room", "bomb1.png")).convert_alpha()
bomb2 = pygame.image.load(os.path.join("Textures", "Boss Room", "bomb2.png")).convert_alpha()
bomb3 = pygame.image.load(os.path.join("Textures", "Boss Room", "bomb3.png")).convert_alpha()
bomb4 = pygame.image.load(os.path.join("Textures", "Boss Room", "bomb4.png")).convert_alpha()
bomb5 = pygame.image.load(os.path.join("Textures", "Boss Room", "bomb5.png")).convert_alpha()
bomb6 = pygame.image.load(os.path.join("Textures", "Boss Room", "bomb6.png")).convert_alpha()
bomb7 = pygame.image.load(os.path.join("Textures", "Boss Room", "bomb7.png")).convert_alpha()
bomb8 = pygame.image.load(os.path.join("Textures", "Boss Room", "bomb8.png")).convert_alpha()
bomb9 = pygame.image.load(os.path.join("Textures", "Boss Room", "bomb9.png")).convert_alpha()
bomb10 = pygame.image.load(os.path.join("Textures", "Boss Room", "bomb10.png")).convert_alpha()
bomb_empty = pygame.image.load(os.path.join("Textures", "Boss Room", "bomb_empty.png")).convert_alpha()
dragon1 = pygame.image.load(os.path.join("Textures", "Boss Room", "dragon1.png")).convert_alpha()
dragon_force = pygame.image.load(os.path.join("Textures", "Boss Room", "dragon_force.png")).convert_alpha()
dragon_hurt = pygame.image.load(os.path.join("Textures", "Boss Room", "dragon_hurt.png")).convert_alpha()

doorfront = pygame.image.load(os.path.join("Textures", "door_front.png")).convert_alpha() # Initialise doors
doorside = pygame.image.load(os.path.join("Textures", "door_side.png")).convert_alpha()
door1_rect = doorfront.get_rect() # Main -> puzzle
door1_rect.top = 368
door1_rect.left = 736
door2_rect = doorfront.get_rect() # Puzzle -> main
door2_rect.top = 736
door2_rect.left = 368
door3_rect = doorfront.get_rect() # Main -> computer
door3_rect.top = 736
door3_rect.left = 368
door4_rect = doorfront.get_rect() # Computer -> main
door4_rect.top = 400
door4_rect.left = 736
door5var = False
door5_rect = doorfront.get_rect() # Main -> memory
door5_rect.top = 200
door5_rect.left = 0
door6_rect = doorfront.get_rect() # Memory -> main
door6_rect.top = 736
door6_rect.left = 368
door7var = False
door7_rect = doorfront.get_rect() # Main -> hall
door7_rect.top = 0
door7_rect.left = 368
door8_rect = doorfront.get_rect() # Hall -> main
door8_rect.top = 736
door8_rect.left = 368
door9_rect = doorfront.get_rect() # Hall -> logic
door9_rect.top = 600
door9_rect.left = 120
door10_rect = doorfront.get_rect() # Logic -> hall
door10_rect.top = 736
door10_rect.left = 368
door11_rect = doorfront.get_rect() # Hall -> trivia
door11_rect.top = 200
door11_rect.left = 120
door12_rect = doorfront.get_rect() # Trivia -> hall
door12_rect.top = 736
door12_rect.left = 50

puzzle_img = {} # Puzzle variables
puzzle_rect = {}
finish = {}
drag = {}
offset_x = 0
offset_y = 0
row1top = [400,400,400,600,400,500]
row1left = [600,100,400,700,300,0]
row2top = [400,400,500,600,400,400]
row2left = [500,0,700,0,200,700]
rowleft1 = [125,225,325,425,525,625]
rowleft2 = [100,175,275,375,475,575]
boss_puzzle_img = {}
boss_puzzle_rect = {}
boss_row1top = [0,100,0,200,0,300]
boss_row1left = [300,0,400,700,100,0]
boss_row2top = [0,100,0,200,300,0]
boss_row2left = [200,700,500,0,700,600]
finish2 = []
timerfont = pygame.font.SysFont(None, 90)
timervalue = 90
dt = 0
dt2 = 0
boss_image_number = 1

button_list = ['r','g','g','r','r','r','g','r','g'] # Computer room variables
button_img = {}
button_rect = {}
button_left = [300,350,400,450,500,550,600,650,700]
button_finish = {}
screen_type = ['corner','side','corner','side','middle','side','corner','side','corner']
screen_img = {}
screen_rect = {}
screen_top = [50,50,50,125,110,125,190,200,190]
screen_left = [300,450,585,300,435,600,300,450,585]

tile_number = 1 # Memory room variables
step_number = 1
tile_lives = 5
memory_button_image = memory_button_g

gamer_text_list = [1, 2, 3] # Logic room variables

question_list = [] # Trivia room variables
answer_a = []
answer_b = []
answer_c = []
answer_d = []
correct_answer = []
question_number = 0
question_random = 1

a_rect = a_image.get_rect()
a_rect.top = 644
a_rect.left = 269
b_rect = b_image.get_rect()
b_rect.top = 644
b_rect.left = 338
c_rect = c_image.get_rect()
c_rect.top = 644
c_rect.left = 406
d_rect = d_image.get_rect()
d_rect.top = 644
d_rect.left = 475

myfont = pygame.font.SysFont(None, 40) # Fonts
tilelivesfont = pygame.font.SysFont(None, 40)
memoryskipfont = pygame.font.SysFont(None, 20)
logicfont = pygame.font.SysFont(None, 25)
triviafont = pygame.font.SysFont(None, 25)
healthfont = pygame.font.Font((os.path.join("Textures", "Eight-Bit Madness.ttf")), 25)

class Character(pygame.sprite.Sprite): # Character main class

    def __init__(self, width, height):
        super().__init__()
        self.image = character
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.direction = 0.0
        self.health = 100
        self.knockback = 0
        self.can_move = True
        self.dir_changed = False
        self.health_changed = False
        self.prev_health = 100

class Altar(pygame.sprite.Sprite): # Altar pieces class

    def __init__(self, width, height):
        super().__init__()
        self.image = circle
        self.rect = self.image.get_rect()
        self.inv = False

class Boss(pygame.sprite.Sprite): # Puzzle boss class

    def __init__(self, width, height):
        super().__init__()
        self.image = puzzle_boss_1
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()

class Blocker(pygame.sprite.Sprite): # Blocker class

    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()

    def draw(self, left, top, width, height):
        pygame.draw.rect(screen, black, [left, top, width, height], 1)
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = top

class MemoryTile(pygame.sprite.Sprite): # Memory room tiles class

    def __init__(self, width, height, left, top):
        super().__init__()
        self.image = tile_off
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = top

class CollisionTile(pygame.sprite.Sprite): # Memory room collision tiles class

    def __init__(self, width, height, left, top):
        super().__init__()
        self.image = collision_tile
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = top

class Gamer(pygame.sprite.Sprite): # Logic room gamer class

    def __init__(self, left, top):
        super().__init__()
        self.image = gamer
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = top


class Obstacle(pygame.sprite.Sprite): # Boss room obstacle classes

    def __init__(self, left, top, direction):
        super().__init__()
        self.image = rock
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.x = left
        self.y = top
        self.rect.x = self.x
        self.rect.y = self.y
        self.direction = direction

class Rock(Obstacle):

    def __init__(self, left, top, direction):
        super().__init__(left, top, direction)
        self.image = rock
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.x = left
        self.y = top
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 3
        self.damage = 10
        self.direction = direction
        self.type = 'rock'
        self.immune = False
        self.can_hurt = False

class Dwayne(Obstacle):

    def __init__(self, left, top, direction):
        super().__init__(left, top, direction)
        self.image = dwayne
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.x = left
        self.y = top
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 2
        self.damage = 100
        self.direction = direction
        self.type = 'dwayne'
        self.immune = False
        self.can_hurt = False

class Bomb(Obstacle):

    def __init__(self, left, top, direction, bomb_num):
        super().__init__(left, top, direction)
        self.image = bomb_empty
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.x = left
        self.y = top
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 5
        self.damage = 50
        self.direction = direction
        self.type = 'bomb'
        self.immune = False
        self.can_hurt = False
        self.bomb_num = bomb_num

obstacle_number = 0
obstacle_dict = {}
obstacle_list = pygame.sprite.Group()
obstacle_list.empty()
player_dir = 0.0
timer_dict = {}
bomb_anim_dict = {}
bomb_number = 0
temp_bomb_num = 0
bomb_dict = {}
bomb_list = pygame.sprite.Group()
bomb_list.empty()
        

class Dragon(pygame.sprite.Sprite): # Dragon class

    def __init__(self, left, top, direction):
        super().__init__()
        self.image = dragon1
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.x = left
        self.y = top
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 5
        self.direction = direction
        self.health = 1000
        self.force_active = False
        
memory_tile_list = pygame.sprite.Group() # Initialise memory tiles
memory_tile_list.empty()
memory_tile_step_list = pygame.sprite.Group()
memory_tile_step_list.empty()
tile1 = MemoryTile(75,75,369,556)
tile2 = MemoryTile(75,75,287,556)
tile3 = MemoryTile(75,75,287,475)
tile4 = MemoryTile(75,75,287,394)
tile5 = MemoryTile(75,75,369,394)
tile6 = MemoryTile(75,75,369,313)
tile7 = MemoryTile(75,75,450,313)
tile8 = MemoryTile(63,75,531,313)
tile9 = MemoryTile(63,75,531,231)
tile10 = MemoryTile(63,75,531,150)
tile11 = MemoryTile(75,75,450,150)
tile12 = MemoryTile(757,75,450,69)

tile8.image = tile_off_cut
tile8.image.set_colorkey(white)
tile9.image = tile_off_cut
tile9.image.set_colorkey(white)
tile10.image = tile_off_cut
tile10.image.set_colorkey(white)

memory_tile_list.add(tile1)
memory_tile_list.add(tile2)
memory_tile_list.add(tile3)
memory_tile_list.add(tile4)
memory_tile_list.add(tile5)
memory_tile_list.add(tile6)
memory_tile_list.add(tile7)
memory_tile_list.add(tile8)
memory_tile_list.add(tile9)
memory_tile_list.add(tile10)
memory_tile_list.add(tile11)
memory_tile_list.add(tile12)

collision_tile_list = pygame.sprite.Group() # Initialise collision tiles
collision_tile_list.empty()
collisiontile1 = CollisionTile(82,82,376,563)
collisiontile2 = CollisionTile(82,82,294,563)
collisiontile3 = CollisionTile(82,82,294,482)
collisiontile4 = CollisionTile(82,82,294,401)
collisiontile5 = CollisionTile(82,82,376,401)
collisiontile6 = CollisionTile(82,82,376,320)
collisiontile7 = CollisionTile(82,82,457,320)
collisiontile8 = CollisionTile(82,82,538,321)
collisiontile9 = CollisionTile(82,82,538,238)
collisiontile10 = CollisionTile(82,82,538,157)
collisiontile11 = CollisionTile(82,82,457,157)
collisiontile12 = CollisionTile(82,82,457,76)
collision_tile_list.add(collisiontile1)
collision_tile_list.add(collisiontile2)
collision_tile_list.add(collisiontile3)
collision_tile_list.add(collisiontile4)
collision_tile_list.add(collisiontile5)
collision_tile_list.add(collisiontile6)
collision_tile_list.add(collisiontile7)
collision_tile_list.add(collisiontile8)
collision_tile_list.add(collisiontile9)
collision_tile_list.add(collisiontile10)
collision_tile_list.add(collisiontile11)
collision_tile_list.add(collisiontile12)

blocker_list = pygame.sprite.Group() # Initialise blockers
blocker_list.empty()
blocker1 = Blocker(1,1)
blocker2 = Blocker(1,1)
blocker3 = Blocker(1,1)
blocker4 = Blocker(1,1)
blocker_list.add(blocker1)
blocker_list.add(blocker2)
blocker_list.add(blocker3)
blocker_list.add(blocker4)
blocker_list.update()

boss_list = pygame.sprite.Group() # Initialise puzzle boss
boss_list.empty()
puzzle_boss = Boss(313, 100)
boss_list.add(puzzle_boss)
puzzle_boss.rect.x = 243.5
puzzle_boss.rect.y = 100
boss_list.update()

dragon_list = pygame.sprite.Group() # Initialise dragon
dragon_list.empty()
dragon = Dragon(325, 100, math.radians(90))
dragon_list.add(dragon)
dragon_list.update()

sprite_list = pygame.sprite.Group() # Initialise character
sprite_list.empty()
player = Character(64,64)
sprite_list.add(player)
player.rect.x = 368
player.rect.y = 218
sprite_list.update()

altar_circle = Altar(100,100) # Create altar pieces
altar_cross = Altar(100,100)
altar_square = Altar(100,100)
altar_triangle = Altar(100,100)
altar_mid1 = Altar(100,100)
altar_mid2 = Altar(100,100)
altar_mid3 = Altar(100,100)
altar_mid4 = Altar(100,100)

altar_list = pygame.sprite.Group() # Altar pieces update group
altar_list.empty()
altar_list.add(altar_circle)
altar_list.add(altar_cross)
altar_list.add(altar_square)
altar_list.add(altar_triangle)
altar_list.add(altar_mid1)
altar_list.add(altar_mid2)
altar_list.add(altar_mid3)
altar_list.add(altar_mid4)
 
altar_circle.rect.x = 200 # Initialise altar pieces
altar_circle.rect.y = 300
altar_cross.rect.x = 500
altar_cross.rect.y = 400
altar_square.rect.x = 200
altar_square.rect.y = 400
altar_triangle.rect.x = 500
altar_triangle.rect.y = 300
altar_mid1.rect.x = 300
altar_mid1.rect.y = 300
altar_mid2.rect.x = 400
altar_mid2.rect.y = 300
altar_mid3.rect.x = 300
altar_mid3.rect.y = 400
altar_mid4.rect.x = 400
altar_mid4.rect.y = 400

altar_circle.image = circle # Set altar pieces texture
altar_cross.image = cross
altar_square.image = square
altar_triangle.image = triangle
altar_mid1.image = mid1
altar_mid2.image = mid2
altar_mid3.image = mid3
altar_mid4.image = mid4
altar_list.update()
 
inv_num = 0 # Altar variables

gamer1 = Gamer(50, 100)
gamer2 = Gamer(250, 100)
gamer3 = Gamer(450, 100)
gamer_list = pygame.sprite.Group() # Gamer update group
gamer_list.empty()
gamer_list.add(gamer1)
gamer_list.add(gamer2)
gamer_list.add(gamer3)
gamer_list.update()

welcome = myfont.render(("Welcome to Secrets of the Altar!"), True, (white)) # Text initialisation
instruction1a = myfont.render(("Go to different rooms through"), True, (white))
instruction1b = myfont.render(("the doorways."), True, (white))
instruction2a = myfont.render(("Solve puzzles to collect items and rewards."), True, (white))
instruction2b = myfont.render(("But beware! You only have 3 lives."), True, (white))
instruction3 = myfont.render(("The object in the centre of the room is the altar."), True, (white))
instruction4a = myfont.render(("When you obtain the altar keys, a"), True, (white))
instruction4b = myfont.render(("portal will open to the boss room!"), True, (white))
instruction5a = myfont.render(("Defeat the boss to escape"), True, (white))
instruction5b = myfont.render(("the dungeon and win the game!"), True, (white))
instruction7 = myfont.render(("Drag and drop the pieces into place."), True, (white))
instruction8 = myfont.render(("If a piece is right, it will snap in."), True, (white))
instruction9 = myfont.render(("Solve the puzzle before the miniboss timer runs out."), True, (white))
instruction10 = myfont.render(("Good luck!"), True, (white))
instruction12 = myfont.render(("Well done, you beat the miniboss!"), True, (white))
instruction13 = myfont.render(("Another doorway seems to have opened..."), True, (white))
instruction15 = myfont.render(("Some of the computers seem to have broken."), True, (white))
instruction16a = myfont.render(("Turn all the buttons green to fix them"), True, (white))
instruction16b = myfont.render(("and get a reward!"), True, (white))
instruction17a = myfont.render(("Click a button to toggle its' colour"), True, (white))
instruction17b = myfont.render(("and the colours of the buttons to either side of it."), True, (white))
instruction19 = myfont.render(("You have fixed the computers. Well done!"), True, (white))
instruction20 = myfont.render(("You have received the circular altar key."), True, (white))
instruction21 = myfont.render(("The circle on the altar has now been activated."), True, (white))
instruction22 = myfont.render(("Proceed to new rooms to collect more keys!"), True, (white))
instruction24 = myfont.render(("Get across the lava by walking on the tiles."), True, (white))
instruction25 = myfont.render(("But beware! Only some tiles work."), True, (white))
instruction26 = myfont.render(("The working tiles will flash yellow."), True, (white))
instruction27 = myfont.render(("There will be 1 flashing first, then 2, and so on."), True, (white))
instruction28a = myfont.render(("Memorise the route to get across the lava!"), True, (white))
instruction28b = myfont.render(("You have 5 lives."), True, (white))
instruction30 = myfont.render(("Well done, you have won the game!"), True, (white))
instruction31a = myfont.render(("You have received a square altar key"), True, (white))
instruction31b = myfont.render(("and another door has opened."), True, (white))
instruction33 = myfont.render(("You are now entering the logic gate."), True, (white))
instruction34 = myfont.render(("Only true thinkers are able to pass through."), True, (white))
instruction35 = myfont.render(("There will be three people with statements."), True, (white))
instruction36 = myfont.render(("Click the one who has the key."), True, (white))
instruction37 = myfont.render(("Choose wisely, or you will lose a life."), True, (white))
instruction39 = myfont.render(("Well done. You have chosen the right person."), True, (white))
instruction40 = myfont.render(("You have received the triangular altar key!"), True, (white))
instruction42 = myfont.render(("You are now entering the trivia room!"), True, (white))
instruction43 = myfont.render(("Fill up the bar by answering questions."), True, (white))
instruction44a = myfont.render(("But get none wrong, for if you do"), True, (white))
instruction44b = myfont.render(("then you will be taken back a space."), True, (white))
instruction45 = myfont.render(("Good luck!"), True, (white))
instruction47 = myfont.render(("Well done!"), True, (white))
instruction48 = myfont.render(("You have filled up the question bar."), True, (white))
instruction49 = myfont.render(("You have received the cross altar key!"), True, (white))
instruction51 = myfont.render(("Well done! You have activated the portal."), True, (white))
instruction52 = myfont.render(("You are now going into the boss room."), True, (white))
instruction53 = myfont.render(("There can be no turning back now."), True, (white))
instruction54 = myfont.render(("Collide with objects to move them."), True, (white))
instruction55 = myfont.render(("Damage the boss by hitting it with the objects."), True, (white))
instruction56 = myfont.render(("But be careful! They can also damage you."), True, (white))
instruction57 = myfont.render(("The bomb has area of effect damage."), True, (white))
instruction58 = myfont.render(("Watch out for the special rock which does more damage."), True, (white))
instruction59 = myfont.render(("Good luck! You have 100 health."), True, (white))
instructiondie = myfont.render(("Try again to advance to new rooms!"), True, (white))
instructionvar = 0
dev1 = myfont.render(("Developer mode activated"), True, (white))
memoryskip1 = memoryskipfont.render(("I have a"), True, (white))
memoryskip2 = memoryskipfont.render(("good memory,"), True, (white))
memoryskip3 = memoryskipfont.render(("skip to the"), True, (white))
memoryskip4 = memoryskipfont.render(("final step."), True, (white))
memoryskip1a = memoryskipfont.render(("This is too"), True, (white))
memoryskip2a = memoryskipfont.render(("hard, please"), True, (white))
memoryskip3a = memoryskipfont.render(("go back to the"), True, (white))
memoryskip4a = memoryskipfont.render(("first step."), True, (white))
logic1 = logicfont.render(("I do not have the key."), True, (white))
logic1a = logicfont.render(("At least 1 other person"), True, (white))
logic1aa = logicfont.render(("is telling the truth."), True, (white))
logic2 = logicfont.render(("I do not have the key."), True, (white))
logic2a = logicfont.render(("We are all telling the truth."), True, (white))
logic3 = logicfont.render(("One of the others is lying."), True, (white))
