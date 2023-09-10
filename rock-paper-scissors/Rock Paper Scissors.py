import pygame
import thorpy
import sys
import threading
import pyganim
import random
import math

pygame.init()
screen = pygame.display.set_mode((900,700))
pygame.display.set_caption('Rock Paper Scissors')
player_choice = ''
score1var = 0
score2var = 0
game = False
running = True
roundnum = 0
can_choose = False
winner = ''
blue_fighter_choice = 0
fight_anim_type = 0 #1rr,2pp,3ss,4rp,5rs,6ps
choose_anim = ''
sprite1 = ''
sprite2 = ''
sprite1type = ''
sprite2type = ''
initanim = False
x1 = 350
y1 = 400
x2 = 500
y2 = 250
animnum = 0
secondanim = False
toggle_red = False
rp_anim = ''
rs_anim = ''
ps_anim = ''
blocker_var = True

rock = pygame.image.load("rock.png").convert()
rock.set_colorkey((255,0,0))
rock = pygame.transform.scale(rock, (200,200))
paper = pygame.image.load("paper.png").convert()
paper.set_colorkey((255,0,0))
paper = pygame.transform.scale(paper, (200,200))
scissors = pygame.image.load("scissors.png").convert()
scissors.set_colorkey((255,0,0))
scissors = pygame.transform.scale(scissors, (200,200))
question_mark = pygame.image.load("question_mark.png").convert_alpha()
question_mark = pygame.transform.scale(question_mark, (200,200))
white = pygame.image.load("white.png").convert_alpha()
white = pygame.transform.scale(white, (200,200))

smallrock = pygame.image.load("rock.png").convert()
smallrock.set_colorkey((255,0,0))
smallrock = pygame.transform.scale(rock, (50,50))
smallpaper = pygame.image.load("paper.png").convert()
smallpaper.set_colorkey((255,0,0))
smallpaper = pygame.transform.scale(paper, (50,50))
smallscissors = pygame.image.load("scissors.png").convert()
smallscissors.set_colorkey((255,0,0))
smallscissors = pygame.transform.scale(scissors, (50,50))

smallrockred = pygame.image.load("rock.png").convert()
smallrockred.set_colorkey((255,0,0))
smallrockred = pygame.transform.scale(rock, (50,50))
smallrockred.fill((190, 0, 0, 200), special_flags=pygame.BLEND_ADD)
smallpaperred = pygame.image.load("paper.png").convert()
smallpaperred.set_colorkey((255,0,0))
smallpaperred = pygame.transform.scale(paper, (50,50))
smallpaperred.fill((190, 0, 0, 200), special_flags=pygame.BLEND_ADD)
smallscissorsred = pygame.image.load("scissors.png").convert()
smallscissorsred.set_colorkey((255,0,0))
smallscissorsred = pygame.transform.scale(scissors, (50,50))
smallscissorsred.fill((190, 0, 0, 200), special_flags=pygame.BLEND_ADD)

rp2 = pygame.image.load("rp-2.png").convert()
rp2.set_colorkey((255,0,0))
rp2 = pygame.transform.scale(rp2, (50,50))
rp3 = pygame.image.load("rp-3.png").convert()
rp3.set_colorkey((255,0,0))
rp3 = pygame.transform.scale(rp3, (50,50))
rp4 = pygame.image.load("rp-4.png").convert()
rp4.set_colorkey((255,0,0))
rp4 = pygame.transform.scale(rp4, (50,50))
rp5 = pygame.image.load("rp-5.png").convert()
rp5.set_colorkey((255,0,0))
rp5 = pygame.transform.scale(rp5, (50,50))
rp6 = pygame.image.load("rp-6.png").convert()
rp6.set_colorkey((255,0,0))
rp6 = pygame.transform.scale(rp6, (50,50))

