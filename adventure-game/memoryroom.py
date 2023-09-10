import pygame # Module imports
import config
import procedures
import time
import threading
import utils
import sys

def player_reset(): # Player reset code
    config.player.rect.x = 368
    config.player.rect.y = 650
    config.screen.fill(config.black)
    config.screen.blit(config.b_memory_room,(0, 0))
    config.sprite_list.draw(config.screen)
    config.sprite_list.update()
    pygame.display.update()

def tile_reset():
    config.tile_number = 200

def tile_end():
    if config.player.rect.y < 45:
        time.sleep(0.5)
        config.memory_room_loop = False
        config.instruction_loop = True
        config.instructionvar = 30
        config.altar_square.inv = True
        config.door7var = True
        procedures.altar_count()

def tile_flashing(): # Flash tiles
    t = threading.Timer(0.5,tile_reset)
    if time.time() >= (config.tile_clock + 0.5):
        if config.tile_number == 1: # Initial pause + reset position
            config.tile_number += 1
            config.tile_clock = time.time()

        elif config.tile_number == 2: # Tile 1 code
            config.tile1.image = config.tile_on
            config.tile_number += 1
            config.tile_clock = time.time()
        elif config.tile_number == 3:
            config.tile1.image = config.tile_off
            config.tile_number = 99

        elif config.tile_number == 4: # Tile 2 code
            config.tile2.image = config.tile_on
            config.tile_number += 1
            config.tile_clock = time.time()
        elif config.tile_number == 5:
            config.tile2.image = config.tile_off
            if config.step_number == 2:
                config.step_number = 2.01
            else:
                config.step_number +=0.1
                config.step_number = round(config.step_number,1)
            config.tile_number = 99

        elif config.tile_number == 6: # Tile 3 code
            config.tile3.image = config.tile_on
            config.tile_number += 1
            config.tile_clock = time.time()
        elif config.tile_number == 7:
            config.tile3.image = config.tile_off
            if config.step_number == 3.1:
                config.step_number = 3.01
            else:
                config.step_number += 0.1
                config.step_number = round(config.step_number,1)
            config.tile_number = 99

        elif config.tile_number == 8: # Tile 4 code
            config.tile4.image = config.tile_on
            config.tile_number += 1
            config.tile_clock = time.time()
        elif config.tile_number == 9:
            config.tile4.image = config.tile_off
            if config.step_number == 4.2:
                config.step_number = 4.01
            else:
                config.step_number += 0.1
                config.step_number = round(config.step_number,1)
            config.tile_number = 99

        elif config.tile_number == 10: # Tile 5 code
            config.tile5.image = config.tile_on
            config.tile_number += 1
            config.tile_clock = time.time()
        elif config.tile_number == 11:
            config.tile5.image = config.tile_off
            if config.step_number == 5.3:
                config.step_number = 5.01
            else:
                config.step_number += 0.1
                config.step_number = round(config.step_number,1)
            config.tile_number = 99

        elif config.tile_number == 12: # Tile 6 code
            config.tile6.image = config.tile_on
            config.tile_number += 1
            config.tile_clock = time.time()
        elif config.tile_number == 13:
            config.tile6.image = config.tile_off
            if config.step_number == 6.4:
                config.step_number = 6.01
            else:
                config.step_number += 0.1
            config.tile_number = 99

        elif config.tile_number == 14: # Tile 7 code
            config.tile7.image = config.tile_on
            config.tile_number += 1
            config.tile_clock = time.time()
        elif config.tile_number == 15:
            config.tile7.image = config.tile_off
            if config.step_number == 7.5:
                config.step_number = 7.01
            else:
                config.step_number += 0.1
                config.step_number = round(config.step_number,1)
            config.tile_number = 99

        elif config.tile_number == 16: # Tile 8 code
            config.tile8.image = config.tile_on_cut
            config.tile_number += 1
            config.tile_clock = time.time()
        elif config.tile_number == 17:
            config.tile8.image = config.tile_off_cut
            if config.step_number == 8.6:
                config.step_number = 8.01
            else:
                config.step_number += 0.1
                config.step_number = round(config.step_number,1)
            config.tile_number = 99

        elif config.tile_number == 18: # Tile 9 code
            config.tile9.image = config.tile_on_cut
            config.tile_number += 1
            config.tile_clock = time.time()
        elif config.tile_number == 19:
            config.tile9.image = config.tile_off_cut
            if config.step_number == 9.7:
                config.step_number = 9.01
            else:
                config.step_number += 0.1
                config.step_number = round(config.step_number,1)
            config.tile_number = 99

        elif config.tile_number == 20: # Tile 10 code
            config.tile10.image = config.tile_on_cut
            config.tile_number += 1
            config.tile_clock = time.time()
        elif config.tile_number == 21:
            config.tile10.image = config.tile_off_cut
            if config.step_number == 10.8:
                config.step_number = 10.01
            else:
                config.step_number += 0.1
                config.step_number = round(config.step_number,1)
            config.tile_number = 99

        elif config.tile_number == 22: # Tile 11 code
            config.tile11.image = config.tile_on
            config.tile_number += 1
            config.tile_clock = time.time()
        elif config.tile_number == 23:
            config.tile11.image = config.tile_off
            if config.step_number == 11.9:
                config.step_number = 11.01
            if config.step_number == 12.9:
                config.step_number = 12.11
            config.tile_number = 99

        elif config.tile_number == 24: # Tile 12 code
            config.tile12.image = config.tile_on
            config.tile_number += 1
            config.tile_clock = time.time()
        elif config.tile_number == 25:
            config.tile12.image = config.tile_off
            if config.step_number == 12.11:
                config.step_number = 12.01
            config.tile_number = 99

        elif config.tile_number == 99: # Should tile sequence finish or not
            if config.step_number == 1: # Step 1
                config.tile_number = 100

            elif round(config.step_number%1,2) == 0.01: # Step finish
                config.step_number -= 0.01
                config.step_number = round(config.step_number)
                config.tile_number = 100

            elif config.step_number == 12.11: # Step 12 extra
                config.tile_number = 24
                
            elif config.step_number%1 == 0: # Step 1
                config.tile_number = 4

            elif round(config.step_number%1,1) == 0.1: # Steps
                config.tile_number = 6

            elif round(config.step_number%1,1) == 0.2: 
                config.tile_number = 8

            elif round(config.step_number%1,1) == 0.3: 
                config.tile_number = 10

            elif round(config.step_number%1,1) == 0.4: 
                config.tile_number = 12

            elif round(config.step_number%1,1) == 0.5: 
                config.tile_number = 14

            elif round(config.step_number%1,1) == 0.6: 
                config.tile_number = 16

            elif round(config.step_number%1,1) == 0.7: 
                config.tile_number = 18

            elif round(config.step_number%1,1) == 0.8: 
                config.tile_number = 20

            elif round(config.step_number%1,1) == 0.9: 
                config.tile_number = 22
            
        elif config.tile_number == 100: # Tile 1 step
            config.memory_tile_step_list.add(config.tile1)
            col = pygame.sprite.spritecollideany(config.player, config.memory_tile_step_list)
            if col:
                t.start()

        elif config.tile_number == 101: # Tile 2 step
            config.memory_tile_step_list.empty()
            config.memory_tile_step_list.add(config.tile2)
            col = pygame.sprite.spritecollideany(config.player, config.memory_tile_step_list)
            if col:
                t.start()
                if config.step_number == 2:
                    config.step_number = 2.01
                elif config.step_number%1 == 0:
                    config.step_number += 0.1
                    config.step_number = round(config.step_number,1)
                
        elif config.tile_number == 102: # Tile 3 step
            config.memory_tile_step_list.empty()
            config.memory_tile_step_list.add(config.tile3)
            col = pygame.sprite.spritecollideany(config.player, config.memory_tile_step_list)
            if col:
                t.start()
                if config.step_number == 3.1:
                    config.step_number = 3.01
                elif round(config.step_number%1,1) == 0.1: 
                    config.step_number += 0.1
                    config.step_number = round(config.step_number,1)

        elif config.tile_number == 103: # Tile 4 step
            config.memory_tile_step_list.empty()
            config.memory_tile_step_list.add(config.tile4)
            col = pygame.sprite.spritecollideany(config.player, config.memory_tile_step_list)
            if col:
                t.start()
                if config.step_number == 4.2:
                    config.step_number = 4.01
                elif round(config.step_number%1,1) == 0.2: 
                    config.step_number += 0.1
                    config.step_number = round(config.step_number,1)

        elif config.tile_number == 104: # Tile 5 step
            config.memory_tile_step_list.empty()
            config.memory_tile_step_list.add(config.tile5)
            col = pygame.sprite.spritecollideany(config.player, config.memory_tile_step_list)
            if col:
                t.start()
                if config.step_number == 5.3:
                    config.step_number = 5.01
                elif round(config.step_number%1,1) == 0.3: 
                    config.step_number += 0.1
                    config.step_number = round(config.step_number,1)

        elif config.tile_number == 105: # Tile 6 step
            config.memory_tile_step_list.empty()
            config.memory_tile_step_list.add(config.tile6)
            col = pygame.sprite.spritecollideany(config.player, config.memory_tile_step_list)
            if col:
                t.start()
                if config.step_number == 6.4:
                    config.step_number = 6.01
                elif round(config.step_number%1,1) == 0.4: 
                    config.step_number += 0.1
                    config.step_number = round(config.step_number,1)

        elif config.tile_number == 106: # Tile 7 step
            config.memory_tile_step_list.empty()
            config.memory_tile_step_list.add(config.tile7)
            col = pygame.sprite.spritecollideany(config.player, config.memory_tile_step_list)
            if col:
                t.start()
                if config.step_number == 7.5:
                    config.step_number = 7.01
                elif round(config.step_number%1,1) == 0.5: 
                    config.step_number += 0.1
                    config.step_number = round(config.step_number,1)

        elif config.tile_number == 107: # Tile 8 step
            config.memory_tile_step_list.empty()
            config.memory_tile_step_list.add(config.tile8)
            col = pygame.sprite.spritecollideany(config.player, config.memory_tile_step_list)
            if col:
                t.start()
                if config.step_number == 8.6:
                    config.step_number = 8.01
                elif round(config.step_number%1,1) == 0.6: 
                    config.step_number += 0.1
                    config.step_number = round(config.step_number,1)

        elif config.tile_number == 108: # Tile 9 step
            config.memory_tile_step_list.empty()
            config.memory_tile_step_list.add(config.tile9)
            col = pygame.sprite.spritecollideany(config.player, config.memory_tile_step_list)
            if col:
                t.start()
                if config.step_number == 9.7:
                    config.step_number = 9.01
                elif round(config.step_number%1,1) == 0.7: 
                    config.step_number += 0.1
                    config.step_number = round(config.step_number,1)

        elif config.tile_number == 109: # Tile 10 step
            config.memory_tile_step_list.empty()
            config.memory_tile_step_list.add(config.tile10)
            col = pygame.sprite.spritecollideany(config.player, config.memory_tile_step_list)
            if col:
                t.start()
                if config.step_number == 10.8:
                    config.step_number = 10.01
                elif round(config.step_number%1,1) == 0.8: 
                    config.step_number += 0.1
                    config.step_number = round(config.step_number,1)
                    
        elif config.tile_number == 110: # Tile 11 step
            config.memory_tile_step_list.empty()
            config.memory_tile_step_list.add(config.tile11)
            col = pygame.sprite.spritecollideany(config.player, config.memory_tile_step_list)
            if col:
                t.start()
                if config.step_number == 11.9:
                    config.step_number = 11.01
                if config.step_number == 12.9:
                    config.step_number = 12.11

        elif config.tile_number == 111: # Tile 12 step
            config.memory_tile_step_list.empty()
            config.memory_tile_step_list.add(config.tile12)
            col = pygame.sprite.spritecollideany(config.player, config.memory_tile_step_list)
            if col:
                t.start()
                if config.step_number == 12.11:
                    config.step_number = 12.01

        elif config.tile_number == 200: # Reset step tiles
            if config.step_number == 1: # Step = 1
                time.sleep(0.5)
                player_reset()
                config.tile_number = 1
                config.step_number = 2

            elif round(config.step_number%1,2) == 0.01: # Step finish
                if config.step_number == 12.01:
                    tile_end()
                else:
                    time.sleep(0.5)
                    player_reset()
                    config.tile_number = 1
                    config.step_number -= 0.01
                    config.step_number = round(config.step_number)
                    config.step_number += 1

            elif config.step_number == 12.11: # Step 12 extra
                config.tile_number = 111
                
            elif config.step_number%1 == 0: # Step 1
                config.tile_number = 101

            elif round(config.step_number%1,1) == 0.1: # Steps
                config.tile_number = 102

            elif round(config.step_number%1,1) == 0.2:
                config.tile_number = 103

            elif round(config.step_number%1,1) == 0.3:
                config.tile_number = 104

            elif round(config.step_number%1,1) == 0.4:
                config.tile_number = 105

            elif round(config.step_number%1,1) == 0.5:
                config.tile_number = 106

            elif round(config.step_number%1,1) == 0.6: 
                config.tile_number = 107

            elif round(config.step_number%1,1) == 0.7: 
                config.tile_number = 108

            elif round(config.step_number%1,1) == 0.8: 
                config.tile_number = 109

            elif round(config.step_number%1,1) == 0.9: 
                config.tile_number = 110

