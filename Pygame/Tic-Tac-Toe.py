#imports
import pygame
from pygame.locals import *
pygame.init()
import time

#colors
white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))
marroon = ((115,0,0))
lime = ((180,255,100))
pink = ((255,100,180))
purple = ((240,0,255))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
rust = ((210,150,75))
dandilion_yellow = ((255,200,0))
highlighter = ((255,255,100))
sky_blue = ((0,255,255))
light_gray = ((200,200,200))
dark_gray = ((50,50,50))
tan = ((230,220,170))
coffee_brown =((200,190,140))
moon_glow = ((235,245,255))

#variables
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tic-Tac-Toe!")
    
def game():
    #variables
    width = 200
    height = 200
    turn = "cross"
    square = None
    dicty = {1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:""}
    winner = None
    
    #functions
    def draw(a, b, x, y, turn, dicty, square):
        if (x <= a <= x + width) and (y <= b <= y + height):
            if turn == "cross":
                if dicty[square] == "":
                    pygame.draw.line(screen, red, (x, y), (x + width, y + height), 2)
                    pygame.draw.line(screen, red, (x + width, y), (x, y + height), 2)
                    dicty[square] = "cross"
                    turn = "circ"
            return(turn)
    
    def drawy(a, b, x, y, turn, dicty, square):
        if (x <= a <= x + width) and (y <= b <= y + height):
            if turn == "circ":
                if dicty[square] == "":
                    pygame.draw.circle(screen, blue, (x + 100, y + 100), 99, 1)
                    dicty[square] = "circ"
                    turn = "cross"
            return(turn)
                    
    def text_one(msg_one, x_one, y_one):
        fontobj_one = pygame.font.SysFont("freesans",32)
        msgobj_one = fontobj_one.render(msg_one, False,red)
        screen.blit(msgobj_one,(x_one,y_one))
    
    def win(turn, dicty, square, winner, text_one):
        if turn == "cross":
            if dicty[1] == dicty[2] == dicty[3]:
                if dicty[1] != "":
                    winner = "cross"
            if dicty[4] == dicty[5] == dicty[6]:
                if dicty[4] != "":
                    winner = "cross"
            if dicty[7] == dicty[8] == dicty[9]:
                if dicty[7] != "":
                    winner = "cross"
            if dicty[1] == dicty[4] == dicty[7]:
                if dicty[1] != "":
                    winner = "cross"
            if dicty[2] == dicty[5] == dicty[8]:
                if dicty[2] != "":
                    winner = "cross"
            if dicty[3] == dicty[6] == dicty[9]:
                if dicty[3] != "":
                    winner = "cross"
            if dicty[1] == dicty[5] == dicty[9]:
                if dicty[1] != "":
                    winner = "cross"
            if dicty[3] == dicty[5] == dicty[7]:
                if dicty[3] != "":
                    winner = "cross"
        elif turn == "circ":
            if dicty[1] == dicty[2] == dicty[3]:
                if dicty[1] != "":
                    winner = "circ"
            if dicty[4] == dicty[5] == dicty[6]:
                if dicty[4] != "":
                    winner = "circ"
            if dicty[7] == dicty[8] == dicty[9]:
                if dicty[7] != "":
                    winner = "circ"
            if dicty[1] == dicty[4] == dicty[7]:
                if dicty[1] != "":
                    winner = "circ"
            if dicty[2] == dicty[5] == dicty[8]:
                if dicty[2] != "":
                    winner = "circ"
            if dicty[3] == dicty[6] == dicty[9]:
                if dicty[3] != "":
                    winner = "circ"
            if dicty[1] == dicty[5] == dicty[9]:
                if dicty[1] != "":
                    winner = "circ"
            if dicty[3] == dicty[5] == dicty[7]:
                if dicty[3] != "":
                    winner = "circ"     
        if (dicty[1] != "") and (dicty[2] != "") and (dicty[3] != "") and (dicty[4] != "") and (dicty[5] != "") and (dicty[6] != "") and (dicty[7] != "") and (dicty[8] != "") and (dicty[9] != ""):
            winner = "tie"
            
        if winner == "cross":
            time.sleep(0.5)
            screen.fill(black)
            text_one("Circle wins!", 100, 100)
            time.sleep(2)
            menu(text_two, text_three)
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    l, m = pygame.mouse.get_pos()
                    if (0 <= l <= 300) and (0 <= m <= 300):
                        print("Play")
                        screen.fill(black)
                        game()
                        menu(text_two, text_three)
                    elif (300 < l <= 600) and (0 < m <= 300):
                        print("Quit")
                        pygame.quit()
                        exit()
        elif winner == "circ":
            time.sleep(0.5)
            screen.fill(black)
            text_one("X wins!", 100, 100)
            time.sleep(2)
            menu(text_two, text_three)
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    l, m = pygame.mouse.get_pos()
                    if (0 <= l <= 300) and (0 <= m <= 300):
                        print("Play")
                        screen.fill(black)
                        game()
                        menu(text_two, text_three)
                    elif (300 < l <= 600) and (0 < m <= 300):
                        print("Quit")
                        pygame.quit()
                        exit()            
        elif winner == "tie":
            time.sleep(0.5)
            screen.fill(black)
            text_one("It's a tie!", 100, 100)
            time.sleep(2)
            menu(text_two, text_three)
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    l, m = pygame.mouse.get_pos()
                    if (0 <= l <= 300) and (0 <= m <= 300):
                        print("Play")
                        screen.fill(black)
                        game()
                        menu(text_two, text_three)
                    elif (300 < l <= 600) and (0 < m <= 300):
                        print("Quit")
                        pygame.quit()
                        exit()
            
    #grid
    pygame.draw.line(screen, purple, (200, 0), (200, 600), 1)
    pygame.draw.line(screen, purple, (400, 0), (400, 600), 1)
    pygame.draw.line(screen, purple, (0, 200), (600, 200), 1)
    pygame.draw.line(screen, purple, (0, 400), (600, 400), 1)
    
    while True:
        
        #quit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        
            #drawing
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                a, b = pygame.mouse.get_pos()
                if (0 <= a < 200) and (0 <= b <= 200):
                    x = 0
                    y = 0
                    square = 1
                if (200 <= a < 400) and (0 <= b <= 200):
                    x = 200
                    y = 0
                    square = 2
                if (400 <= a < 600) and (0 <= b <= 200):
                    x = 400
                    y = 0
                    square = 3
                if (0 <= a < 200) and (200 <= b <= 400):
                    x = 0
                    y = 200
                    square = 4
                if (200 <= a < 400) and (200 <= b <= 400):
                    x = 200
                    y = 200
                    square = 5
                if (400 <= a < 600) and (200 <= b <= 400):
                    x = 400
                    y = 200
                    square = 6
                if (0 <= a < 200) and (400 <= b <= 600):
                    x = 0
                    y = 400
                    square = 7
                if (200 <= a < 400) and (400 <= b <= 600):
                    x = 200
                    y = 400
                    square = 8
                if (400 <= a < 600) and (400 <= b <= 600):
                    x = 400
                    y = 400
                    square = 9
                
                if turn == "cross":
                    turn = draw(a, b, x, y, turn, dicty, square)
                else:
                    turn = drawy(a, b, x, y, turn, dicty, square)
        
        win(turn, dicty, square, winner, text_one)           
        pygame.display.update()
        
