import pygame
import sys
import threading
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 250))
pygame.display.set_caption('Dino Game')
running = False
black = (0,0,0)
white = (255,255,255)
down_var = True
up_var = True
obstacle_num = 1
obstacles = {}
run = True
speed = 1
score = 0
hiscore = 0

dino = pygame.image.load('dino.png').convert_alpha()
dino_left = pygame.image.load('dino_left.png').convert_alpha()
dino_right = pygame.image.load('dino_right.png').convert_alpha()
cacti3 = pygame.image.load('cacti3.png').convert_alpha()
cacti2 = pygame.image.load('cacti2.png').convert_alpha()
cactus_big = pygame.image.load('cactus_big.png').convert_alpha()
cactus_small = pygame.image.load('cactus_small.png').convert_alpha()
background = pygame.image.load('background.png').convert_alpha()
dino_dead = pygame.image.load('dino_dead.png').convert_alpha()
game_over = pygame.image.load('game_over.png').convert_alpha()

scroll = 0
tiles = math.ceil(800/background.get_width()) + 1

class Dino(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()
        self.image = dino
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.x = 50
        self.y = 125

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()
        self.image = cacti3
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.x = 700
        self.y = 200
        self.rect.x = 700
        self.rect.y = 135

sprite_list = pygame.sprite.Group()
sprite_list.empty()
dino_sprite = Dino(64,64)
sprite_list.add(dino_sprite)
dino_sprite.rect.x = 50
dino_sprite.rect.y = 125
dino_mask = pygame.mask.from_surface(dino)
dino_sprite.mask = dino_mask
sprite_list.update()

obstacle_list = pygame.sprite.Group()
obstacle_list.empty()

def legs():
    global run
    if dino_sprite.image == dino_right:
        dino_sprite.image = dino_left
    else:
        dino_sprite.image = dino_right
    if run == True:
        threading.Timer(0.1,legs).start()

def down():
    global speed
    global down_var
    global up_var
    if dino_sprite.rect.y < 21:
        dino_sprite.rect.y += 1.5*speed
        threading.Timer(0.007,down).start()
    elif dino_sprite.rect.y > 20 and dino_sprite.rect.y < 125:
        dino_sprite.rect.y += 3*speed
        threading.Timer(0.007,down).start()
    else:
        down_var = True
        up_var = True

def up():
    global down_var
    global up_var
    global speed
    if dino_sprite.rect.y > 20:
        dino_sprite.rect.y -= 3*speed
        threading.Timer(0.007,up).start()
    elif dino_sprite.rect.y < 21 and dino_sprite.rect.y > -1:
        dino_sprite.rect.y -= 1.5*speed
        threading.Timer(0.007,up).start()
    else:
        threading.Timer(0.007,down).start()

def move():
    global run
    global up_var
    global down_var
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and up_var == True and down_var == True and run == True:
        up_var = False
        threading.Timer(0.007,up).start()
        down_var = False

def obstacle_move():
    global run
    global speed
    global score
    for i in obstacle_list:
        if i.rect.x > 0:
            i.rect.x -= 2*speed
        elif i.rect.x < 1:
            obstacle_list.remove(i)
    obstacle_list.update()
    if run == True:
        threading.Timer(0.005,obstacle_move).start()

def spawn():
    global run
    global obstacle_num
    obstacle_type = random.randint(1,10)
    if obstacle_type < 5:
        obstacles['obstacle'+str(obstacle_num)] = Obstacle(34,70)
        obstacles['obstacle'+str(obstacle_num)].image = cactus_big
        obstacles['obstacle'+str(obstacle_num)].rect.y = 115
    elif obstacle_type > 4 and obstacle_type < 8:
        obstacles['obstacle'+str(obstacle_num)] = Obstacle(17,35)
        obstacles['obstacle'+str(obstacle_num)].image = cactus_small
    elif obstacle_type > 7 and obstacle_type < 10:
        obstacles['obstacle'+str(obstacle_num)] = Obstacle(51,35)
        obstacles['obstacle'+str(obstacle_num)].image = cacti3
    elif obstacle_type == 10:
        obstacles['obstacle'+str(obstacle_num)] = Obstacle(34,35)
        obstacles['obstacle'+str(obstacle_num)].image = cacti2
        
    obstacle_list.add(obstacles['obstacle'+str(obstacle_num)])
    obstacle_num+=1
    obstacle_list.update()
    if run == True:
        threading.Timer((random.randint(3,5)),spawn).start()
    
def die():
    global run
    run = False
    dino_sprite.image = dino_dead

def collision():
    for i in obstacle_list:
        if pygame.sprite.collide_mask(dino_sprite, i):
            die()

def speed_add():
    global score
    global speed
    speed = 1+(score/1000)

def clock():
    global score
    global run
    if run == True:
        threading.Timer(0.2,clock).start()
    score +=1

def blit_score():
    global score
    global hiscore
    font = pygame.font.SysFont(None, 25)
    if score < 10:
        text = font.render(("Score: 0000"+str(score)), True, (black))
    elif score < 100:
        text = font.render(("Score: 000"+str(score)), True, (black))
    elif score < 1000:
        text = font.render(("Score: 00"+str(score)), True, (black))
    elif score < 10000:
        text = font.render(("Score: 0"+str(score)), True, (black))
    screen.blit(text, (650,25))
    if hiscore != 0:
        hitext = font.render(("High Score: "+str(hiscore)), True, (black))
        screen.blit(hitext, (400,25))

if running == False:
    spawn()
    threading.Timer(0.015,obstacle_move).start()
    threading.Timer(0.1,clock).start()
    threading.Timer(0.05,legs).start()
    running = True
        
while running:
    screen.fill(white)
    pygame.time.Clock().tick(30)
    i = 0
    while(i < tiles):
        screen.blit(background, (background.get_width()*i
                         + scroll, 0))
        i += 1
    scroll -= 6*speed
    if abs(scroll) > background.get_width():
        scroll = 0
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            exit()
            quit()
        key = pygame.key.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN or key[pygame.K_SPACE] and run == False:
            obstacle_list.empty()
            dino_sprite.image = dino
            run = True
            spawn()
            threading.Timer(0.015,obstacle_move).start()
            threading.Timer(0.2,clock).start()
            threading.Timer(0.05,legs).start()
            if score > hiscore:
                hiscore = score
            score = 0
            speed = 1
    move()
    collision()
    speed_add()
    blit_score()
    if run == False:
        screen.blit(game_over, (240,50))
        obstacle_list.empty()
    sprite_list.draw(screen)
    sprite_list.update()
    obstacle_list.draw(screen)
    obstacle_list.update()
    pygame.display.update()
