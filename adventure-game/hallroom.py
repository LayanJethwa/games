import pygame
import config
import procedures

def hall_room_update(): # Update room
    config.screen.fill(config.black)
    config.screen.blit(config.b_hall_room,(0, 0))
    config.sprite_list.draw(config.screen)
    config.sprite_list.update()
    config.screen.blit(config.doorfront, config.door8_rect)
    config.screen.blit(config.doorfront, config.door9_rect)
    config.screen.blit(config.doorfront, config.door11_rect)
    pygame.display.update()

def hall_room():
    procedures.player_move()
    procedures.quit()
    hall_room_update()

