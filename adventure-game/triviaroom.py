import pygame
import config
import procedures
import time
import random
import sys

def question_reset(): # Reset question lists
    config.question_list = ['What is the capital city of Bhutan?','What is the longest river in the world?','In what year did the RMS Titanic sink?','Which British mathematician helped to crack the Enigma code?',
                     'Which famous footballer started a campaign to end child food poverty?','Which author wrote the novel War and Peace?','What are the names of the two opposing families in Romeo and Juliet?',
                     'Which pop musician wrote the theme for the 2021 film No Time To Die?',"Which 2021 Netflix drama is about people playing children's games?",
                     'Which BBC series is based on a detective series by Arthur Conan Doyle?','What is the capital city of Poland?','In which year did World War Two start?',
                     'Which 19th century German philosopher was an advocate for Communism?','Which British monarch ascended the throne in 1910?','Which sport takes place in a velodrome?']
    config.answer_a = ['New Delhi','The Nile','1812','John von Neumann','Raheem Sterling','Fyodor Dostoevsky','The Montagues and the Capulets','Billie Eilish','Crab Game','Murder, She Wrote','Copenhagen','1939','Immanuel Kant','George VI',
                'Running']
    config.answer_b = ['Thimpu','The Amazon','1914','Blaise Pascal','Cristiano Ronaldo','Leo Tolstoy','The Jets and the Sharks','Justin Bieber',"The Queen's Gambit",'NCIS','Warsaw','1938','Karl Marx','Edward VII','Skiing']
    config.answer_c = ['Kathmandu','The Yangtze','1912','Stephen Hawking','Marcus Rashford','Jane Austen','The Medici and the Albizzi','Ariana Grande','Squid Game','Poirot','Brussels','1941','Sigmund Freud','Victoria I','Cycling']
    config.answer_d = ['Dhaka','The Thames','1910','Alan Turing','Lionel Messi','William Shakespeare','The Bloods and the Crips','Harry Styles','Bridgerton','Sherlock','Amsterdam','1945','Adolf Hitler','George V','Horse-riding']
    config.correct_answer = ['b','a','c','d','c','b','a','a','c','d','b','a','b','d','c']

def question_blit(): # Blit questions on screen
    question_text = config.triviafont.render((config.question_list[config.question_random]), True, (config.white))
    a_text = config.triviafont.render(('A: '+(config.answer_a[config.question_random])), True, (config.white))
    b_text = config.triviafont.render(('B: '+(config.answer_b[config.question_random])), True, (config.white))
    c_text = config.triviafont.render(('C: '+(config.answer_c[config.question_random])), True, (config.white))
    d_text = config.triviafont.render(('D: '+(config.answer_d[config.question_random])), True, (config.white))
    config.screen.blit(question_text, (60,220))
    config.screen.blit(a_text, (60,265))
    config.screen.blit(b_text, (60,300))
    config.screen.blit(c_text, (60,335))
    config.screen.blit(d_text, (60,370))
    config.screen.blit(config.a_image, config.a_rect)
    config.screen.blit(config.b_image, config.b_rect)
    config.screen.blit(config.c_image, config.c_rect)
    config.screen.blit(config.d_image, config.d_rect)

def correct(): # What to do if answer is correct
    config.screen.blit(config.green_tick, (680,600))
    pygame.display.update()
    time.sleep(0.5)
    config.question_number += 1
    config.question_list.pop(config.question_random)
    config.answer_a.pop(config.question_random)
    config.answer_b.pop(config.question_random)
    config.answer_c.pop(config.question_random)
    config.answer_d.pop(config.question_random)
    config.correct_answer.pop(config.question_random)
    if len(config.question_list) == 0:
        question_reset()
    config.question_random = random.randint(0,(len(config.question_list)-1))

def wrong(): # What to do if answer is wrong
    config.screen.blit(config.red_cross, (680,600))
    pygame.display.update()
    time.sleep(0.5)
    if config.question_number > 0:
        config.question_number -= 1
    config.question_list.pop(config.question_random)
    config.answer_a.pop(config.question_random)
    config.answer_b.pop(config.question_random)
    config.answer_c.pop(config.question_random)
    config.answer_d.pop(config.question_random)
    config.correct_answer.pop(config.question_random)
    if len(config.question_list) == 0:
        question_reset()
    config.question_random = random.randint(0,(len(config.question_list)-1))

def answer(): # Check if correct answer clicked
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if config.a_rect.collidepoint(event.pos) and config.correct_answer[config.question_random] == 'a': # Correct answers
                    correct()
                elif config.b_rect.collidepoint(event.pos) and config.correct_answer[config.question_random] == 'b':
                    correct()
                elif config.c_rect.collidepoint(event.pos) and config.correct_answer[config.question_random] == 'c':
                    correct()
                elif config.d_rect.collidepoint(event.pos) and config.correct_answer[config.question_random] == 'd':
                    correct()

                elif config.a_rect.collidepoint(event.pos) and config.correct_answer[config.question_random] != 'a': # Wrong answers
                    wrong()
                elif config.b_rect.collidepoint(event.pos) and config.correct_answer[config.question_random] != 'b':
                    wrong()
                elif config.c_rect.collidepoint(event.pos) and config.correct_answer[config.question_random] != 'c':
                    wrong()
                elif config.d_rect.collidepoint(event.pos) and config.correct_answer[config.question_random] != 'd':
                    wrong()

        if event.type == pygame.QUIT:
            config.running = False
            pygame.quit()
            sys.exit()
            exit()

def correct_questions(): # Fill up question bar
    if config.question_number > 0:
        config.screen.blit(config.bar1, (25, 538))
    if config.question_number > 1:
        config.screen.blit(config.bar2, (94, 538))
    if config.question_number > 2:
        config.screen.blit(config.bar3, (163, 538))
    if config.question_number > 3:
        config.screen.blit(config.bar4, (231, 538))
    if config.question_number > 4:
        config.screen.blit(config.bar5, (300, 538))
    if config.question_number > 5:
        config.screen.blit(config.bar6, (369, 538))
    if config.question_number > 6:
        config.screen.blit(config.bar7, (438, 538))
    if config.question_number > 7:
        config.screen.blit(config.bar8, (506, 538))
    if config.question_number > 8:
        config.screen.blit(config.bar9, (575, 538))
    if config.question_number > 9:
        config.screen.blit(config.bar10, (644, 538))
    if config.question_number > 10:
        config.screen.blit(config.bar11, (713, 538))
        pygame.display.update()
        time.sleep(2)
        config.trivia_room_loop = False
        config.instruction_loop = True
        config.instructionvar = 47
        config.altar_cross.inv = True
        procedures.altar_count()

def trivia_room_update(): # Update room
    config.screen.fill(config.black)
    config.screen.blit(config.b_trivia_room,(0, 0))
    config.sprite_list.draw(config.screen)
    config.sprite_list.update()
    config.screen.blit(config.doorfront, config.door12_rect)
    correct_questions()
    question_blit()
    answer()
    pygame.display.update()

def trivia_room():
    procedures.player_move()
    trivia_room_update()