rs1 = pygame.image.load("rs-1.png").convert()
rs1.set_colorkey((255,0,24))
rs1 = pygame.transform.scale(rs1, (50,100))
rs2 = pygame.image.load("rs-2.png").convert()
rs2.set_colorkey((255,0,24))
rs2 = pygame.transform.scale(rs2, (50,100))
rs3 = pygame.image.load("rs-3.png").convert()
rs3.set_colorkey((255,0,24))
rs3 = pygame.transform.scale(rs3, (50,100))
rs4 = pygame.image.load("rs-4.png").convert()
rs4.set_colorkey((255,0,24))
rs4 = pygame.transform.scale(rs4, (50,100))
rs5 = pygame.image.load("rs-5.png").convert()
rs5.set_colorkey((255,0,24))
rs5 = pygame.transform.scale(rs5, (50,100))
rs6 = pygame.image.load("rs-6.png").convert()
rs6.set_colorkey((255,0,24))
rs6 = pygame.transform.scale(rs6, (50,100))
rs7 = pygame.image.load("rs-7.png").convert()
rs7.set_colorkey((255,0,24))
rs7 = pygame.transform.scale(rs7, (50,100))
rs8 = pygame.image.load("rs-8.png").convert()
rs8.set_colorkey((255,0,24))
rs8 = pygame.transform.scale(rs8, (50,100))
rs9 = pygame.image.load("rs-9.png").convert()
rs9.set_colorkey((255,0,24))
rs9 = pygame.transform.scale(rs9, (50,100))
rs10 = pygame.image.load("rs-10.png").convert()
rs10.set_colorkey((255,0,24))
rs10 = pygame.transform.scale(rs10, (50,100))
rs11 = pygame.image.load("rs-11.png").convert()
rs11.set_colorkey((255,0,24))
rs11 = pygame.transform.scale(rs11, (50,100))
rs12 = pygame.image.load("rs-12.png").convert()
rs12.set_colorkey((255,0,24))
rs12 = pygame.transform.scale(rs12, (50,100))
rs13 = pygame.image.load("rs-13.png").convert()
rs13.set_colorkey((255,0,24))
rs13 = pygame.transform.scale(rs13, (50,100))
rs14 = pygame.image.load("rs-14.png").convert()
rs14.set_colorkey((255,0,24))
rs14 = pygame.transform.scale(rs14, (50,100))
rs15 = pygame.image.load("rs-15.png").convert()
rs15.set_colorkey((255,0,24))
rs15 = pygame.transform.scale(rs15, (50,100))

ps1 = pygame.image.load("ps-1.png").convert()
ps1.set_colorkey((255,0,24))
ps1 = pygame.transform.scale(ps1, (75,50))
ps2 = pygame.image.load("ps-2.png").convert()
ps2.set_colorkey((255,0,24))
ps2 = pygame.transform.scale(ps2, (75,50))
ps3 = pygame.image.load("ps-3.png").convert()
ps3.set_colorkey((255,0,24))
ps3 = pygame.transform.scale(ps3, (75,50))
ps4 = pygame.image.load("ps-4.png").convert()
ps4.set_colorkey((255,0,24))
ps4 = pygame.transform.scale(ps4, (75,50))
ps5 = pygame.image.load("ps-5.png").convert()
ps5.set_colorkey((255,0,24))
ps5 = pygame.transform.scale(ps5, (75,50))
ps6 = pygame.image.load("ps-6.png").convert()
ps6.set_colorkey((255,0,24))
ps6 = pygame.transform.scale(ps6, (75,50))
ps7 = pygame.image.load("ps-7.png").convert()
ps7.set_colorkey((255,0,24))
ps7 = pygame.transform.scale(ps7, (75,50))
ps8 = pygame.image.load("ps-8.png").convert()
ps8.set_colorkey((255,0,24))
ps8 = pygame.transform.scale(ps8, (75,50))
ps9 = pygame.image.load("ps-9.png").convert()
ps9.set_colorkey((255,0,24))
ps9 = pygame.transform.scale(ps9, (75,50))
ps10 = pygame.image.load("ps-10.png").convert()
ps10.set_colorkey((255,0,24))
ps10 = pygame.transform.scale(ps10, (75,50))
ps11 = pygame.image.load("ps-11.png").convert()
ps11.set_colorkey((255,0,24))
ps11 = pygame.transform.scale(ps11, (75,50))

red_fighter = white
blue_fighter = white

def get_pil_text_size(text, font_size, font_name):
    font = ImageFont.truetype(font_name, font_size)
    size = font.getlength(text)
    return size

