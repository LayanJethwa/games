import pygame # Module imports
import time
import sys
import threading
import config
import mainroom
import puzzleroom
import computerroom
import memoryroom
import hallroom
import logicroom
import triviaroom
import bossroom
import utils
import math

def update(): # Update all rooms
    if config.main_room_loop == True:
        mainroom.main_room_update()
    if config.puzzle_room_loop == True:
        puzzleroom.puzzle_room_update()
    if config.computer_room_loop == True:
        computerroom.computer_room_update()
    if config.memory_room_loop == True:
        memoryroom.memory_room_update()
    if config.hall_room_loop == True:
        hallroom.hall_room_update()
    if config.logic_room_loop == True:
        logicroom.logic_room_update()
    if config.trivia_room_loop == True:
        triviaroom.trivia_room_update()
    if config.boss_room_loop == True:
        bossroom.boss_room_update()

def playerleft(): # Player animations
    config.player.image = config.characterleft
    tnormal = threading.Timer(0.1, playernormal)
    tnormal.start()
def playerright():
    config.player.image = config.characterright
    tnormal = threading.Timer(0.1, playernormal)
    tnormal.start()
def playernormal():
    config.player.image = config.character
        
def player_move():

    if config.player.rect.colliderect(config.door1_rect) and config.main_room_loop == True: # Move through doorways
        config.main_room_loop = False
        config.instruction_loop = True
        config.instructionvar = 7

    elif config.player.rect.colliderect(config.door3_rect) and config.main_room_loop == True:
        config.main_room_loop = False
        config.instruction_loop = True
        config.instructionvar = 15

    elif config.player.rect.colliderect(config.door2_rect) and config.puzzle_room_loop == True:
        config.puzzle_room_loop = False
        config.main_room_loop = True
        config.player.rect.x = 650
        config.player.rect.y = 368
        time.sleep(0.5)
    elif config.player.rect.colliderect(config.door4_rect) and config.computer_room_loop == True:
        config.computer_room_loop = False
        config.main_room_loop = True
        config.player.rect.x = 368
        config.player.rect.y = 650
        time.sleep(0.5)

    elif config.player.rect.colliderect(config.door5_rect) and config.main_room_loop == True and config.door5var == True:
        config.main_room_loop = False
        config.instruction_loop = True
        config.instructionvar = 24

    elif config.player.rect.colliderect(config.door6_rect) and config.memory_room_loop == True:
        config.memory_room_loop = False
        config.main_room_loop = True
        config.player.rect.x = 100
        config.player.rect.y = 200
        time.sleep(0.5)

    elif config.player.rect.colliderect(config.door7_rect) and config.main_room_loop == True and config.door7var == True:
        config.main_room_loop = False
        config.hall_room_loop = True
        config.player.rect.x = 368
        config.player.rect.y = 650
        time.sleep(0.5)

    elif config.player.rect.colliderect(config.door8_rect) and config.hall_room_loop == True:
        config.hall_room_loop = False
        config.main_room_loop = True
        config.player.rect.x = 368
        config.player.rect.y = 100
        time.sleep(0.5)

    elif config.player.rect.colliderect(config.door9_rect) and config.hall_room_loop == True:
        config.hall_room_loop = False
        config.instruction_loop = True
        config.instructionvar = 33

    elif config.player.rect.colliderect(config.door10_rect) and config.logic_room_loop == True:
        config.logic_room_loop = False
        config.hall_room_loop = True
        config.player.rect.x = 200
        config.player.rect.y = 600
        time.sleep(0.5)

    elif config.player.rect.colliderect(config.door11_rect) and config.hall_room_loop == True:
        config.hall_room_loop = False
        config.instruction_loop = True
        config.instructionvar = 42

    elif config.player.rect.colliderect(config.door12_rect) and config.trivia_room_loop == True:
        config.trivia_room_loop = False
        config.hall_room_loop = True
        config.player.rect.x = 200
        config.player.rect.y = 200
        time.sleep(0.5)


    col = pygame.sprite.spritecollideany(config.player, config.altar_list) # Movement code
    blockercol = pygame.sprite.spritecollideany(config.player, config.blocker_list)
    key = pygame.key.get_pressed()
    if (key[pygame.K_LEFT] or key[pygame.K_a]) and (config.player.rect.x > 0) and config.player.can_move == True:
        config.player.rect.x -=config.move * pygame.time.Clock().tick(30)
        tleft = threading.Timer(0.1, playerleft)
        tleft.start()
        update()
        if (key[pygame.K_UP] or key[pygame.K_w]) and (config.player.rect.y > 0) and config.player.can_move == True:
            config.player.rect.y -=config.move * pygame.time.Clock().tick(30)
            update()
            config.player.direction = math.radians(225)
        elif (key[pygame.K_DOWN] or key[pygame.K_s]) and (config.player.rect.y < 736) and config.player.can_move == True:
            config.player.rect.y +=config.move * pygame.time.Clock().tick(30)
            update()
            config.player.direction = math.radians(135)
        else:
            config.player.direction = math.radians(180)

    elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and (config.player.rect.x < 736) and config.player.can_move == True:
        config.player.rect.x +=config.move * pygame.time.Clock().tick(30)
        tright = threading.Timer(0.1, playerright)
        tright.start()
        update()
        if (key[pygame.K_UP] or key[pygame.K_w]) and (config.player.rect.y > 0) and config.player.can_move == True:
            config.player.rect.y -=config.move * pygame.time.Clock().tick(30)
            update()
            config.player.direction = math.radians(315)
        elif (key[pygame.K_DOWN] or key[pygame.K_s]) and (config.player.rect.y < 736) and config.player.can_move == True:
            config.player.rect.y +=config.move * pygame.time.Clock().tick(30)
            update()
            config.player.direction = math.radians(45)
        else:
            config.player.direction = math.radians(0)

    elif (key[pygame.K_UP] or key[pygame.K_w]) and (config.player.rect.y > 0) and config.player.can_move == True:
        config.player.rect.y -=config.move * pygame.time.Clock().tick(30)
        update()
        config.player.direction = math.radians(270)

    elif (key[pygame.K_DOWN] or key[pygame.K_s]) and (config.player.rect.y < 736) and config.player.can_move == True:
        config.player.rect.y +=config.move * pygame.time.Clock().tick(30)
        update()
        config.player.direction = math.radians(90)

    if col and config.main_room_loop == True: # Altar collision
        if config.inv_num < 4:
            if config.player.rect.x <= 600 and config.player.rect.x >= 351:
                config.player.rect.x +=5
            if config.player.rect.x >= 136 and config.player.rect.x <= 350:
                config.player.rect.x -=5
            if config.player.rect.y <= 500 and config.player.rect.y >= 351:
                config.player.rect.y +=5
            if config.player.rect.y >= 236 and config.player.rect.y <= 350:
                config.player.rect.y -=5
        elif config.inv_num == 4:
            config.main_room_loop = False
            config.instruction_loop = True
            config.instructionvar = 51

    if blockercol and config.computer_room_loop == True: # Blocker collisions

        if config.player.rect.x <= 345 and config.player.rect.x >= 300: # Collisions to the right
            config.player.rect.x +=5
        if config.player.rect.x <= 225 and config.player.rect.x >= 200:
            config.player.rect.x +=5
        if config.player.rect.x <= 775 and config.player.rect.x >= 751:
            config.player.rect.x +=5
        if config.player.rect.x <= 750 and config.player.rect.x >= 700:
            config.player.rect.x +=5

        if config.player.rect.x >= 25 and config.player.rect.x <= 100: # Collisions to the left
            config.player.rect.x -=5
        if config.player.rect.x >= 350 and config.player.rect.x <= 500:
            config.player.rect.x -=5
        if config.player.rect.x >= 275 and config.player.rect.x <= 299:
            config.player.rect.x -=5

        if config.player.rect.y <= 275 and config.player.rect.y >= 200: # Collisions to the bottom
            config.player.rect.y +=5
        if config.player.rect.y <= 775 and config.player.rect.y >= 700:
            config.player.rect.y +=5
        if config.player.rect.y <= 375 and config.player.rect.y >= 300:
            config.player.rect.y +=5

        if config.player.rect.y >= 20 and config.player.rect.y <= 100: # Collisions to the top
            config.player.rect.y -=5
        if config.player.rect.y >= 550 and config.player.rect.y <= 600:
            config.player.rect.y -=5
        if config.player.rect.y >= 410 and config.player.rect.y <= 500:
            config.player.rect.y -=5

    if config.memory_room_loop == True: # Memory room move limitations
        if config.player.rect.x < 190:
            config.player.rect.x +=5
        if config.player.rect.x > 550:
            config.player.rect.x -=5

    if config.hall_room_loop == True: # Hall room move limitations
        if config.player.rect.x < 145:
            config.player.rect.x +=5
        if config.player.rect.x > 600:
            config.player.rect.x -=5

    if config.trivia_room_loop == True: # Trivia room move limitations
        if config.player.rect.y < 570:
            config.player.rect.y +=5

