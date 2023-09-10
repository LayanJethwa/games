import random
grid = []
size = 30
for i in range(size):
    temp_list = []
    for i in range(size):
        if random.randint(1,size) % 6 == 0:
            temp_list.append('x')
        else:
            temp_list.append('o')
    grid.append(temp_list)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        count = 0
        if grid[i][j] == 'o':
            if i>0:
                if j>0:
                    if grid[i-1][j-1] == 'x':
                        count += 1
                if j<(len(grid[i])-1):
                    if grid[i-1][j+1] == 'x':
                        count += 1
                if grid[i-1][j] == 'x':
                    count += 1

            if j>0:
                if grid[i][j-1] == 'x':
                    count += 1
            if j<(len(grid[i])-1):
                if grid[i][j+1] == 'x':
                    count += 1
                
            if i<(len(grid)-1):
                if j>0:
                    if grid[i+1][j-1] == 'x':
                        count += 1
                if j<(len(grid[i])-1):
                    if grid[i+1][j+1] == 'x':
                        count += 1
                if grid[i+1][j] == 'x':
                    count += 1
            grid[i][j] = str(count)

import thorpy
import pygame
import sys
import time
import threading
import os
import signal
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Minesweeper')
running = True
game_finished = False
black = (0,0,0)
white = (255,255,255)

painter1 = thorpy.painters.basicframe.BasicFrame(size=(800/size,800/size),color=(229,194,159))
painter2 = thorpy.painters.basicframe.BasicFrame(size=(800/size,800/size),color=(215,184,153))
painter3 = thorpy.painters.basicframe.BasicFrame(size=(800/size,800/size),color=(170,215,81))
painter4 = thorpy.painters.basicframe.BasicFrame(size=(800/size,800/size),color=(162,209,73))
render_grid = []

flag = pygame.image.load("flag.png").convert_alpha()
flag = pygame.transform.scale(flag,(800/size,800/size))
flag1 = pygame.image.load("flag1.png").convert_alpha()
flag1 = pygame.transform.scale(flag1,(800/size,800/size))

clicked = []
for i in range(size):
    temp_list = []
    for j in range(size):
        temp_list.append(False)
    clicked.append(temp_list)

myfont = pygame.font.SysFont(None, 60) # Text and button initialisation
text = myfont.render((""), True, (black))

def quit_game():
    global running
    running = False
    os._exit(0)
    os.kill(os.getpid(), signal.SIGTERM)

def lose():
    global text, game_finished
    myfont = pygame.font.SysFont(None, 60)
    text = myfont.render(("Oh no, you lost the game."), True, (white))
    time.sleep(1)
    game_finished = True
    threading.Timer(2,quit_game).start()

def win():
    global text, game_finished
    myfont = pygame.font.SysFont(None, 60)
    text = myfont.render(("Well done, you have won!"), True, (white))
    time.sleep(1)
    game_finished = True
    threading.Timer(2,quit_game).start()

def click(x,y):
    global render_grid
    global clicked
    if (x+y)%2 == 0:
        render_grid[x][y].set_painter(painter1)
    elif (x+y)%2 == 1:
        render_grid[x][y].set_painter(painter2)
    clicked[x][y] = True
    render_grid[x][y].finish()
    render_grid[x][y].set_topleft((y*(800/size),x*(800/size)))
    render_grid[x][y].set_font_size(35)
    setup(render_grid[x][y])
    render_grid[x][y].update()
    render_grid[x][y].unblit_and_reblit()
    if grid[x][y] == '0':
        grid[x][y] = 'o'
        if x > 0:
            if y > 0:
                click(x-1,y-1)
                click(x,y-1)
            if y < size-1:
                click(x-1,y+1)
                click(x,y+1)
            click(x-1,y)
        if x < size-1:
            if y > 0:
                click(x+1,y-1)
            if y < size-1:
                click(x+1,y+1)
            click(x+1,y)
    elif grid[x][y] == 'x':
        lose()
    else:
        None

    if sum(row.count(True) for row in clicked) == (size**2) - sum(row.count('x') for row in grid):
        win()

for i in range(size):
    temp_list = []
    for j in range(size):
        temp_list.append(thorpy.make_button(grid[i][j],click,params={'x':i,'y':j}))
    render_grid.append(temp_list)

elements = []
temp_grid = []

for i in range(len(render_grid)):
    for j in range(len(render_grid[i])):
        if (i+j)%2 == 0:
            render_grid[i][j].set_painter(painter3)
        elif (i+j)%2 == 1:
            render_grid[i][j].set_painter(painter4)
        render_grid[i][j].finish()
        render_grid[i][j].set_topleft((j*(800/size),i*(800/size)))
        elements.append(render_grid[i][j])
        temp_grid.append(render_grid[i][j])
    
def setup(i):
    i.set_font("Gothic")
    if i.get_text() == '1':
        i.set_font_color((25,118,210))
        i.set_font_color_hover((25,118,210))
    if i.get_text() == '2':
        i.set_font_color((56,142,60))
        i.set_font_color_hover((56,142,60))
    if i.get_text() == '3':
        i.set_font_color((211,47,47))
        i.set_font_color_hover((211,47,47))
    if i.get_text() == '4':
        i.set_font_color((123,31,162))
        i.set_font_color_hover((123,31,162))
    if i.get_text() == '5':
        i.set_font_color((244,155,42))
        i.set_font_color_hover((244,155,42))
    if i.get_text() == '0':
        i.set_text('')

for i in elements:
    i.set_font_size(0)
    setup(i)
        
background = thorpy.Background(color=(255, 255, 255), elements=elements)
menu = thorpy.Menu(background)
def blit_all():
    for element in menu.get_population():
        element.surface = screen
        element.blit()

blit_all()
pygame.display.flip()

while running:
    screen.fill(black)
    if not game_finished:
        blit_all()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            exit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and (clicked[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))] == False):
            if (render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))]).get_text() != 'f':
                elements.remove(render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))])
                if (int(event.pos[1]//(800/size)) + int(event.pos[0]//(800/size))) % 2 == 0:
                    render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))] = thorpy.make_image_button(flag)
                elif (int(event.pos[1]//(800/size)) + int(event.pos[0]//(800/size))) % 2 == 1:
                    render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))] = thorpy.make_image_button(flag1)
                render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))].set_topleft((((event.pos[0]//(800/size))*(800/size)),((event.pos[1]//(800/size))*(800/size))))
                render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))].set_text('f')
                render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))].set_font_size(0)
                render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))].update()
                render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))].unblit_and_reblit()
                elements.append(render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))])
            elif (render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))]).get_text() == 'f':
                elements.remove(render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))])
                render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))] = temp_grid[(((int(event.pos[1]//(800/size)))*size)+(int(event.pos[0]//(800/size))))]
                render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))].set_topleft((((event.pos[0]//(800/size))*(800/size)),((event.pos[1]//(800/size))*(800/size))))
                setup(render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))])
                render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))].update()
                render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))].unblit_and_reblit()
                elements.append(render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))])
                render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))].update()
                render_grid[int(event.pos[1]//(800/size))][int(event.pos[0]//(800/size))].unblit_and_reblit()
            background = thorpy.Background(color=(255, 255, 255), elements=elements)
            menu = thorpy.Menu(background)
    menu.react(event)
    if game_finished:
        screen.blit(text,text.get_rect(center=(400,100)))
    pygame.display.update()
