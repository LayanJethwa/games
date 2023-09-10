import pygame
import time
print('\n')

size = width, height = 800, 700

win=pygame.display.set_mode(size)

clock=pygame.time.Clock()

white = 255, 255, 255
red = 255, 0, 0
black = 0, 0, 0

img={}
rect={}
finish={}
drag={}

a=0
b=100
c=200
d=300
e=400
f=500
g=600

row1i=[g,f,e,b,c,a,d]
row1ii=[g,f,b,c,a,g,e]

row2i=[e,c,a,b,d,f,g]
row2ii=[f,b,e,d,g,c,a]

row3i=[f,g,c,a,d,b,e]
row3ii=[a,f,c,b,d,g,e]

row4i=[c,a,f,g,d,b,e]
row4ii=[f,a,b,c,a,e,d]

row5i=[c,a,e,d,g,f,b]
row5ii=[d,c,a,b,d,g,f]

row6i=[d,a,e,c,f,g,b]
row6ii=[c,d,c,g,d,b,a]

row7i=[f,b,c,a,d,e,g]
row7ii=[e,b,e,f,f,g,e]

listi=[25, 125, 225, 325, 425, 525, 625, 725]
listi1=[0, 75, 175, 275, 375, 475, 575, 675]

global offset_x
global offset_y

offset_x = 0
offset_y = 0

finish2=0

def image():
    for i in range(7):
        img[i] = pygame.image.load("row-1-col-{}.jpg".format(str(i + 1))).convert()
        rect[i] = img[i].get_rect()
        rect[i].top=row1i[i]
        rect[i].left=row1ii[i]
        finish[i] = False
        drag[i] = False

    for i in range(7):
        img[i+7] = pygame.image.load("row-2-col-{}.jpg".format(str(i + 1))).convert()
        rect[i+7] = img[i+7].get_rect()
        rect[i+7].top=row2i[i]
        rect[i+7].left=row2ii[i]
        finish[i+7] = False
        drag[i+7] = False

    for i in range(7):
        img[i+14] = pygame.image.load("row-3-col-{}.jpg".format(str(i + 1))).convert()
        rect[i+14] = img[i+14].get_rect()
        rect[i+14].top=row3i[i]
        rect[i+14].left=row3ii[i]
        finish[i+14] = False
        drag[i+14] = False

    for i in range(7):
        img[i+21] = pygame.image.load("row-4-col-{}.jpg".format(str(i + 1))).convert()
        rect[i+21] = img[i+21].get_rect()
        rect[i+21].top=row4i[i]
        rect[i+21].left=row4ii[i]
        finish[i+21] = False
        drag[i+21] = False

    for i in range(7):
        img[i+28] = pygame.image.load("row-5-col-{}.jpg".format(str(i + 1))).convert()
        rect[i+28] = img[i+28].get_rect()
        rect[i+28].top=row5i[i]
        rect[i+28].left=row5ii[i]
        finish[i+28] = False
        drag[i+28] = False

    for i in range(7):
        img[i+35] = pygame.image.load("row-6-col-{}.jpg".format(str(i + 1))).convert()
        rect[i+35] = img[i+35].get_rect()
        rect[i+35].top=row6i[i]
        rect[i+35].left=row6ii[i]
        finish[i+35] = False
        drag[i+35] = False

    for i in range(7):
        img[i+42] = pygame.image.load("row-7-col-{}.jpg".format(str(i + 1))).convert()
        rect[i+42] = img[i+42].get_rect()
        rect[i+42].top=row7i[i]
        rect[i+42].left=row7ii[i]
        finish[i+42] = False
        drag[i+42] = False
  
   

def snap():
    for i in range(7):
        if rect[i].top<=25 and rect[i].top>=0 and rect[i].left>=listi1[i] and rect[i].left<=listi[i]:
                rect[i].top=0
                rect[i].left=((listi[i])-25)
                finish[i] = True
    for i in range(7):
        if rect[i+7].top<=125 and rect[i+7].top>=75 and rect[i+7].left>=listi1[i] and rect[i+7].left<=listi[i]:
                rect[i+7].top=100
                rect[i+7].left=((listi[i])-25)
                finish[i+7] = True
    for i in range(7):
        if rect[i+14].top<=225 and rect[i+14].top>=175 and rect[i+14].left>=listi1[i] and rect[i+14].left<=listi[i]:
                rect[i+14].top=200
                rect[i+14].left=((listi[i])-25)
                finish[i+14] = True
    for i in range(7):
        if rect[i+21].top<=325 and rect[i+21].top>=275 and rect[i+21].left>=listi1[i] and rect[i+21].left<=listi[i]:
                rect[i+21].top=300
                rect[i+21].left=((listi[i])-25)
                finish[i+21] = True
    for i in range(7):
        if rect[i+28].top<=425 and rect[i+28].top>=375 and rect[i+28].left>=listi1[i] and rect[i+28].left<=listi[i]:
                rect[i+28].top=400
                rect[i+28].left=((listi[i])-25)
                finish[i+28] = True
    for i in range(7):
        if rect[i+35].top<=525 and rect[i+35].top>=475 and rect[i+35].left>=listi1[i] and rect[i+35].left<=listi[i]:
                rect[i+35].top=500
                rect[i+35].left=((listi[i])-25)
                finish[i+35] = True
    for i in range(7):
        if rect[i+42].top<=625 and rect[i+42].top>=575 and rect[i+42].left>=listi1[i] and rect[i+42].left<=listi[i]:
                rect[i+42].top=600
                rect[i+42].left=((listi[i])-25)
                finish[i+42] = True           
                
           

def eventkeys():
    global offset_x
    global offset_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                print("Thank you for using my puzzle program! I hoped you enjoyed it.")
                pygame.quit()
                exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(49):
                    if rect[i].collidepoint(event.pos):
                        drag[i] = True
                        mouse_x, mouse_y = event.pos
                        offset_x = rect[i].x - mouse_x
                        offset_y = rect[i].y - mouse_y
   

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                for i in range(49):
                    drag[i] = False
                offset_x = 0
                offset_y = 0

        if event.type == pygame.MOUSEMOTION:
            for i in range(49):
                if drag[i]:
                    if finish[i] == False:
                        mouse_x, mouse_y = event.pos
                        rect[i].x = mouse_x + offset_x
                        rect[i].y = mouse_y + offset_y

def blitting():
    for i in range(49):
        win.blit(img[i], rect[i])



finish2=[]
def finn(finish2):
    for i in range(49):
        if finish[i] == True:
            if i not in finish2:
                finish2.append(i)
                
    return finish2








pygame.init()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()    

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((700/2),(700/2))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    exit()

def end():
    message_display('Well done, you won!')

def finishhh(finish2):
    finish3=0
    for i in range(49):
        if i in finish2:
            finish3+=1
    if finish3==49:
        end()


def main():
    image()
    finish2=[]
    while True:
        clock.tick(30)
        win.fill(black)

        finishhh(finish2)
        finish3=finn(finish2)
        snap()
        eventkeys()
        blitting()
        
        pygame.display.flip()



main()        