#more functions
def text_two(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",150)
    msgobj_one = fontobj_one.render(msg_one, False, purple)
    screen.blit(msgobj_one,(x_one,y_one))
def text_three(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",100)
    msgobj_one = fontobj_one.render(msg_one, False, purple)
    screen.blit(msgobj_one,(x_one,y_one))
def text_four(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",100)
    msgobj_one = fontobj_one.render(msg_one, False, purple)
    screen.blit(msgobj_one,(x_one,y_one))
def menu(text_one, text_two):
    pygame.draw.rect(screen, (blue), (0, 0, 300, 300), 0)
    pygame.draw.rect(screen, (red), (300, 0, 300, 300), 0)
    pygame.draw.rect(screen, (green), (0, 300, 600, 300), 0)
    text_one("Play", 30, 10)
    text_one("Quit", 330, 10)
    text_two("Atiksh Paul:", 30, 330)
    text_two("Tic-Tac-Toe", 150, 430)
 
#game
while True:
    menu(text_two, text_three)
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
            l, m = pygame.mouse.get_pos()
            if (0 <= l <= 300) and (0 <= m <= 300):
                print("Play")
                screen.fill(black)
                game()
                menu(text_two, text_three)
            elif (300 < l <= 600) and (0 < m <= 300):
                print("Quit")
                pygame.quit()
                exit()
    pygame.display.update()