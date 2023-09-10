import pygame # Module imports
import time
import random
import threading
import config
import procedures

def main_room_update(): # Update sprite and main room background
    config.screen.fill(config.black)
    config.screen.blit(config.b_main_room,(0, 0))
    config.altar_list.draw(config.screen)
    config.altar_list.update()
    config.sprite_list.draw(config.screen)
    config.sprite_list.update()
    config.screen.blit(config.doorfront, config.door1_rect)
    config.screen.blit(config.doorfront, config.door3_rect)
    if config.door5var == True:
        config.screen.blit(config.doorfront, config.door5_rect)
    if config.door7var == True:
        config.screen.blit(config.doorfront, config.door7_rect)
    pygame.display.update()

def main_room(): # Main room code
    main_room_update()
    procedures.player_move()
    procedures.quit()
