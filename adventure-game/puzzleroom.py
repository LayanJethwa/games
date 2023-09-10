import pygame # Module imports
import time
import os
import config
import procedures
import sys
import threading
import pyganim


bossAnim = pyganim.PygAnimation([('Textures/Puzzle Room/puzzle_boss-1.png', 100),
                                 ('Textures/Puzzle Room/puzzle_boss-2.png', 100),
                                 ('Textures/Puzzle Room/puzzle_boss-3.png', 100),
                                 ('Textures/Puzzle Room/puzzle_boss-4.png', 100),
                                 ('Textures/Puzzle Room/puzzle_boss-5.png', 100),
                                 ('Textures/Puzzle Room/puzzle_boss-6.png', 100)])

bossAnim.play()
    
def pieces(): # Import puzzle images

    for i in range(6):
        config.puzzle_img[i] = pygame.image.load(os.path.join("Textures", "Puzzle Room", "row-1-column-{}.png".format(str(i + 1)))).convert()
        config.puzzle_rect[i] = config.puzzle_img[i].get_rect()
        config.puzzle_rect[i].top=config.row1top[i]
        config.puzzle_rect[i].left=config.row1left[i]
        config.finish[i] = False
        config.drag[i] = False

    for i in range(6):
        config.puzzle_img[i+6] = pygame.image.load(os.path.join("Textures", "Puzzle Room", "row-2-column-{}.png".format(str(i + 1)))).convert()
        config.puzzle_rect[i+6] = config.puzzle_img[i].get_rect()
        config.puzzle_rect[i+6].top=config.row2top[i]
        config.puzzle_rect[i+6].left=config.row2left[i]
        config.finish[i+6] = False
        config.drag[i+6] = False

def pieces_update(): # Update puzzle images
    for i in range(6):
        config.puzzle_rect[i].top=config.row1top[i]
        config.puzzle_rect[i].left=config.row1left[i]
        config.finish[i] = False
        config.drag[i] = False

    for i in range(6):
        config.puzzle_rect[i+6].top=config.row2top[i]
        config.puzzle_rect[i+6].left=config.row2left[i]
        config.finish[i+6] = False
        config.drag[i+6] = False

    for i in range(6):
        config.boss_puzzle_rect[i].top=config.boss_row1top[i]
        config.boss_puzzle_rect[i].left=config.boss_row1left[i]

    for i in range(6):
        config.boss_puzzle_rect[i+6].top=config.boss_row2top[i]
        config.boss_puzzle_rect[i+6].left=config.boss_row2left[i]
        
    config.timervalue = 90

def boss_pieces(): # Import boss puzzle images
    for i in range(6):
        config.boss_puzzle_img[i] = pygame.image.load(os.path.join("Textures", "Puzzle Room", "row-1-column-{}.png".format(str(i + 1)))).convert()
        config.boss_puzzle_rect[i] = config.boss_puzzle_img[i].get_rect()
        config.boss_puzzle_rect[i].top=config.boss_row1top[i]
        config.boss_puzzle_rect[i].left=config.boss_row1left[i]

    for i in range(6):
        config.boss_puzzle_img[i+6] = pygame.image.load(os.path.join("Textures", "Puzzle Room", "row-2-column-{}.png".format(str(i + 1)))).convert()
        config.boss_puzzle_rect[i+6] = config.boss_puzzle_img[i].get_rect()
        config.boss_puzzle_rect[i+6].top=config.boss_row2top[i]
        config.boss_puzzle_rect[i+6].left=config.boss_row2left[i]

def boss_iteration(timervalue, index, top, left): # Boss puzzle pieces placement iteration
    if config.timervalue >= timervalue-1 and config.timervalue <= timervalue+1:
        config.boss_puzzle_rect[index].top=top
        config.boss_puzzle_rect[index].left=left

def boss_pieces_placement(): # Boss puzzle pieces animation
    boss_iteration(85,0,200,100)
    boss_iteration(78,5,200,600)
    boss_iteration(71,8,300,300)
    boss_iteration(64,2,200,300)
    boss_iteration(57,10,300,500)
    boss_iteration(50,3,200,400)
    boss_iteration(43,11,300,600)
    boss_iteration(36,1,200,200)
    boss_iteration(29,4,200,500)
    boss_iteration(22,9,300,400)
    boss_iteration(15,6,300,100)
    boss_iteration(8,7,300,200)