def die(): # Die code
    col1 = pygame.sprite.spritecollideany(config.player, config.collision_tile_list)
    if config.player.rect.y < 638 and config.player.rect.y > 62 and not col1:
        config.tile_lives -= 1
        config.step_number = round(config.step_number)
        config.tile_number = 1
        time.sleep(0.5)
        player_reset()
        if config.tile_lives < 1:
            config.memory_room_loop = False
            config.instruction_loop = True
            config.instructionvar = 100
            config.lives -= 1

def skip_button(): # Button skip code

    memory_button_rect = config.memory_button_image.get_rect() # Blit button
    memory_button_rect.top = 750
    memory_button_rect.left = 550
    config.screen.blit(config.memory_button_image, memory_button_rect)

    if config.memory_button_image == config.memory_button_g: # Blit text
        config.screen.blit(config.memoryskip1, config.memoryskip1.get_rect(center=(550,700)))
        config.screen.blit(config.memoryskip2, config.memoryskip2.get_rect(center=(550,710)))
        config.screen.blit(config.memoryskip3, config.memoryskip3.get_rect(center=(550,720)))
        config.screen.blit(config.memoryskip4, config.memoryskip4.get_rect(center=(550,730)))
    elif config.memory_button_image == config.memory_button_r:
        config.screen.blit(config.memoryskip1a, config.memoryskip1a.get_rect(center=(550,700)))
        config.screen.blit(config.memoryskip2a, config.memoryskip2a.get_rect(center=(550,710)))
        config.screen.blit(config.memoryskip3a, config.memoryskip3a.get_rect(center=(550,720)))
        config.screen.blit(config.memoryskip4a, config.memoryskip4a.get_rect(center=(550,730)))
    
    for event in pygame.event.get(): # Event handling
        if event.type == pygame.QUIT:
            config.running = False
            pygame.quit()
            sys.exit()
            exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if memory_button_rect.collidepoint(event.pos): # Button clicking
                    if config.memory_button_image == config.memory_button_g:
                        config.memory_button_image = config.memory_button_r
                        config.step_number = 12
                        config.tile_number = 1
                        player_reset()
                    elif config.memory_button_image == config.memory_button_r:
                        config.memory_button_image = config.memory_button_g
                        config.step_number = 1
                        config.tile_number = 1
                        player_reset()
                    
             
def memory_room_update(): # Update stuff
    config.screen.fill(config.black)
    config.screen.blit(config.b_memory_room,(0, 0))
    tile_flashing()
    die()
    skip_button()
    
    if config.developer_mode == True: # Debugging
        utils.tile_debug()
        
    config.memory_tile_list.draw(config.screen) # Render stuff
    config.memory_tile_list.update()
    config.sprite_list.draw(config.screen)
    config.sprite_list.update()
    config.screen.blit(config.doorfront, config.door6_rect)
    tilelivestext = config.tilelivesfont.render(("Lives: "+str(config.tile_lives)), True, (config.white))
    config.screen.blit(tilelivestext, (25, 25))
    pygame.display.update()

def memory_room(): # Main memory room loop
    memory_room_update()
    procedures.player_move()
