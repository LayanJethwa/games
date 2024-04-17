import random
import pygame
import time
pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Minesweeper')
running = True

g_size = 20
r_size = 800//g_size

font = pygame.font.SysFont(None, int(r_size/1.2))
flag = pygame.image.load("flag.png").convert_alpha()
flag = pygame.transform.scale(flag,(r_size,r_size))
flag1 = pygame.image.load("flag1.png").convert_alpha()
flag1 = pygame.transform.scale(flag1,(r_size,r_size))

grid = []
for i in range(g_size):
    t = []
    for j in range(g_size):
        if random.randint(0,g_size//2) == 0:
            t += ['x']
        else:
            t += ['o']
    grid.append(t)

m = (g_size-1)//2
for i in [m,m-1,m+1]:
    for j in [m,m-1,m+1]:
        grid[i][j] = 'o'

opened = {}

while 'o' in ''.join([''.join(i) for i in grid]):
    n_grid = [['o']*(g_size+2)]+[['o']+i+['o'] for i in grid]+[['o']*(g_size+2)]
    for i in range(g_size):
        for j in range(g_size):
            if grid[i][j] != 'x':
                a = [(i+1,j),(i+1,j+2),(i,j),(i,j+1),(i,j+2),(i+2,j),(i+2,j+1),(i+2,j+2)]
                grid[i][j] = str([n_grid[i[0]][i[1]] for i in a].count('x'))

class Tile(pygame.sprite.Sprite):
    def __init__(self, width, height, left, top):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = top

tile_list = pygame.sprite.Group()
tile_list.empty()
tiles = {}
for x in range(g_size):
    for y in range(g_size):
        tiles[str(x)+str(y)] = Tile(r_size, r_size, x*r_size, y*r_size)
        if (x+y) % 2 == 0:
            tiles[str(x)+str(y)].image.fill((170,215,81))
        else:
            tiles[str(x)+str(y)].image.fill((162,209,73))
        tile_list.add(tiles[str(x)+str(y)])
tile_list.update()

text = {}

lost_text = font.render(("Oh no, you lost the game!"), True, (255,255,255))
lost = False
won_text = font.render(("Well done, you won the game!"), True, (255,255,255))
won = False
game_over_screen_fade = pygame.Surface((800, 800))
game_over_screen_fade.fill((0, 0, 0))
game_over_screen_fade.set_alpha(160)

q = []
def click(tile):
    global lost
    global won
    
    if ((tile.rect.x//r_size)+(tile.rect.y//r_size)) % 2 == 0:
        tile.image.fill((229,194,159))
    else:
        tile.image.fill((215,184,153))

    num = grid[tile.rect.y//r_size][tile.rect.x//r_size]
    if num == '0':
        num = ''
        col = (0,0,0)
    elif num == '1':
        col = (25,118,210)
    elif num == '2':
        col = (56,142,60)
    elif num == '3':
        col = (211,47,47)
    elif num == '4':
        col = (123,31,162)
    elif num == '5':
        col = (244,155,42)
    elif num == 'x':
        col = (0,0,0)
        lost = True

    text[((tile.rect.x),(tile.rect.y))] = font.render((num), True, col)

    opened[(tile.rect.x, tile.rect.y)] = True
    if len(opened) == g_size**2 - ''.join([''.join(i) for i in grid]).count('x'):
        won = True

    if num == '':
        for t in tile_list:
            if abs(t.rect.y - tile.rect.y) + abs(t.rect.x - tile.rect.x) in [r_size,r_size*2] and grid[t.rect.y//r_size][t.rect.x//r_size] != 'x' and not opened.get((t.rect.x,t.rect.y),False):
                click(t)


for tile in tile_list:
    if tile.rect.x//r_size == (g_size-1)//2 == tile.rect.y//r_size:
        click(tile)

while running:
    screen.fill((0,0,0))
        
    tile_list.draw(screen)
    for t in text:
        screen.blit(text[t], text[t].get_rect(center=(t[0]+(r_size//2), t[1]+(r_size//2))))

    if lost:
        screen.blit(game_over_screen_fade, (0, 0))
        screen.blit(lost_text, lost_text.get_rect(center=(400,400)))
    elif won:
        screen.blit(game_over_screen_fade, (0, 0))
        screen.blit(won_text, won_text.get_rect(center=(400,400)))
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
            quit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN and not won and not lost:
            x, y = event.pos
            for tile in tile_list:
                if tile.rect.collidepoint(x,y):
                    
                    if event.button == 1:
                        click(tile)

                    elif event.button == 3 and not opened.get((tile.rect.x,tile.rect.y),False):
                        if tile.image == flag or tile.image == flag1:
                            tile.image = pygame.Surface([r_size, r_size])
                            if ((tile.rect.x//r_size)+(tile.rect.y//r_size)) % 2 == 0:
                                tile.image.fill((170,215,81))
                            else:
                                tile.image.fill((162,209,73))
                        else:
                            if ((tile.rect.x//r_size)+(tile.rect.y//r_size)) % 2 == 0:
                                tile.image = flag
                            else:
                                tile.image = flag1
                    
    tile_list.update()
    pygame.display.update()
    
