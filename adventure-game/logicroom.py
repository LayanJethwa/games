import pygame
import config
import procedures
import random

gamer1textnum = 0
gamer2textnum = 0
gamer3textnum = 0
gamertextnumlist = []

def logic_text_init(): # Initialise text on gamers
    global gamer1textnum
    global gamer2textnum
    global gamer3textnum
    global gamertextnumlist
    rand1 = random.randint(0,2)
    rand2 = random.randint(0,1)
    gamer1textnum = config.gamer_text_list[rand1]
    config.gamer_text_list.pop(rand1)
    gamer2textnum = config.gamer_text_list[rand2]
    config.gamer_text_list.pop(rand2)
    gamer3textnum = config.gamer_text_list[0]
    config.gamer_text_list.pop(0)
    gamertextnumlist = [gamer1textnum, gamer2textnum, gamer3textnum]

def gamer_text_blit(): # Blit text on gamers
    global gamer1textnum
    global gamer2textnum
    global gamer3textnum
    for i in range(1,4):
        if gamer1textnum == i:
            if i == 1:
                config.screen.blit(config.logic1, config.logic1.get_rect(center=(200,450)))
                config.screen.blit(config.logic1a,config.logic1a.get_rect(center=(200,480)))
                config.screen.blit(config.logic1aa,config.logic1aa.get_rect(center=(200,500)))
            elif i == 2:
                config.screen.blit(config.logic2, config.logic2.get_rect(center=(200,450)))
                config.screen.blit(config.logic2a,config.logic2a.get_rect(center=(200,500)))
            elif i == 3:
                config.screen.blit(config.logic3, config.logic3.get_rect(center=(200,450)))
        if gamer2textnum == i:
            if i == 1:
                config.screen.blit(config.logic1, config.logic1.get_rect(center=(400,450)))
                config.screen.blit(config.logic1a,config.logic1a.get_rect(center=(400,480)))
                config.screen.blit(config.logic1aa,config.logic1aa.get_rect(center=(400,500)))
            elif i == 2:
                config.screen.blit(config.logic2, config.logic2.get_rect(center=(400,450)))
                config.screen.blit(config.logic2a,config.logic2a.get_rect(center=(400,500)))
            elif i == 3:
                config.screen.blit(config.logic3, config.logic3.get_rect(center=(400,450)))
        if gamer3textnum == i:
            if i == 1:
                config.screen.blit(config.logic1, config.logic1.get_rect(center=(600,450)))
                config.screen.blit(config.logic1a,config.logic1a.get_rect(center=(600,480)))
                config.screen.blit(config.logic1aa,config.logic1aa.get_rect(center=(600,500)))
            elif i == 2:
                config.screen.blit(config.logic2, config.logic2.get_rect(center=(600,450)))
                config.screen.blit(config.logic2a,config.logic2a.get_rect(center=(600,500)))
            elif i == 3:
                config.screen.blit(config.logic3, config.logic3.get_rect(center=(600,450)))

def win(): # Win condition
    config.logic_room_loop = False
    config.instruction_loop = True
    config.instructionvar = 39
    config.altar_triangle.inv = True
    procedures.altar_count()

def lose(): # Lose condition
    config.logic_room_loop = False
    config.instruction_loop = True
    config.lives -=1
    config.instructionvar = 100
    config.gamer_text_list = [1,2,3]
    logic_text_init()

def gamer_text_click(): # Detect if player clicked right gamer
    global gamertextnumlist
    for event in pygame.event.get(): # Move to next screen
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if config.gamer1.rect.collidepoint(event.pos):
                    if gamertextnumlist[0] == 2:
                        win()
                    else:
                        lose()
                elif config.gamer2.rect.collidepoint(event.pos):
                    if gamertextnumlist[1] == 2:
                        win()
                    else:
                        lose()
                elif config.gamer3.rect.collidepoint(event.pos):
                    if gamertextnumlist[2] == 2:
                        win()
                    else:
                        lose()

        if event.type == pygame.QUIT:
            config.running = False
            pygame.quit()
            sys.exit()
            exit()

def logic_room_update(): # Update room
    config.screen.fill(config.black)
    config.screen.blit(config.b_logic_room,(0, 0))
    config.sprite_list.draw(config.screen)
    config.sprite_list.update()
    config.gamer_list.draw(config.screen)
    config.gamer_list.update()
    config.screen.blit(config.doorfront, config.door10_rect)
    gamer_text_blit()
    gamer_text_click()
    pygame.display.update()

def logic_room():
    procedures.player_move()
    procedures.quit()
    logic_room_update()