def timer(): # Countdown timer
    config.timervalue = 90-config.dt
    if config.timervalue <= 0:
        config.timervalue = 0.00
    timertext = config.timerfont.render(str(round(config.timervalue, 1)), True, (config.white))
    timertext = pygame.transform.scale(timertext, (80,80))
    config.dt = (pygame.time.get_ticks() - config.dt2)/1000
    config.screen.blit(timertext, (10, 10))

def puzzle_room_update(): # Puzzle room update
    divider = pygame.Rect(0,380,800,20)
    config.screen.fill(config.black)
    config.screen.blit(config.b_puzzle_room,(0, 0))

    for i in range(12): # Render puzzle pieces
        config.screen.blit(config.puzzle_img[i], config.puzzle_rect[i])

    for i in range(12): # Render boss puzzle pieces
        config.screen.blit(config.boss_puzzle_img[i], config.boss_puzzle_rect[i])
        
    for i in range(6): # Snap puzzle pieces in place
        if config.puzzle_rect[i].top<=525 and config.puzzle_rect[i].top>=500 and config.puzzle_rect[i].left>=config.rowleft2[i] and config.puzzle_rect[i].left<=config.rowleft1[i]:
                config.puzzle_rect[i].top=500
                config.puzzle_rect[i].left=((config.rowleft1[i])-25)
                config.finish[i] = True
    for i in range(6):
        if config.puzzle_rect[i+6].top<=625 and config.puzzle_rect[i+6].top>=600 and config.puzzle_rect[i+6].left>=config.rowleft2[i] and config.puzzle_rect[i+6].left<=config.rowleft1[i]:
            config.puzzle_rect[i+6].top=600
            config.puzzle_rect[i+6].left=((config.rowleft1[i])-25)
            config.finish[i+6] = True

    if config.player.rect.y <= 400: # Player move limitations
        config.player.rect.y = 401

    for i in range(12): # Puzzle finish code
        if config.finish[i] == True:
            if i not in config.finish2:
                config.finish2.append(i)
    if len(config.finish2) == 12 and config.timervalue > 0:
        time.sleep(0.5)
        config.puzzle_room_loop = False
        config.instruction_loop = True
        config.instructionvar = 12
    elif config.timervalue <= 0:
        time.sleep(0.5)
        config.puzzle_room_loop = False
        config.instruction_loop = True
        config.instructionvar = 100
        config.lives -= 1

    timer() # Countdown timer code

    boss_pieces_placement() # Boss piece updates

    config.sprite_list.draw(config.screen) # Render objects
    config.sprite_list.update()
    bossAnim.blit(config.screen, (243.5,100))
    config.screen.blit(config.doorfront, config.door2_rect)
    pygame.draw.rect(config.screen, config.white, divider)
    pygame.display.update()

def drag_function(): # Puzzle pieces drag code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.running = False
            pygame.quit()
            sys.exit()
            exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(12):
                    if config.puzzle_rect[i].collidepoint(event.pos):
                        config.drag[i] = True
                        mouse_x, mouse_y = event.pos
                        config.offset_x = config.puzzle_rect[i].left - mouse_x
                        config.offset_y = config.puzzle_rect[i].top - mouse_y
   

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                for i in range(12):
                    config.drag[i] = False
                config.offset_x = 0
                config.offset_y = 0

        if event.type == pygame.MOUSEMOTION:
            for i in range(12):
                mouse_x, mouse_y = event.pos
                if config.drag[i] and config.puzzle_rect[i].top >= 400 and config.puzzle_rect[i].top <= 700 and config.puzzle_rect[i].left >= 0 and config.puzzle_rect[i].left <= 700 and config.finish[i] == False:
                    config.puzzle_rect[i].left = mouse_x + config.offset_x
                    config.puzzle_rect[i].top = mouse_y + config.offset_y
                    if config.puzzle_rect[i].top <= 400:
                        config.puzzle_rect[i].top = 401
                    if config.puzzle_rect[i].top >= 700:
                        config.puzzle_rect[i].top = 699
                    if config.puzzle_rect[i].left <= 0:
                        config.puzzle_rect[i].left = 1
                    if config.puzzle_rect[i].left >= 700:
                        config.puzzle_rect[i].left = 699

def puzzle_room(): # Puzzle room code
    procedures.player_move()
    puzzle_room_update()
    drag_function()
