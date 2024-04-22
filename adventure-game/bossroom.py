import pygame
import config
import procedures
import threading
import random
import math
import sys
import pyganim
import utils

def initial_obstacle_spawn(): # Initial obstacle spawning
    for i in range(5):
        obstacle_type = random.randint(0,40)
        left = float(random.choice([random.randint(50,config.dragon.rect.x),random.randint((config.dragon.rect.x+150),700)]))
        top = float(random.choice([random.randint(50,config.dragon.rect.y),random.randint((config.dragon.rect.y+150),700)]))
        direction = math.radians(random.randint(0,360))
        
        if obstacle_type > 0 and obstacle_type <= 39:
            config.obstacle_dict['obstacle'+str(config.obstacle_number)] = config.Rock(left,top,direction)
            config.obstacle_list.add(config.obstacle_dict['obstacle'+str(config.obstacle_number)])
            config.obstacle_number+=1

        elif obstacle_type == 40:
            config.obstacle_dict['obstacle'+str(config.obstacle_number)] = config.Dwayne(left,top,direction)
            config.obstacle_list.add(config.obstacle_dict['obstacle'+str(config.obstacle_number)])
            config.obstacle_number+=1


def obstacle_spawn(): # Spawn obstacles
    if config.obstacle_number < 30 and config.running == True and config.boss_room_loop == True:
        threading.Timer((random.randint(1,2)),obstacle_spawn).start()
        obstacle_type = random.randint(0,40)
        left = float(random.choice([random.randint(50,325),random.randint(475,700)]))
        top = float(random.choice([random.randint(50,config.dragon.rect.y),random.randint((config.dragon.rect.y+150),700)]))
        direction = math.radians(random.randint(0,360))
        
        if obstacle_type > 0 and obstacle_type <= 39:
            config.obstacle_dict['obstacle'+str(config.obstacle_number)] = config.Rock(left,top,direction)
            config.obstacle_list.add(config.obstacle_dict['obstacle'+str(config.obstacle_number)])
            config.obstacle_number+=1

        elif obstacle_type == 40:
            config.obstacle_dict['obstacle'+str(config.obstacle_number)] = config.Dwayne(left,top,direction)
            config.obstacle_list.add(config.obstacle_dict['obstacle'+str(config.obstacle_number)])
            config.obstacle_number+=1

def obstacle_remove(): # Obstacle removing
    for i in list(config.obstacle_dict):
        if config.obstacle_dict[i].rect.x <= 0 or config.obstacle_dict[i].rect.x >=750 or config.obstacle_dict[i].rect.y <= 0 or config.obstacle_dict[i].rect.y >=750:
            config.obstacle_list.remove(config.obstacle_dict[i])
            config.obstacle_number-=1
            
def obstacle_move(): # Make obstacles move
    threading.Timer(0.1,obstacle_move).start()
    for i in list(config.obstacle_dict):
        config.obstacle_dict[i].x += ((math.cos(config.obstacle_dict[i].direction))*config.obstacle_dict[i].speed)
        config.obstacle_dict[i].y += ((math.sin(config.obstacle_dict[i].direction))*config.obstacle_dict[i].speed)
        config.obstacle_dict[i].rect.x = config.obstacle_dict[i].x
        config.obstacle_dict[i].rect.y = config.obstacle_dict[i].y

def dragon_move(): # Make dragon move
    threading.Timer(0.1,dragon_move).start()
    config.dragon.x += ((math.cos(config.dragon.direction))*config.dragon.speed)
    config.dragon.y += ((math.sin(config.dragon.direction))*config.dragon.speed)
    config.dragon.rect.x = config.dragon.x
    config.dragon.rect.y = config.dragon.y

def dragon_col(): # Detect dragon collision with wall
    if config.dragon.rect.x <=50:
        config.dragon.rect.x +=10
        config.dragon.direction = math.radians(random.choice([random.randint(0, 90),random.randint(270,360)]))
    if config.dragon.rect.x >=550:
        config.dragon.rect.x -=10
        config.dragon.direction = math.radians(random.randint(90, 270))
    if config.dragon.rect.y <=50:
        config.dragon.rect.y +=10
        config.dragon.direction = math.radians(random.randint(0, 180))
    if config.dragon.rect.y >=550:
        config.dragon.rect.y -=10
        config.dragon.direction = math.radians(random.randint(180, 360))

def dragon_collision(): # Detect collisions with dragon
    if pygame.sprite.collide_mask(config.player, config.dragon) and config.player.can_move == True:
        config.player.can_move = False
        config.player.prev_health = config.player.health
        if config.dragon.direction < math.pi and config.player.dir_changed == False:
            config.player.dir_changed = True
            config.player.direction = (config.dragon.direction + math.pi)
        elif config.dragon.direction >= math.pi and config.player.dir_changed == False:
            config.player.dir_changed = True
            config.player.direction = (config.dragon.direction - math.pi)
        if config.player.prev_health == config.player.health:
            config.player.health -= 5
        player_knockback()

