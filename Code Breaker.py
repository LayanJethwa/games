import pygame
import sys
import thorpy
import random
pygame.init()
screen = pygame.display.set_mode((297, 750))
pygame.display.set_caption('Code Breaker')
running = True
black = (0,0,0)
white = (255,255,255)
current_square = 0
code = 0
colours = 'rrrr'
box = False

def make_code():
    global code
    code = random.randint(0,9999)
    code = str(code).zfill(4)

make_code()

class MyPainter(thorpy.painters.painter.Painter):

    def __init__(self,c1, c2, size=None, clip=None, pressed=False,
                    hovered=False,):
        super(MyPainter, self).__init__(size, clip, pressed, hovered)
        self.c1 = c1
        self.c2 = c2

    def get_surface(self):
        surface = pygame.Surface(self.size, flags=pygame.SRCALPHA).convert_alpha()
        rect_corner = pygame.Rect(0, 0, self.size[0]//6, self.size[1]//6)
        rect_body = surface.get_rect().inflate((-5,-5))
        pygame.draw.rect(surface, self.c1, rect_body)
        pygame.draw.rect(surface, self.c2, rect_body.inflate((-5,-5)))
        surface.set_clip(self.clip)
        return surface

painter1 = MyPainter(c1=(211,214,218), c2=(255,255,255),size=(48,48))
painter2 = thorpy.painters.roundrect.RoundRect(size=(36,60),color=(218,220,224),radius=0.3)
painter3 = thorpy.painters.roundrect.RoundRect(size=(55,60),color=(218,220,224),radius=0.3)
painter4 = MyPainter(c1=(0,0,0), c2=(255,255,255),size=(48,48))
painter5 = MyPainter(c1=(120,124,126), c2=(120,124,126),size=(48,48))
painter6 = MyPainter(c1=(201,180,88), c2=(201,180,88),size=(48,48))
painter7 = MyPainter(c1=(106,170,100), c2=(106,170,100),size=(48,48))

square1 = thorpy.Element('')
square2 = thorpy.Element('')
square3 = thorpy.Element('')
square4 = thorpy.Element('')
square5 = thorpy.Element('')
square6 = thorpy.Element('')
square7 = thorpy.Element('')
square8 = thorpy.Element('')
square9 = thorpy.Element('')
square10 = thorpy.Element('')
square11 = thorpy.Element('')
square12 = thorpy.Element('')
square13 = thorpy.Element('')
square14 = thorpy.Element('')
square15 = thorpy.Element('')
square16 = thorpy.Element('')
square17 = thorpy.Element('')
square18 = thorpy.Element('')
square19 = thorpy.Element('')
square20 = thorpy.Element('')
square21 = thorpy.Element('')
square22 = thorpy.Element('')
square23 = thorpy.Element('')
square24 = thorpy.Element('')
square25 = thorpy.Element('')
square26 = thorpy.Element('')
square27 = thorpy.Element('')
square28 = thorpy.Element('')
square29 = thorpy.Element('')
square30 = thorpy.Element('')
square31 = thorpy.Element('')
square32 = thorpy.Element('')
square33 = thorpy.Element('')
square34 = thorpy.Element('')
square35 = thorpy.Element('')
square36 = thorpy.Element('')
square37 = thorpy.Element('')
square38 = thorpy.Element('')
square39 = thorpy.Element('')
square40 = thorpy.Element('')
square41 = thorpy.Element('')
square42 = thorpy.Element('')
square43 = thorpy.Element('')
square44 = thorpy.Element('')
square45 = thorpy.Element('')
square46 = thorpy.Element('')
square47 = thorpy.Element('')
square48 = thorpy.Element('')

elements = [square1,square2,square3,square4,
            square5,square6,square7,square8,
            square9,square10,square11,square12,
            square13,square14,square15,square16,
            square17,square18,square19,square20,
            square21,square22,square23,square24,
            square25,square26,square27,square28,
            square29,square30,square31,square32,
            square33,square34,square35,square36,
            square37,square38,square39,square40,
            square41,square42,square43,square44,
            square45,square46,square47,square48,]

for i in elements:
    i.set_painter(painter1)
    i.finish()
    i.set_topleft((((50*(elements.index(i)%4))+47),(50*(elements.index(i)//4)+10)))

def fill(x):
    global current_square
    global box
    if box != True:
        elements[current_square].set_text(str(x))
        elements[current_square].set_font_size(30)
        elements[current_square].change_painter(painter4)
        elements[current_square].update()
        elements[current_square].unblit_and_reblit()
        if current_square % 4 != 3:
            current_square += 1

def is_float(element: any) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False

def back():
    global current_square
    if current_square % 4 != 0 and not is_float(elements[current_square].get_text()):
        current_square -= 1
    elements[current_square].set_text('')
    elements[current_square].change_painter(painter1)
    elements[current_square].update()
    elements[current_square].unblit_and_reblit()

def enter():
    global current_square
    global code
    global colours
    global box
    if current_square % 4 == 3 and is_float(elements[current_square].get_text()):
        temp_code = code
        colours = 'rrrr'
        code_input = elements[current_square-3].get_text()+elements[current_square-2].get_text()+elements[current_square-1].get_text()+elements[current_square].get_text()
        for i in range(0,4):
            if code_input[i] == temp_code[i]:
                temp_code = temp_code[:i] + "g" + temp_code[i+1:]
                colours = colours[:i] + "g" + colours[i+1:]
        for i in range(0,4):
            if code_input[i] in temp_code:
                ind = temp_code.find(code_input[i])
                temp_code = temp_code[:ind] + "y" + temp_code[ind+1:]
                colours = colours[:i] + "y" + colours[i+1:]
        for i in range(0,4):
            if colours[i] == 'g':
                elements[current_square+(i-3)].change_painter(painter7)
            elif colours[i] == 'y':
                elements[current_square+(i-3)].change_painter(painter6)
            else:
                elements[current_square+(i-3)].change_painter(painter5)
            elements[current_square+(i-3)].set_font_color(white)
        if colours == 'gggg':
            box = True
            win.set_text("Well done, you won!")
            if (current_square+1)//4 == 1:
                score.set_text("You found the code in "+str((current_square+1)//4)+" guess")
            else:
                score.set_text("You found the code in "+str((current_square+1)//4)+" guesses")
        elif current_square == 47:
            box = True
            win.set_text("Oh no, you lost!")
            score.set_text("The code was "+code)
        else:
            current_square += 1

def new_game():
    global current_square
    global box
    if box == True:
        current_square = 0
        box = False
        make_code()
        for i in range(48):
            elements[i].change_painter(painter1)
            elements[i].set_font_color(black)
            elements[i].set_text('')

def quit_app():
    global box
    if box == True:
        pygame.quit()
        sys.exit()
        quit()
        exit()

button0 = thorpy.make_button('0',fill,params={"x":0})
button1 = thorpy.make_button('1',fill,params={"x":1})
button2 = thorpy.make_button('2',fill,params={"x":2})
button3 = thorpy.make_button('3',fill,params={"x":3})
button4 = thorpy.make_button('4',fill,params={"x":4})
backbutton = thorpy.make_button('BACK',back)
button5 = thorpy.make_button('5',fill,params={"x":5})
button6 = thorpy.make_button('6',fill,params={"x":6})
button7 = thorpy.make_button('7',fill,params={"x":7})
button8 = thorpy.make_button('8',fill,params={"x":8})
button9 = thorpy.make_button('9',fill,params={"x":9})
enterbutton = thorpy.make_button('ENTER',enter)

elements1 = [button0,button1,button2,button3,button4,backbutton,button5,button6,button7,button8,button9,enterbutton]

for i in elements1:
    i.set_painter(painter2)
    i.finish()
    elements.append(i)
    i.set_topleft((((40*(elements1.index(i)%6))+20.5),(65*(elements1.index(i)//6)+615)))

enterbutton.set_painter(painter3)
enterbutton.finish()
enterbutton.set_topleft((220.5,680))
backbutton.set_painter(painter3)
backbutton.finish()
backbutton.set_topleft((220.5,615))

win = thorpy.make_button("Well done, you won!")
score = thorpy.make_button("You found the code in 5 guesses")
new_game_button = thorpy.make_button("New Game",new_game)
quit_game_button = thorpy.make_button("Quit Game",quit_app)

painter = thorpy.painters.optionnal.human.Human(size=(200,30),radius_ext=0.5,radius_int=0.4,border_color=(255,255,255),color=(255, 102, 102))
quit_game_button.set_painter(painter)
quit_game_button.finish()

box_elements = [win,score,new_game_button,quit_game_button]

central_box = thorpy.Box(elements=box_elements)
central_box.fit_children(margins=(10,10))
central_box.center()
central_box.set_topleft((None,610))
central_box.set_main_color((220,220,220,180))

elements.append(central_box)

background = thorpy.Background(color=(255, 255, 255), elements=elements)

menu = thorpy.Menu(background)

screen.fill((255,255,255))

def blit_all():
    global box
    for element in menu.get_population():
        element.surface = screen
        element.blit()
    if box == True:
        for i in elements1:
            i.unblit()
        if central_box not in elements:
            elements.append(central_box)
    elif box == False:
        for i in elements1:
            i.blit()
        central_box.unblit()
        if central_box in elements:
            elements.remove(central_box)

blit_all()
pygame.display.flip()
    
while running:
    screen.fill(white)
    blit_all()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            exit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                back()
            elif event.key == pygame.K_RETURN:
                enter()
            elif event.unicode in '1234567890':
                fill(event.unicode)
    menu.react(event)
    pygame.display.update()

