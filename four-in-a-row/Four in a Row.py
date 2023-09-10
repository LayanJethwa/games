import pygame #boilerplate
import sys
import threading
import thorpy
import time
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Four In A Row')
running = True
black = (0,0,0)
white = (255,255,255)
size = 8
grid = pygame.image.load("square.png").convert_alpha() #cant be asked to iterate image loading
drop = pygame.image.load("dropper.png").convert_alpha()
drop1 = pygame.image.load("dropper1.png").convert_alpha()
rcoin = pygame.image.load("red.png").convert_alpha()
ycoin = pygame.image.load("yellow.png").convert_alpha()
drop_list = []
places = []
turn = 'r'
game_running = False
can_drop = True

def setup():
    global grid,drop,drop1,rcoin,ycoin,size,places,drop_list,screen
    grid = pygame.transform.scale(grid,(800/size,800/size))
    drop = pygame.transform.scale(drop,(800/size,800/size))
    drop1 = pygame.transform.scale(drop1,(800/size,800/size))
    rcoin = pygame.transform.scale(rcoin,(800/size,800/size))
    ycoin = pygame.transform.scale(ycoin,(800/size,800/size))
    screen = pygame.display.set_mode((800, 800+(800/size)))

    places = []
    drop_list = []
    for i in range(size): #set up 2D array board
        temp_list = []
        for j in range(size):
            temp_list.append('x')
        places.append(temp_list)

    for i in range(size): #sort out droppers
        drop_list.append(drop.get_rect())
        drop_list[i].left = ((800/size)*i)

class Coin(pygame.sprite.Sprite): #counter thingy
    def __init__(self,width,height,colour,left,x,y):
        super().__init__()
        self.colour = colour
        if colour == 'r':
            self.image = rcoin
        else:
            self.image = ycoin
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = drop_list[1].top
        self.l = x
        self.t = y
        self.falling = False
        self.checked = False
        self.temp_str = ''

coin_list = pygame.sprite.Group()
coin_list.empty()

def win(player): #win conditions
    global game_running
    global value1
    global value2
    global screen
    game_running = False
    global welcome
    if player == 'r':
        welcome = myfont.render((value1+' (red) wins!'), True, (black))
    elif player == 'y':
        welcome = myfont.render((value2+' (yellow) wins!'), True, (black))
    elif player == 'd':
        welcome = myfont.render(('It is a draw!'), True, (black))
    screen = pygame.display.set_mode((800, 800))

def check(i): #do diagonals now
    i.checked = True
    colour = i.colour
    found = False
    i.temp_str = ''  
#horizontal check
    for a in range(i.l-3 if i.l-3 >= 0 else 0, i.l+4 if i.l+4 <= size else size): i.temp_str += places[i.t][a] #how in hell does this work
    exec("if i.colour*4 in i.temp_str:\n\twin(i.colour);found=True\nelse:\n\ti.temp_str = ''") #why did i do this
    if found == True: return #josh are you happy now no indents
        
    for a in range(i.t-3 if i.t-3 >= 0 else 0, i.t+4 if i.t+4 <= size else size): i.temp_str += places[a][i.l] #vertical check
    exec("if i.colour*4 in i.temp_str:\n\twin(i.colour);found=True\nelse:\n\ti.temp_str = ''")
    if found == True: return

    for a in range(i.l-3 if i.l-3 >= 0 else 0, i.l+4 if i.l+4 <= size else size): #diagonal l-r u-d check
        if i.t-(i.l-a) >= 0 and i.t-(i.l-a) <= size-1: i.temp_str += places[i.t-(i.l-a)][a] 
    exec("if i.colour*4 in i.temp_str:\n\twin(i.colour);found=True\nelse:\n\ti.temp_str = ''")
    if found == True: return

    for a in range(i.l-3 if i.l-3 >= 0 else 0, i.l+4 if i.l+4 <= size else size): #diagonal l-r d-u check
        if i.t+(i.l-a) >= 0 and i.t+(i.l-a) <= size-1: i.temp_str += places[i.t+(i.l-a)][a] 
    exec("if i.colour*4 in i.temp_str:\n\twin(i.colour);found=True\nelse:\n\ti.temp_str = ''")
    if found == True: return

    if len(coin_list) == size**2: win('d')
                    
def background(): #updates stuff
    for i in range(size):
        if places[0][i] == 'x':
            screen.blit(drop,drop_list[i])
        else:
            screen.blit(drop1,drop_list[i])
        for j in range(size):
            screen.blit(grid,(((800/size)*i),((800/size)*j)+800/size))