def dragon_attack_trigger(): # Dragon attack trigger
    threading.Timer((random.randint(3,10)), dragon_attack).start()

def dragon_attack(): # Dragon attack
    config.bomb_number+=1
    config.bomb_dict['bomb'+str(config.bomb_number)] = config.Bomb(config.dragon.x,config.dragon.y,config.bomb_number)
    config.bomb_list.add(config.bomb_dict['bomb'+str(config.bomb_number)])
    config.bomb_anim_dict['bombAnim'+str(config.bomb_number)] = pyganim.PygAnimation([('Textures/Boss Room/bomb1.png', 500),
                         ('Textures/Boss Room/bomb2.png', 500),
                         ('Textures/Boss Room/bomb3.png', 500),
                         ('Textures/Boss Room/bomb4.png', 500),
                         ('Textures/Boss Room/bomb5.png', 500),
                         ('Textures/Boss Room/bomb6.png', 500),
                         ('Textures/Boss Room/bomb7.png', 500),
                         ('Textures/Boss Room/bomb8.png', 500),
                         ('Textures/Boss Room/bomb9.png', 500),
                         ('Textures/Boss Room/bomb10.png', 500),
                         ('Textures/Boss Room/bomb11.png', 1000)],loop=False)

    config.bomb_anim_dict['bombAnim'+str(config.bomb_number)].play()

def bomb_move():
    small2_x = (utils.smaller(config.dragon.rect.x, config.player.rect.x))
    small2_y = (utils.smaller(config.dragon.rect.y, config.player.rect.y))
    big2_x = (utils.bigger(config.dragon.rect.x, config.player.rect.x))
    big2_y = (utils.bigger(config.dragon.rect.y, config.player.rect.y))

    if small2_x == config.dragon.rect.x:
        small_x = small2_x+75
        big_x = big2_x+32
    elif small2_x == config.player.rect.x:
        small_x = small2_x+32
        big_x = big2_x+75

    if small2_y == config.dragon.rect.y:
        small_y = small2_y+75
        big_y = big2_y+32
    elif small2_y == config.player.rect.y:
        small_y = small2_y+32
        big_y = big2_y+75
    
    if small2_x == config.player.rect.x and small2_y == config.player.rect.y:        
        pygame.draw.arc(config.screen, config.white, ((small_x),(small_y-(big_y-small_y)),(2*(big_x-small_x)),(2*(big_y-small_y))),math.pi, (3*math.pi)/2)

    if small2_x == config.player.rect.x and small2_y == config.dragon.rect.y:        
        pygame.draw.arc(config.screen, config.white, ((small_x),(small_y),(2*(big_x-small_x)),(2*(big_y-small_y))),math.pi/2, math.pi)

    if small2_x == config.dragon.rect.x and small2_y == config.player.rect.y:        
        pygame.draw.arc(config.screen, config.white, ((small_x),(small_y),(2*(big_x-small_x)),(2*(big_y-small_y))),math.pi/2, math.pi)

    if small2_x == config.dragon.rect.x and small2_y == config.dragon.rect.y:        
        pygame.draw.arc(config.screen, config.white, ((small_x),(small_y-(big_y-small_y)),(2*(big_x-small_x)),(2*(big_y-small_y))),math.pi, (3*math.pi)/2)      

def player_knockback(): # Dragon collisions with player
    if config.player.knockback == 0:
        config.player.x = config.player.rect.x
        config.player.y = config.player.rect.y
        threading.Timer(0.0001, player_knockback).start()
        config.player.knockback += 1
    elif config.player.knockback < 4 and config.player.knockback > 0:
        threading.Timer(0.1, player_knockback).start()
        config.player.x += ((math.cos(config.player.direction))*25)
        config.player.y += ((math.sin(config.player.direction))*25)
        config.player.rect.x = config.player.x
        config.player.rect.y = config.player.y
        config.player.knockback += 1
    elif config.player.knockback >= 4:
        dragon_col_reset()

def dragon_col_reset(): # Reset player speed
    if config.player.can_move == False:
        config.dragon.image = config.dragon1
        config.player.can_move = True
        config.player.dir_changed = False
        config.player.health_changed = False
        config.player.knockback = 0
    
def player_obstacle_collision(): # Detect player collisions with obstacles
    for i in list(config.obstacle_dict):
        if pygame.sprite.collide_mask(config.player, config.obstacle_dict[i]):
            if config.obstacle_dict[i].immune == False:
                config.obstacle_dict[i].direction = config.player.direction
                if config.obstacle_dict[i].type == 'rock':
                    config.obstacle_dict[i].speed = 12
                    config.obstacle_dict[i].can_hurt = True
                    config.timer_dict['timer'+str(config.obstacle_number)] = threading.Timer(1,obstacle_reset_speed).start()
                if config.obstacle_dict[i].type == 'dwayne':
                    config.obstacle_dict[i].speed = 18
                    config.obstacle_dict[i].can_hurt = True
                    config.timer_dict['timer'+str(config.obstacle_number)] = threading.Timer(1,obstacle_reset_speed).start()

