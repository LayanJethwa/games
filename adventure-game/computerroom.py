import pygame # Module imports
import os
import sys
import time
import config
import procedures

def buttons(): # Import button images
    for i in range(9):
        config.button_img[i] = pygame.image.load(os.path.join("Textures", "Computer Room", "red_button.png")).convert()
        config.button_rect[i] = config.button_img[i].get_rect()
        config.button_rect[i].top = 350
        config.button_rect[i].left = config.button_left[i]
        config.button_finish[i] = False

def object_colour(): # Check for button and screen colours
    for i in range(9):
        if config.button_list[i] == 'r':
            config.button_img[i] = pygame.image.load(os.path.join("Textures", "Computer Room", "red_button.png")).convert()
            config.screen_img[i] = pygame.image.load(os.path.join("Textures", "Computer Room", "{}_screen_off.png".format(config.screen_type[i]))).convert()
        elif config.button_list[i] == 'g':
            config.button_img[i] = pygame.image.load(os.path.join("Textures", "Computer Room", "green_button.png")).convert()
            config.screen_img[i] = pygame.image.load(os.path.join("Textures", "Computer Room", "{}_screen_on.png".format(config.screen_type[i]))).convert()

def button_click(): # Button clicking code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.running = False
            pygame.quit()
            sys.exit()
            exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(9):
                    if config.button_rect[i].collidepoint(event.pos):
                        config.button_list[i] = 'r' if config.button_list[i] == 'g' else 'g'
                        if i > 0 and i < 8:
                            config.button_list[i-1] = 'r' if config.button_list[i-1] == 'g' else 'g'
                            config.button_list[i+1] = 'r' if config.button_list[i+1] == 'g' else 'g'
                        elif i == 0:
                            config.button_list[i+1] = 'r' if config.button_list[i+1] == 'g' else 'g'
                        elif i == 8:
                            config.button_list[i-1] = 'r' if config.button_list[i-1] == 'g' else 'g'

def button_finish(): # Check if all buttons are green
    for i in range(9):
        if config.button_list[i] == 'g':
            config.button_finish[i] = True
        elif config.button_list[i] == 'r':
            config.button_finish[i] = False

    if config.button_finish[0] and config.button_finish[1] and config.button_finish[2] and config.button_finish[3] and config.button_finish[4] and config.button_finish[5] and config.button_finish[6] and config.button_finish[7] and config.button_finish[8] == True:
        for i in range(9):
            config.button_img[i] = pygame.image.load(os.path.join("Textures", "Computer Room", "green_button.png")).convert()
            config.screen_img[i] = pygame.image.load(os.path.join("Textures", "Computer Room", "{}_screen_on.png".format(config.screen_type[i]))).convert()
            config.screen.blit(config.button_img[i], config.button_rect[i])
            config.screen.blit(config.screen_img[i], config.screen_rect[i])
            pygame.display.update()
        time.sleep(2)
        config.computer_room_loop = False
        config.instruction_loop = True
        config.instructionvar = 19
        config.altar_circle.inv = True
        procedures.altar_count()
        print(config.inv_num)

def screens(): # Render screens
    for i in range(9):
        config.screen_img[i] = pygame.image.load(os.path.join("Textures", "Computer Room", "{}_screen_off.png".format(config.screen_type[i]))).convert()
        config.screen_rect[i] = config.screen_img[i].get_rect()
        config.screen_rect[i].top = config.screen_top[i]
        config.screen_rect[i].left = config.screen_left[i]

def computer_room_update(): # Update sprite and main background
    config.screen.fill(config.black)
    config.screen.blit(config.b_computer_room,(0, 0))
    config.sprite_list.draw(config.screen)
    config.sprite_list.update()
    
    for i in range(9): # Render objects
        config.screen.blit(config.button_img[i], config.button_rect[i])
        config.screen.blit(config.screen_img[i], config.screen_rect[i])
    config.screen.blit(config.doorfront, config.door4_rect)
    config.blocker1.draw(275,20,475,255)
    config.blocker2.draw(420,550,355,225)
    config.blocker3.draw(25,25,200,350)
    config.blocker4.draw(0,475,345,325)
    config.blocker_list.update()
    
    object_colour() # Update objects
    button_click()
    button_finish()
        
    pygame.display.update()

def computer_room(): # Main loop
    computer_room_update()
    procedures.player_move()