def fall(i): #falling animation
    i.rect.y += 800/size
    i.falling = False
    coin_list.update()

def gravity(): #gravity works now
    for i in coin_list:
        if i.t < size-1 and i.falling == False:
            if places[i.t+1][i.l] == 'x':
                places[i.t][i.l] = 'x'
                i.t += 1
                places[i.t][i.l] = i.colour
                i.falling = True
                coin_list.update()
                threading.Timer(0.1,fall,[i]).start()
            else:
                if i.checked == False and i.falling == False:
                    i.falling = 'done'
                    check(i)
        else:
            if i.checked == False and i.falling == False:
                i.falling = 'done'
                check(i)
            
def init_drop(): #idk why not in gravity function
    for i in coin_list:
        if i.rect.y == 0:
            i.rect.y = 800/size
            places[i.t][i.l] = i.colour
            coin_list.update()

def drop_space(): #space out dropping
    global can_drop
    can_drop = True

def spawn(i): #spawn
    global turn
    if places[0][i] == 'x':
        coin_list.add(Coin(800/size,800/size,turn,(i*(800/size)),i,0))
        coin_list.update()
        if turn == 'r':
            turn = 'y'
        else:
            turn = 'r'
        threading.Timer(0.1,init_drop).start()

def enter(): #enter player names
    global value1
    global value2
    global size
    value1 = player1_input.get_value()
    value2 = player2_input.get_value()
    size = slider.get_value()
    player1_input.unblit_and_reblit()
    player2_input.unblit_and_reblit()
    slider.unblit_and_reblit()

def start():
    enter()
    setup()
    global game_running,turn
    game_running = True
    coin_list.empty()
    coin_list.update()
    turn = 'r'

myfont = pygame.font.SysFont(None, 60) # Text and button initialisation
welcome = myfont.render(("Welcome to Four in a Row!"), True, (black))

new_game = thorpy.make_button("New game", start)
painter = thorpy.painters.optionnal.human.Human(size=(200,100),radius_ext=0.5,radius_int=0.4,border_color=(30, 150, 201),color=(41, 180, 240))
new_game.set_painter(painter)
new_game.finish()
new_game.set_topleft((300,200))
new_game.set_font_size(30)

player1_input = thorpy.Inserter(name="Player 1 name: ", value='Player 1')
player2_input = thorpy.Inserter(name="Player 2 name: ", value='Player 2')
player1_input.set_topleft((300,350))
player2_input.set_topleft((300,450))
player1_input._make_size((200,20))
player2_input._make_size((200,20))

value1 = 'Player 1'
value2 = 'Player 2'

slider = thorpy.SliderX(200, (4, 16), "Board size ("+str(size)+"): ", type_=int, initial_value=8)
slider.set_topleft((200,550))

elements = [new_game,player1_input,player2_input,slider]
t_background = thorpy.Background(color=(185, 195, 196), elements=elements)

reaction_insert1 = thorpy.ConstantReaction(reacts_to=thorpy.constants.THORPY_EVENT,reac_func=enter,event_args={"id":thorpy.constants.EVENT_INSERT,"el":player1_input})
t_background.add_reaction(reaction_insert1)
reaction_insert2 = thorpy.ConstantReaction(reacts_to=thorpy.constants.THORPY_EVENT,reac_func=enter,event_args={"id":thorpy.constants.EVENT_INSERT,"el":player2_input})
t_background.add_reaction(reaction_insert2)
reaction_slider = thorpy.ConstantReaction(reacts_to=thorpy.constants.THORPY_EVENT,reac_func=enter,event_args={"id":thorpy.constants.EVENT_INSERT,"el":slider})
t_background.add_reaction(reaction_slider)

menu = thorpy.Menu(t_background)
def blit_buttons():
    for element in menu.get_population():
        element.surface = screen
        element.blit()
    
while running: #game loop
    screen.fill(black)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            exit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #sort out button press
            if game_running:
                for i in range(len(drop_list)):
                    if drop_list[i].collidepoint(event.pos) and can_drop:
                        can_drop = False
                        threading.Timer(0.3,drop_space).start()
                        spawn(i)
        if not game_running:
            menu.react(event)
    if game_running:
        background()
        gravity()
        coin_list.draw(screen)
        coin_list.update()
    else:
        blit_buttons()
        screen.blit(welcome,welcome.get_rect(center=(400,100)))
    pygame.display.update()
