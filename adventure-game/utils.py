import pygame
import config
import os
import os.path

def install_pkgs():
    print('')
    # go into python.exe
    # import pip
    # pip.main(["install", "lib"])

pygame.init()

sumlines = 0

def debug(func): # from utils import debug, @debug above func
    def wrapper(*args,**kwargs):
        print(f'====== Calling {func.__name__} with {args} {kwargs}')
        res = func(*args, **kwargs)
        print(f'====== Got {res} from {func.__name__}')
        return res
    return wrapper

def tile_debug(): # Memory room debug
    key = pygame.key.get_pressed()
    if key[pygame.K_q]:
        print('Step number =', config.step_number)
        print('Tile number =', config.tile_number)

def line_count(): # Lines
    global sumlines
    lines1 = sum(1 for line in open('computerroom.py'))
    lines2 = sum(1 for line in open('config.py'))
    lines3 = sum(1 for line in open('game.py'))
    lines4 = sum(1 for line in open('mainroom.py'))
    lines5 = sum(1 for line in open('memoryroom.py'))
    lines6 = sum(1 for line in open('procedures.py'))
    lines7 = sum(1 for line in open('puzzleroom.py'))
    lines8 = sum(1 for line in open('utils.py'))
    lines9 = sum(1 for line in open('hallroom.py'))
    lines10 = sum(1 for line in open('logicroom.py'))
    lines11 = sum(1 for line in open('triviaroom.py'))
    lines12 = sum(1 for line in open('bossroom.py'))
    sumlines = lines1+lines2+lines3+lines4+lines5+lines6+lines7+lines8+lines9+lines10+lines11+lines12

def bigger(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return a

def smaller(a,b):
    if a>b:
        return b
    elif b>a:
        return a
    else:
        return b

'''
def room():
'''
# Template for making a room

# create config.doorx in and out of room
# create config.x_room_loop 
# create config.doorxvar if needed
# create config.b_x_room

# create file xroom.py 

'''
def x_room_update():
'''
# in xroom.py 
'''
config.screen.fill(config.black)
config.screen.blit(config.b_x_room,(0, 0)) 
config.sprite_list.draw(config.screen)
config.sprite_list.update()
config.screen.blit(config.doorfront, config.doorx_rect) 
pygame.display.update()

def x_room(): 
procedures.player_move()
procedures.quit()
x_room_update() 


while config.x_room_loop:
'''
# in game.py IMPORT
'''
xroom.x_room()
'''
# add instructions
'''


def update():
'''
# in procedures.py IMPORT
'''
if config.x_room_loop == True: 
xroom.x_room_update() 
if config.player.rect.colliderect(config.doorx_rect) and config.main_room_loop == True and config.doorxvar == True: 
config.main_room_loop = False
config.instruction_loop/config.x_room_loop = True
'''
# repeat for door out of room
# add move limitations
'''
if config.doorxvar == True:
'''
# in mainroom.py
'''
config.screen.blit(config.doorfront, config.doorx_rect)
'''
# add file to line counter

def find():
    string = str(input('What string do you want to find?'))
    for fname in os.listdir('.'):
        if os.path.isfile(fname):
            f = open(fname)
            if string in f.read():
                print (fname)
            f.close()