def dragon_obstacle_collision(): # Detect dragon collisions with obstacles
    for i in list(config.obstacle_dict):
        if pygame.sprite.collide_mask(config.dragon, config.obstacle_dict[i]): # Collisions with dragon
            if config.obstacle_dict[i].immune == False:
                config.obstacle_dict[i].direction = config.dragon.direction
                if config.obstacle_dict[i].type == 'rock':
                    config.obstacle_dict[i].speed = 12
                    config.obstacle_dict[i].immune = True
                    config.timer_dict['timer'+str(config.obstacle_number)] = threading.Timer(1,obstacle_reset_speed).start()
                if config.obstacle_dict[i].type == 'dwayne':
                    config.obstacle_dict[i].speed = 20
                    config.obstacle_dict[i].immune = True
                    config.timer_dict['timer'+str(config.obstacle_number)] = threading.Timer(1,obstacle_reset_speed).start()
            elif config.obstacle_dict[i].can_hurt == True and config.obstacle_dict[i].type != 'bomb':
                config.obstacle_number-=1
                config.dragon.health -= config.obstacle_dict[i].damage
                config.obstacle_dict[i].can_hurt = False
                config.obstacle_dict[i].immune = False
                config.obstacle_list.remove(config.obstacle_dict[i])
                
def obstacle_reset_speed():
    for i in list(config.obstacle_dict):
        if config.obstacle_dict[i].speed == 12:
            config.obstacle_dict[i].speed = 3
            config.obstacle_dict[i].immune = False
        if config.obstacle_dict[i].speed == 20:
            config.obstacle_dict[i].speed = 5
            config.obstacle_dict[i].immune = False

def bomb_anim():
    for i in list(config.bomb_dict):
        if config.bomb_dict[i].type == 'bomb' and config.bomb_dict[i] in config.bomb_list and ('bombAnim'+str(config.bomb_dict[i].bomb_num)) in config.bomb_anim_dict:
            config.bomb_anim_dict['bombAnim'+str(config.obstacle_dict[i].bomb_num)].blit(config.screen, (config.obstacle_dict[i].x,config.obstacle_dict[i].y))
            if config.bomb_anim_dict['bombAnim'+str(config.obstacle_dict[i].bomb_num)].state == 'stopped':
                config.bomb_list.remove(config.bomb_dict[i])
                config.bomb_number -=1

def player_health(): # Blit player health to screen
    playerhealthtext = config.healthfont.render((str(config.player.health)), True, (config.red))
    config.screen.blit(playerhealthtext, playerhealthtext.get_rect(center=((config.player.rect.x+32), (config.player.rect.y-10))))

def die(): # Die
    if config.player.health <=0:
        config.lives -=1
        config.boss_room_loop = False
        config.instruction_loop = True
        config.instructionvar = 100

def win(): #Dragon died
    if config.dragon.health <= 0:
        config.boss_room_loop = False
        config.instruction_loop = True
        config.instructionvar = 61
    
def boss_room_update(): # Update room
    config.screen.fill(config.black)
    config.screen.blit(config.b_boss_room,(0, 0)) 
    player_health()
    die()
    win()
    obstacle_remove()
    player_obstacle_collision()
    dragon_obstacle_collision()
    dragon_col()
    dragon_collision()
    bomb_anim()
    bomb_move()

    if config.developer_mode == True: # Debug obstacles
        #print('x:', config.dragon.rect.x, 'y:', config.dragon.rect.y)
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in list(config.obstacle_dict):
                        if config.obstacle_dict[i].rect.collidepoint(event.pos):
                            print('\n')
                            print('x = ',config.obstacle_dict[i].rect.x)
                            print('y = ',config.obstacle_dict[i].rect.y)
                            print('cos = ',math.cos(config.obstacle_dict[i].direction))
                            print('sin = ',math.sin(config.obstacle_dict[i].direction))
                            print('rad dir = ',config.obstacle_dict[i].direction)
                            print('deg dir = ',math.degrees(config.obstacle_dict[i].direction))
                            print('cos add = ',config.obstacle_dict[i].rect.x + ((math.cos(config.obstacle_dict[i].direction))*1))
                            print('sin add = ',config.obstacle_dict[i].rect.y + ((math.sin(config.obstacle_dict[i].direction))*1))
                            print('speed = ',config.obstacle_dict[i].speed)
            if event.type == pygame.QUIT:
                config.running = False
                pygame.quit()
                sys.exit()
                exit()
                quit()
                
    config.sprite_list.draw(config.screen)
    config.sprite_list.update()
    config.obstacle_list.draw(config.screen)
    config.obstacle_list.update()
    pygame.draw.rect(config.screen,config.purple,(150,10,(config.dragon.health/2),30)) # Dragon health bar
    config.dragon_list.draw(config.screen)
    config.dragon_list.update()
    pygame.display.update()

def boss_room():
    procedures.player_move()
    procedures.quit()
    boss_room_update()

