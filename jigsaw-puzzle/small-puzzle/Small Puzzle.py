import pygame
import time
print('\n')

size = width, height = 400, 400

win=pygame.display.set_mode(size)

clock=pygame.time.Clock()

white = 255, 255, 255
red = 255, 0, 0
black = 0, 0, 0

a=50
b=150
c=100
d=225
e=100
f=23

img1 = pygame.image.load('Small (1).jpg').convert()
rect1 = img1.get_rect()

rect1.top=a
rect1.left=a

rect1_draging = False
rect1_finish = False

img2 = pygame.image.load('Small (2).jpg').convert()
rect2 = img2.get_rect()

rect2.top=b
rect2.left=b

rect2_draging = False
rect2_finish = False

img3 = pygame.image.load('Small (3).jpg').convert()
rect3 = img3.get_rect()

rect3.top=c
rect3.left=d

rect3_draging = False
rect3_finish = False

img4 = pygame.image.load('Small (4).jpg').convert()
rect4 = img4.get_rect()

rect4.top=e
rect4.left=f

rect4_draging = False
rect4_finish = False


pygame.init()

def end():
    message_display('Well done, you won!')

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((400/2),(400/2))
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    exit()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()    



while True:
    clock.tick(30)
    win.fill(black)

    if rect1.top>=175 and rect1.top<=225 and rect1.left>=175 and rect1.left<=225:
        rect1.top=200
        rect1.left=200
        rect1_finish = True

    if rect2.top<=25 and rect2.left<=25:
        rect2.top=0
        rect2.left=0
        rect2_finish = True

    if rect3.top<=25 and rect3.left>=175 and rect3.left<=225:
        rect3.top=0
        rect3.left=200
        rect3_finish = True

    if rect4.top>=175 and rect4.top<=225 and rect4.left<=25:
        rect4.top=200
        rect4.left=0
        rect4_finish = True

    if rect1_finish == True and rect2_finish == True and rect3_finish == True and rect4_finish == True:
        end()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                print("Thank you for using my puzzle program! I hoped you enjoyed it.")
                pygame.quit()
                exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if rect1.collidepoint(event.pos):
                    rect1_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rect1.x - mouse_x
                    offset_y = rect1.y - mouse_y
                elif rect2.collidepoint(event.pos):
                    rect2_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rect2.x - mouse_x
                    offset_y = rect2.y - mouse_y
                elif rect3.collidepoint(event.pos):
                    rect3_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rect3.x - mouse_x
                    offset_y = rect3.y - mouse_y
                elif rect4.collidepoint(event.pos):
                    rect4_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rect4.x - mouse_x
                    offset_y = rect4.y - mouse_y    
   

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                rect1_draging = False
                rect2_draging = False
                rect3_draging = False
                rect4_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if rect1_draging:
                if rect1_finish == False:
                    mouse_x, mouse_y = event.pos
                    rect1.x = mouse_x + offset_x
                    rect1.y = mouse_y + offset_y
            if rect2_draging:
                if rect2_finish == False:
                    mouse_x, mouse_y = event.pos
                    rect2.x = mouse_x + offset_x
                    rect2.y = mouse_y + offset_y
            if rect3_draging:
                if rect3_finish == False:
                    mouse_x, mouse_y = event.pos
                    rect3.x = mouse_x + offset_x
                    rect3.y = mouse_y + offset_y
            if rect4_draging:
                if rect4_finish == False:
                    mouse_x, mouse_y = event.pos
                    rect4.x = mouse_x + offset_x
                    rect4.y = mouse_y + offset_y        
    

    win.blit(img1, rect1)
    win.blit(img2, rect2)
    win.blit(img3, rect3)
    win.blit(img4, rect4)
    
    pygame.display.update()