def quit_app():
    global running
    running = False
    pygame.quit()
    sys.exit()
    quit()
    exit()

def next_round():
    global roundnum
    global red_fighter
    global blue_fighter
    global blocker_var
    blocker_var = False
    roundnum += 1
    text.set_text('ROUND '+str(roundnum))
    text.update()
    text.unblit_and_reblit()
    blue_fighter = question_mark
    red_fighter = question_mark
    startround = threading.Timer(2, start_fight)
    startround.start()

def start_fight():
    global player_choice
    global can_choose
    text.set_text('Pick your fighter:')
    text.update()
    text.unblit_and_reblit()
    can_choose = True

def reset():
    global blocker_var
    global x1
    global y1
    global x2
    global y2
    global score1var
    global score2var
    global red_fighter
    global blue_fighter
    blocker_var = True
    x1 = 350
    y1 = 400
    x2 = 500
    y2 = 250
    score1var = 0
    score1.set_text(str(score1var))
    score1.update()
    score2var = 0
    score2.set_text(str(score2var))
    score2.update()
    text.set_text("Press 'New Game' to start.")
    red_fighter = white
    blue_fighter = white

def end_game():
    global game
    global blocker_var
    global score1var
    global score2var
    if game == False:
        end_game_button.set_text("End Game")
        end_game_button.update()
        end_game_button.unblit_and_reblit()
        game = True
        blocker_var = False
        next_round()
    elif game == True:
        end_game_button.set_text("New Game")
        end_game_button.update()
        end_game_button.unblit_and_reblit()
        blocker_var = False
        threading.Timer(2, reset).start()
        if score1var == score2var:
            text.set_text("The game has resulted in a draw!")
        elif score1var > score2var:
            text.set_text("You are the ultimate winner!")
        elif score1var < score2var:
            text.set_text("The computer is the ultimate winner!")
        game = False

def re_init():
    global blocker_var
    global x1
    global y1
    global x2
    global y2
    global sprite1type
    global sprite2type
    global red_fighter
    global blue_fighter
    blocker_var = True
    x1 = 350
    y1 = 400
    x2 = 500
    y2 = 250
    text.set_text("Press 'Next Round' or 'End Game'")
    sprite1type = ''
    sprite2type = ''
    red_fighter = white
    blue_fighter = white

def announce_winner():
    global winner
    global score1var
    global score2var
    if winner == 'Computer':
        text.set_text('The computer wins!')
        score2var += 1
        score2.set_text(str(score2var))
        score2.update()
    elif winner == 'Player':
        text.set_text('You win!')
        score1var += 1
        score1.set_text(str(score1var))
        score1.update()
    threading.Timer(1, re_init).start()