def quit(): # Quit handling
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            config.running = False
            pygame.quit()
            sys.exit()
            exit()

def altar_count():
    config.inv_num = 0
    for i in config.altar_list:
        if i.inv == True:
            config.inv_num += 1
    if config.altar_circle.inv == True:
        config.altar_circle.image = config.circle_lit
    if config.altar_cross.inv == True: 
        config.altar_cross.image = config.cross_lit
    if config.altar_square.inv == True:
        config.altar_square.image = config.square_lit
    if config.altar_triangle.inv == True:
        config.altar_triangle.image = config.triangle_lit
    if config.inv_num == 4:
        config.altar_mid1.image = config.mid1_on
        config.altar_mid2.image = config.mid2_on
        config.altar_mid3.image = config.mid3_on
        config.altar_mid4.image = config.mid4_on

def developer_mode(): # Developer mode unlocks variables
    config.door5var = True # Change variable values
    config.altar_circle.inv = True
    config.altar_square.inv = True
    config.altar_triangle.inv = True
    config.altar_cross.inv = True
    config.developer_mode = True
    config.door7var = True
    altar_count()

    config.screen.fill(config.black) # Password screen

    for event in pygame.event.get(): # Text box handling
        if event.type == pygame.MOUSEBUTTONDOWN:
            if config.input_rect.collidepoint(event.pos):
                config.password_active = True
            else:
                config.password_active = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE: 
                    config.password_text = config.password_text[:-1]
                else:
                    config.password_text += event.unicode

        if event.type == pygame.QUIT:
            config.running = False
            pygame.quit()
            sys.exit()
            exit()

    if config.password_active:
        colour = (144,255,0)
    else:
        colour = (0,255,0)

    pygame.draw.rect(config.screen, colour, config.input_rect) # Blit text box
    text_surface = config.password_font.render(config.password_text, True, (config.black))
    config.screen.blit(text_surface, (config.input_rect.x+5, config.input_rect.y+5))
    config.input_rect.w = max(100, text_surface.get_width()+10)
    if text_surface.get_width() <= 50:
        config.input_rect.left = 350
    else:
        config.input_rect.left = (400 - (config.input_rect.width/2))
    pygame.display.flip()

    if config.password_text == 'd':
        time.sleep(0.1)
        config.password_complete = True

    elif config.password_text == 'lines':
        time.sleep(0.5)
        config.password_complete = True
        config.lines_true = True

    if config.password_complete == True: # Confirmation screen
        config.screen.fill(config.black)
        config.screen.blit(config.dev1, config.dev1.get_rect(center=(400, 300)))
        
        if config.lines_true == True: # Line count
            utils.line_count()
            lines = config.myfont.render(("Number of lines: "+str(utils.sumlines)), True, (config.white)) 
            config.screen.blit(lines, lines.get_rect(center=(400, 100)))
            pygame.display.update()
            time.sleep(1)
        pygame.display.update()
        time.sleep(0.5)
        
        config.instructionvar = 6 # Back to instructions
        config.instruction_loop = True
        config.developer_mode_loop = False
