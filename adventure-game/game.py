import pygame # Module imports
import sys
import os
import time
import threading

import config # Created module imports
import mainroom
import puzzleroom
import procedures
import computerroom
import memoryroom
import hallroom
import logicroom
import triviaroom
import bossroom

def instruction_add():
    if config.dievar == 1:
        config.instructionvar = 13.1
        config.dievar = 0
    elif config.dievar == 2:
        config.instructionvar = 31.1
        config.dievar = 0
    else:
        config.instructionvar += 1

def instructions(): # Instruction text
    
    arrow1 = config.arrow.get_rect() # Initialise instruction variables
    arrow1.top = 600
    arrow1.left = 336
    
    for event in pygame.event.get(): # Move to next screen
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if arrow1.collidepoint(event.pos):
                    config.instructionvar += 1
        if event.type == pygame.QUIT:
            config.running = False
            pygame.quit()
            sys.exit()
            exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        config.instructionvar += 1
        time.sleep(0.1)

    if config.instructionvar == 100: # Lose lives
        if config.lives > 0:
            arrow1 = config.arrow.get_rect()
            arrow1.top = 600
            arrow1.left = 336
            die = config.myfont.render(("You died!"), True, (config.white))
            if config.lives == 1:
                life_text = config.myfont.render(("You have "+str(config.lives)+" life left."), True, (config.white))
            elif config.lives > 1:
                life_text = config.myfont.render(("You have "+str(config.lives)+" lives left."), True, (config.white))

            config.screen.fill(config.black) # Show life lost
            config.screen.blit(config.arrow, arrow1)
            config.screen.blit(die, die.get_rect(center=(400, 300)))
            config.screen.blit(life_text, life_text.get_rect(center=(400, 340)))
            config.player.health = 100
            pygame.display.update()

        elif config.lives <= 0:
            die = config.myfont.render(("You died!"), True, (config.white))
            life_text = config.myfont.render(("You have "+str(config.lives)+" lives left."), True, (config.white))
            closing = config.myfont.render(("The program will close in 5 seconds"), True, (config.white))

            config.screen.fill(config.black) # Show life lost
            config.screen.blit(die, die.get_rect(center=(400, 300)))
            config.screen.blit(life_text, life_text.get_rect(center=(400, 340)))
            config.screen.blit(closing, closing.get_rect(center=(400, 380)))
            pygame.display.update()
            time.sleep(5)
            config.running = False
            pygame.quit()
            sys.exit()
            exit()

    if config.instructionvar == 101:
        config.screen.blit(config.instructiondie, config.instructiondie.get_rect(center=(400, 300)))

    if config.instructionvar == 102:
        config.instruction_loop = False
        config.main_room_loop = True
        
        config.player.rect.x = 318
        config.player.rect.y = 218
                        
    if config.instructionvar == 0:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.welcome, config.welcome.get_rect(center=(400, 300)))
        pygame.display.update()
        if key[pygame.K_d]:
            config.developer_mode_loop = True
            config.instruction_loop = False

    elif config.instructionvar == 1:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)        
        config.screen.blit(config.instruction1a, config.instruction1a.get_rect(center=(400, 300)))
        config.screen.blit(config.instruction1b, config.instruction1b.get_rect(center=(400, 340)))
        pygame.display.update()

    elif config.instructionvar == 2:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction2a, config.instruction2a.get_rect(center=(400, 300)))
        config.screen.blit(config.instruction2b, config.instruction2b.get_rect(center=(400, 340)))
        pygame.display.update()

    elif config.instructionvar == 3:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction3, config.instruction3.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 4:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction4a, config.instruction4a.get_rect(center=(400, 300)))
        config.screen.blit(config.instruction4b, config.instruction4b.get_rect(center=(400, 340)))
        pygame.display.update()

    elif config.instructionvar == 5:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction5a, config.instruction5a.get_rect(center=(400, 300)))
        config.screen.blit(config.instruction5b, config.instruction5b.get_rect(center=(400, 340)))
        pygame.display.update()

    elif config.instructionvar == 6:
        config.instruction_loop = False
        config.main_room_loop = True
        

    elif config.instructionvar == 7:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction7, config.instruction7.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 8:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction8, config.instruction8.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 9:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction9, config.instruction9.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 10:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction10, config.instruction10.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 11:
        config.instruction_loop = False
        config.puzzle_room_loop = True
        config.dt2 = pygame.time.get_ticks()
        puzzleroom.pieces_update()
        config.player.rect.x = 368
        config.player.rect.y = 650

    elif config.instructionvar == 12:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction12, config.instruction12.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 13:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction13, config.instruction13.get_rect(center=(400, 300)))
        config.door5var = True
        pygame.display.update()

    elif config.instructionvar == 14:
        config.instruction_loop = False
        config.main_room_loop = True
        config.player.rect.x = 650
        config.player.rect.y = 368

    elif config.instructionvar == 15:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction15, config.instruction15.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 16:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction16a, config.instruction16a.get_rect(center=(400, 300)))
        config.screen.blit(config.instruction16b, config.instruction16b.get_rect(center=(400, 340)))
        pygame.display.update()

    elif config.instructionvar == 17:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction17a, config.instruction17a.get_rect(center=(400, 300)))
        config.screen.blit(config.instruction17b, config.instruction17b.get_rect(center=(400, 340)))
        pygame.display.update()

    elif config.instructionvar == 18:
        config.instruction_loop = False
        config.computer_room_loop = True
        config.player.rect.x = 650
        config.player.rect.y = 400

    elif config.instructionvar == 19:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction19, config.instruction19.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 20:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction20, config.instruction20.get_rect(center=(400, 300)))
        altar_key_text = config.myfont.render(("You have collected "+str(config.inv_num)+" out of 4 keys."), True, (config.white))        
        config.screen.blit(altar_key_text, altar_key_text.get_rect(center=(400, 340)))
        if config.inv_num == 4:
            boss_portal_text = config.myfont.render(("You can now enter the boss portal in the main room!"), True, (config.white))
            config.screen.blit(boss_portal_text, boss_portal_text.get_rect(center=(400, 380)))
        pygame.display.update()

    elif config.instructionvar == 21:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction21, config.instruction21.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 22:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction22, config.instruction22.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 23:
        config.instruction_loop = False
        config.main_room_loop = True
        config.player.rect.x = 368
        config.player.rect.y = 650

    elif config.instructionvar == 24:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction24, config.instruction24.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 25:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction25, config.instruction25.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 26:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction26, config.instruction26.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 27:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction27, config.instruction27.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 28:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction28a, config.instruction28a.get_rect(center=(400, 300)))
        config.screen.blit(config.instruction28b, config.instruction28b.get_rect(center=(400, 340)))
        pygame.display.update()

    elif config.instructionvar == 29:
        config.instruction_loop = False
        config.memory_room_loop = True
        config.tile_number = 1
        for i in config.memory_tile_list:
            i.image = config.tile_off
        config.player.rect.x = 368
        config.player.rect.y = 650
        if config.tile_lives <= 0:
            config.tile_lives = 5
            config.step_number = 1
            config.tile_number = 1

    elif config.instructionvar == 30:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction30, config.instruction30.get_rect(center=(400, 300)))
        pygame.display.update()   

    elif config.instructionvar == 31:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction31a, config.instruction31a.get_rect(center=(400, 300)))
        config.screen.blit(config.instruction31b, config.instruction31b.get_rect(center=(400, 340)))
        altar_key_text = config.myfont.render(("You have collected "+str(config.inv_num)+" out of 4 keys."), True, (config.white))
        config.screen.blit(altar_key_text, altar_key_text.get_rect(center=(400, 380)))
        if config.inv_num == 4:
            boss_portal_text = config.myfont.render(("You can now enter the boss portal in the main room!"), True, (config.white))
            config.screen.blit(boss_portal_text, boss_portal_text.get_rect(center=(400, 420)))
        pygame.display.update()

    elif config.instructionvar == 32:
        config.instruction_loop = False
        config.main_room_loop = True
        config.player.rect.x = 100
        config.player.rect.y = 200

    elif config.instructionvar == 33:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction33, config.instruction33.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 34:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction34, config.instruction34.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 35:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction35, config.instruction35.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 36:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction36, config.instruction36.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 37:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction37, config.instruction37.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 38:
        config.instruction_loop = False
        config.logic_room_loop = True
        config.player.rect.x = 368
        config.player.rect.y = 650

    elif config.instructionvar == 39:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction39, config.instruction39.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 40:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction40, config.instruction40.get_rect(center=(400, 300)))
        altar_key_text = config.myfont.render(("You have collected "+str(config.inv_num)+" out of 4 keys."), True, (config.white))
        config.screen.blit(altar_key_text, altar_key_text.get_rect(center=(400, 340)))
        if config.inv_num == 4:
            boss_portal_text = config.myfont.render(("You can now enter the boss portal in the main room!"), True, (config.white))
            config.screen.blit(boss_portal_text, boss_portal_text.get_rect(center=(400, 380)))
        pygame.display.update()

    elif config.instructionvar == 41:
        config.instruction_loop = False
        config.hall_room_loop = True
        config.player.rect.x = 220
        config.player.rect.y = 600
        
    elif config.instructionvar == 42:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction42, config.instruction42.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 43:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction43, config.instruction43.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 44:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction44a, config.instruction44a.get_rect(center=(400, 300)))
        config.screen.blit(config.instruction44b, config.instruction44b.get_rect(center=(400, 340)))
        pygame.display.update()

    elif config.instructionvar == 45:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction45, config.instruction45.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 46:
        config.instruction_loop = False
        config.trivia_room_loop = True 
        config.player.rect.x = 50
        config.player.rect.y = 650

    elif config.instructionvar == 47:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction47, config.instruction47.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 48:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction48, config.instruction48.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 49:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction49, config.instruction49.get_rect(center=(400, 300)))
        altar_key_text = config.myfont.render(("You have collected "+str(config.inv_num)+" out of 4 keys."), True, (config.white))
        config.screen.blit(altar_key_text, altar_key_text.get_rect(center=(400, 340)))
        if config.inv_num == 4:
            boss_portal_text = config.myfont.render(("You can now enter the boss portal in the main room!"), True, (config.white))
            config.screen.blit(boss_portal_text, boss_portal_text.get_rect(center=(400, 380)))
        pygame.display.update()

    elif config.instructionvar == 50:
        config.instruction_loop = False
        config.hall_room_loop = True
        config.player.rect.x = 220
        config.player.rect.y = 200

    elif config.instructionvar == 51:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction51, config.instruction51.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 52:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction52, config.instruction52.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 53:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction53, config.instruction53.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 54:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction54, config.instruction54.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 55:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction55, config.instruction55.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 56:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction56, config.instruction56.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 57:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction57, config.instruction57.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 58:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction58, config.instruction58.get_rect(center=(400, 300)))
        pygame.display.update()

    elif config.instructionvar == 59:
        config.screen.fill(config.black)
        config.screen.blit(config.arrow, arrow1)
        config.screen.blit(config.instruction59, config.instruction59.get_rect(center=(400, 300)))
        if config.lives == 1:
            life_text = config.myfont.render(("You have "+str(config.lives)+" life left."), True, (config.white))
        elif config.lives > 1 or config.lives < 1:
            life_text = config.myfont.render(("You have "+str(config.lives)+" lives left."), True, (config.white))

        config.screen.blit(life_text, life_text.get_rect(center=(400, 340)))
        pygame.display.update()

    elif config.instructionvar == 60:
        config.instruction_loop = False
        config.boss_room_loop = True
        config.player.rect.x = 368
        config.player.rect.y = 650
        bossroom.dragon_move()
        bossroom.obstacle_spawn()
        bossroom.obstacle_move()
        bossroom.initial_obstacle_spawn()
        
puzzleroom.pieces()
puzzleroom.boss_pieces()
computerroom.buttons()
computerroom.screens()
logicroom.logic_text_init()
triviaroom.question_reset()

while config.running: # Game loops
    while config.instruction_loop:
        instructions()

    while config.main_room_loop:
        mainroom.main_room()

    while config.puzzle_room_loop:
        puzzleroom.puzzle_room()

    while config.computer_room_loop:
        computerroom.computer_room()

    while config.memory_room_loop:
        memoryroom.memory_room()

    while config.hall_room_loop:
        hallroom.hall_room()

    while config.logic_room_loop:
        logicroom.logic_room()

    while config.trivia_room_loop:
        triviaroom.trivia_room()

    while config.boss_room_loop:
        bossroom.boss_room()


    while config.developer_mode_loop:
        procedures.developer_mode()