def second_anim():
    global sprite1
    global sprite2
    global animnum
    global secondanim
    global toggle_red
    global sprite1type
    global sprite2type
    global fight_anim_type
    global rs_anim
    global rp_anim
    global ps_anim
    if secondanim == True:
        if fight_anim_type < 4:
            threading.Timer(0.2, second_anim).start()
            animnum += 1
            if fight_anim_type == 1:
                if toggle_red == False:
                    sprite1type = smallrockred
                    sprite2type = smallrock
                    toggle_red = True   
                elif toggle_red == True:
                    sprite2type = smallrockred
                    sprite1type = smallrock
                    toggle_red = False
                if animnum == 7:
                    sprite1type = smallrock
                    sprite2type = smallrock
                    secondanim = False
                    text.set_text('The result is a draw.')
                    threading.Timer(1, re_init).start()
                    
            elif fight_anim_type == 2:
                if toggle_red == False:
                    sprite1type = smallpaperred
                    sprite2type = smallpaper
                    toggle_red = True   
                elif toggle_red == True:
                    sprite2type = smallpaperred
                    sprite1type = smallpaper
                    toggle_red = False
                if animnum == 7:
                    sprite1type = smallpaper
                    sprite2type = smallpaper
                    secondanim = False
                    text.set_text('The result is a draw.')
                    threading.Timer(1, re_init).start()
                    
            elif fight_anim_type == 3:
                if toggle_red == False:
                    sprite1type = smallscissorsred
                    sprite2type = smallscissors
                    toggle_red = True   
                elif toggle_red == True:
                    sprite2type = smallscissorsred
                    sprite1type = smallscissors
                    toggle_red = False
                if animnum == 7:
                    sprite1type = smallscissors
                    sprite2type = smallscissors
                    secondanim = False
                    text.set_text('The result is a draw.')
                    threading.Timer(1, re_init).start()

        elif fight_anim_type > 3:
            sprite1type = ''
            sprite2type = ''
            if fight_anim_type == 4:
                threading.Timer(2, announce_winner).start()
                rp_anim = pyganim.PygAnimation([(smallpaper, 300),
                                            (rp2, 300),
                                            (rp3, 300),
                                            (rp4, 300),
                                            (rp5, 300),
                                            (rp6, 1000)])
                rp_anim.play()
                rp_anim.loop = False

            elif fight_anim_type == 5:
                threading.Timer(2, announce_winner).start()
                rs_anim = pyganim.PygAnimation([(rs1, 100),
                                            (rs2, 100),
                                            (rs3, 100),
                                            (rs4, 100),
                                            (rs5, 100),
                                            (rs6, 100),
                                            (rs7, 100),
                                            (rs8, 100),
                                            (rs9, 100),
                                            (rs10, 100),
                                            (rs11, 100),
                                            (rs12, 100),
                                            (rs13, 100),
                                            (rs14, 100),
                                            (rs15, 1000)])
                rs_anim.play()
                rs_anim.loop = False

            elif fight_anim_type == 6:
                threading.Timer(2, announce_winner).start()
                ps_anim = pyganim.PygAnimation([(ps1, 150),
                                            (ps2, 150),
                                            (ps3, 150),
                                            (ps4, 150),
                                            (ps5, 150),
                                            (ps6, 150),
                                            (ps7, 150),
                                            (ps8, 150),
                                            (ps9, 150),
                                            (ps10, 150),
                                            (ps11, 1000)])
                ps_anim.play()
                ps_anim.loop = False

def initial_anim():
    global sprite1
    global sprite2
    global initanim
    global x1
    global y1
    global x2
    global y2
    global animnum
    global secondanim
    if initanim == True:
        threading.Timer(0.1, initial_anim).start()
        sprite1 = pygame.Rect(x1,y1,50,50)
        sprite2 = pygame.Rect(x2,y2,50,50)
        x1 += ((math.cos(7*math.pi/4))*2)
        y1 += ((math.sin(7*math.pi/4))*2)
        x2 += ((math.cos(3*math.pi/4))*2)
        y2 += ((math.sin(3*math.pi/4))*2)
        animnum +=1
        if animnum == 50:
            initanim = False
            secondanim = True
            second_anim()
            animnum = 0
        
def fight_anim():
    global fight_anim_type
    global sprite1
    global sprite2
    global sprite1type
    global sprite2type
    global initanim
    global player_choice
    sprite1 = smallrock.get_rect()
    sprite2 = smallrock.get_rect()
    if fight_anim_type == 1:        
        sprite1type = smallrock        
        sprite2type = smallrock
    if fight_anim_type == 2:        
        sprite1type = smallpaper       
        sprite2type = smallpaper
    if fight_anim_type == 3:        
        sprite1type = smallscissors       
        sprite2type = smallscissors
    if fight_anim_type == 4:
        if player_choice == 'rock':
            sprite1type = smallrock        
            sprite2type = smallpaper
        elif player_choice == 'paper':
            sprite2type = smallrock        
            sprite1type = smallpaper
    if fight_anim_type == 5:        
        if player_choice == 'rock':
            sprite1type = smallrock        
            sprite2type = smallscissors
        elif player_choice == 'scissors':
            sprite2type = smallrock        
            sprite1type = smallscissors
    if fight_anim_type == 6:        
        if player_choice == 'paper':
            sprite1type = smallpaper        
            sprite2type = smallscissors
        elif player_choice == 'scissors':
            sprite2type = smallpaper        
            sprite1type = smallscissors
    initanim = True
    initial_anim()

def fight():
    global blue_fighter
    global blue_fighter_choice
    global player_choice
    global winner
    global fight_anim_type
    text.set_text('Let the battle commence!')
    
    if blue_fighter_choice == 1:
        blue_fighter = rock
        if player_choice == 'rock':
            winner = 'draw'
            fight_anim_type = 1
        elif player_choice == 'paper':
            winner = 'Player'
            fight_anim_type = 4
        elif player_choice == 'scissors':
            winner = 'Computer'
            fight_anim_type = 5
            
    elif blue_fighter_choice == 2:
        blue_fighter = paper
        if player_choice == 'rock':
            winner = 'Computer'
            fight_anim_type = 4
        elif player_choice == 'paper':
            winner = 'draw'
            fight_anim_type = 2
        elif player_choice == 'scissors':
            winner = 'Player'
            fight_anim_type = 6
            
    elif blue_fighter_choice == 3:
        blue_fighter = scissors
        if player_choice == 'rock':
            winner = 'Player'
            fight_anim_type = 5
        elif player_choice == 'paper':
            winner = 'Computer'
            fight_anim_type = 6
        elif player_choice == 'scissors':
            winner = 'draw'
            fight_anim_type = 3

    fight_anim()

def computer_choose():
    global blue_fighter_choice
    global choose_anim
    global blue_fighter
    text.set_text("Computer choosing")
    startfight = threading.Timer(2, fight)
    startfight.start()

    blue_fighter_choice = random.randint(1,3)
    blue_fighter = white

    if blue_fighter_choice == 1:    
        choose_anim = pyganim.PygAnimation([(rock, 100),
                                            (paper, 100),
                                            (scissors, 100),
                                            (rock, 100),
                                            (paper, 100),
                                            (scissors, 100),
                                            (rock, 100),
                                            (paper, 100),
                                            (scissors, 100),
                                            (rock, 200),
                                            (paper, 300),
                                            (scissors, 400),
                                            (rock, 100)])
    elif blue_fighter_choice == 2:    
        choose_anim = pyganim.PygAnimation([(rock, 100),
                                            (paper, 100),
                                            (scissors, 100),
                                            (rock, 100),
                                            (paper, 100),
                                            (scissors, 100),
                                            (rock, 100),
                                            (paper, 100),
                                            (scissors, 100),
                                            (rock, 100),
                                            (paper, 200),
                                            (scissors, 300),
                                            (rock, 400),
                                            (paper, 100)])
    elif blue_fighter_choice == 3:    
        choose_anim = pyganim.PygAnimation([(rock, 100),
                                            (paper, 100),
                                            (scissors, 100),
                                            (rock, 100),
                                            (paper, 100),
                                            (scissors, 100),
                                            (rock, 100),
                                            (paper, 100),
                                            (scissors, 100),
                                            (rock, 100),
                                            (paper, 100),
                                            (scissors, 200),
                                            (rock, 300),
                                            (paper, 400),
                                            (scissors, 100)])
    choose_anim.play()
    choose_anim.loop = False

def choose(choice):
    global player_choice
    global red_fighter
    global can_choose
    player_choice = str(choice)
    if can_choose == True:
        if player_choice == 'rock':
            red_fighter = rock
            can_choose = False
            computer_choose()
        elif player_choice == 'paper':
            red_fighter = paper
            can_choose = False
            computer_choose()
        elif player_choice == 'scissors':
            red_fighter = scissors
            can_choose = False
            computer_choose()

painter1 = thorpy.painters.basicframe.BasicFrame(size=(150,150),color=(0,0,0))
painter2 = thorpy.painters.basicframe.BasicFrame(size=(500,25),color=(255,255,255))

player1 = thorpy.Element("Player")
player1.set_topleft((75, 25))
player1.set_size((200,50))
player1.set_main_color((207, 18, 0))

player2 = thorpy.Element("Computer")
player2.set_topleft((625, 25))
player2.set_size((200,50))
player2.set_main_color((0, 18, 207))
player2.set_font_color((255,255,255))

next_round_button = thorpy.make_button("Next Round", next_round)
next_round_button.set_main_color((241,243,244))
next_round_button.finish()

end_game_button = thorpy.make_button("New Game", end_game)
end_game_button.set_main_color((241,243,244))
end_game_button.finish()

close_button = thorpy.make_button("Close Game", quit_app)    
close_button.set_main_color((241,243,244))
close_button.finish()

ring = thorpy.Image(path="ring.jpg")
ring.center()
ring.set_topleft((None,180))

text = thorpy.Element("Press 'New Game' to start.")
text.set_painter(painter2)
text.finish()
text.set_font_size(22)
text.center()
text.set_topleft((None,525))

rock_button = thorpy.make_image_button("rock.png",colorkey=(255,0,0))
rock_button.set_topleft((275,575))

paper_button = thorpy.make_image_button("paper.png",colorkey=(255,0,0))
paper_button.set_topleft((400,575))

scissors_button = thorpy.make_image_button("scissors.png",colorkey=(255,0,0))
scissors_button.set_topleft((525,575))

score1 = thorpy.Element(str(score1var))
score1.set_painter(painter1)
score1.finish()
score1.set_font("Calibri")
score1.set_font_size(150)
score1.set_topleft((150,100))
score1.set_center((175,None))
score1.set_font_color((222, 215, 4))

score2 = thorpy.Element(str(score2var))
score2.set_painter(painter1)
score2.finish()
score2.set_font("Calibri")
score2.set_font_size(150)
score2.set_topleft((700,100))
score2.set_center((725,None))
score2.set_font_color((222, 215, 4))

elements = [end_game_button,next_round_button,close_button]

for i in range(len(elements)):
    elements[i]._make_size((150,30))

blocker = thorpy.Element("Access the menu when the round is finished.")
blocker.set_size((210,150))
blocker.center()
blocker.set_topleft((None,25))

central_box = thorpy.Box(elements=elements)
central_box.fit_children(margins=(30,30))
central_box.center()
central_box.set_topleft((None,25))
central_box.set_main_color((220,220,220,180))

element_list = [central_box, player1, player2, ring, text, rock_button, paper_button, scissors_button, score1, score2, blocker]

background = thorpy.Background(color=(255,255,255),elements=element_list)

reaction1 = thorpy.ConstantReaction(reacts_to=thorpy.constants.THORPY_EVENT,reac_func=choose,params={"choice":"rock"},
                                    event_args={"id":thorpy.constants.EVENT_PRESS,"el":rock_button})
reaction2 = thorpy.ConstantReaction(reacts_to=thorpy.constants.THORPY_EVENT,reac_func=choose,params={"choice":"paper"},
                                    event_args={"id":thorpy.constants.EVENT_PRESS,"el":paper_button})
reaction3 = thorpy.ConstantReaction(reacts_to=thorpy.constants.THORPY_EVENT,reac_func=choose,params={"choice":"scissors"},
                                    event_args={"id":thorpy.constants.EVENT_PRESS,"el":scissors_button})

background.add_reaction(reaction1)
background.add_reaction(reaction2)
background.add_reaction(reaction3)

menu = thorpy.Menu(background)

screen.fill((255,255,255))

def blit_all():
    for element in menu.get_population():
        element.surface = screen
        element.blit()

blit_all()
blocker.unblit()
pygame.display.update()

while running == True:
    screen.fill((255,255,255))
    blit_all()
    if blocker_var == True:
        blocker.unblit()
        next_round_button.blit()
        end_game_button.blit()
        close_button.blit()
    elif blocker_var == False:
        blocker.blit()
        next_round_button.unblit()
        end_game_button.unblit()
        close_button.unblit()
    screen.blit(red_fighter,(75,300))
    screen.blit(blue_fighter,(625,300))
    if choose_anim != '':
        choose_anim.blit(screen,(625,300))
    if rp_anim != '':
        rp_anim.blit(screen,(410,340))
    if rs_anim != '':
        rs_anim.blit(screen,(410,290))
    if ps_anim != '':
        ps_anim.blit(screen,(390,340))
    if sprite1type != '' and sprite2type != '':
        screen.blit(sprite1type, sprite1)
        screen.blit(sprite2type, sprite2)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            quit()
            exit()
        menu.react(event)
        pygame.display.update()

pygame.quit()
sys.exit()
quit()
exit()

