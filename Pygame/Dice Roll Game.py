import pygame
from pygame.locals import *
pygame.init()
import random

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
dice_choices = [1,2,3,4,5,6]
score = 0

screen = pygame.display.set_mode((800,570))
pygame.display.set_caption("Shapes!!!")

#text functions
def text_one(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",100)
    msgobj_one = fontobj_one.render(msg_one, False,red)
    screen.blit(msgobj_one,(x_one,y_one))

#initial draw
pygame.draw.rect(screen, (white), (50,220, 300, 300), 0)
pygame.draw.rect(screen, (white), (450,220, 300, 300), 0)
pygame.draw.circle(screen, (black), (200, 370), 30, 0)
pygame.draw.circle(screen, (black), (600, 370), 30, 0)

#choose
while True:
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
            dice_one = random.choice(dice_choices)
            dice_two = random.choice(dice_choices)
            screen.fill(black)
            print(dice_one)
            print(dice_two)
            text_one("Score: " + str(score), 250, 20)
            
            #point
            if dice_one == dice_two:
                print("match")
                score = score + 5
            else: 
                print("miss")
                score = score - 1
                
            #draw dice 1
            if dice_one == 1:
                pygame.draw.rect(screen, (white), (50,220, 300, 300), 0)
                pygame.draw.circle(screen, (black), (200, 370), 30, 0)
            elif dice_one == 2:
                pygame.draw.rect(screen, (white), (50,220, 300, 300), 0)
                pygame.draw.circle(screen, (black), (130, 290), 30, 0)
                pygame.draw.circle(screen, (black), (270, 450), 30, 0)
            elif dice_one == 3:
                pygame.draw.rect(screen, (white), (50,220, 300, 300), 0)
                pygame.draw.circle(screen, (black), (130, 290), 30, 0)
                pygame.draw.circle(screen, (black), (270, 450), 30, 0)
                pygame.draw.circle(screen, (black), (200, 370), 30, 0)
            elif dice_one == 4:
                pygame.draw.rect(screen, (white), (50,220, 300, 300), 0)
                pygame.draw.circle(screen, (black), (130, 290), 30, 0)
                pygame.draw.circle(screen, (black), (270, 450), 30, 0)
                pygame.draw.circle(screen, (black), (270, 290), 30, 0)
                pygame.draw.circle(screen, (black), (130, 450), 30, 0)
            elif dice_one == 5:
                pygame.draw.rect(screen, (white), (50,220, 300, 300), 0)
                pygame.draw.circle(screen, (black), (130, 290), 30, 0)
                pygame.draw.circle(screen, (black), (270, 450), 30, 0)
                pygame.draw.circle(screen, (black), (270, 290), 30, 0)
                pygame.draw.circle(screen, (black), (130, 450), 30, 0)
                pygame.draw.circle(screen, (black), (200, 370), 30, 0)
            elif dice_one == 6:
                pygame.draw.rect(screen, (white), (50,220, 300, 300), 0)
                pygame.draw.circle(screen, (black), (130, 290), 30, 0)
                pygame.draw.circle(screen, (black), (270, 450), 30, 0)
                pygame.draw.circle(screen, (black), (270, 290), 30, 0)
                pygame.draw.circle(screen, (black), (130, 450), 30, 0)
                pygame.draw.circle(screen, (black), (130, 370), 30, 0)
                pygame.draw.circle(screen, (black), (270, 370), 30, 0)
                
            #draw dice 2
            if dice_two == 1:
                pygame.draw.rect(screen, (white), (450,220, 300, 300), 0)
                pygame.draw.circle(screen, (black), (600, 370), 30, 0)
            elif dice_two == 2:
                pygame.draw.rect(screen, (white), (450,220, 300, 300), 0)
                pygame.draw.circle(screen, (black), (530, 290), 30, 0)
                pygame.draw.circle(screen, (black), (670, 450), 30, 0)
            elif dice_two == 3:
                pygame.draw.rect(screen, (white), (450,220, 300, 300), 0)
                pygame.draw.circle(screen, (black), (530, 290), 30, 0)
                pygame.draw.circle(screen, (black), (670, 450), 30, 0)
                pygame.draw.circle(screen, (black), (600, 370), 30, 0)
            elif dice_two == 4:
                pygame.draw.rect(screen, (white), (450,220, 300, 300), 0)
                pygame.draw.circle(screen, (black), (530, 290), 30, 0)
                pygame.draw.circle(screen, (black), (670, 450), 30, 0)
                pygame.draw.circle(screen, (black), (670, 290), 30, 0)
                pygame.draw.circle(screen, (black), (530, 450), 30, 0)
            elif dice_two == 5:
                pygame.draw.rect(screen, (white), (450,220, 300, 300), 0)
                pygame.draw.circle(screen, (black), (530, 290), 30, 0)
                pygame.draw.circle(screen, (black), (670, 450), 30, 0)
                pygame.draw.circle(screen, (black), (670, 290), 30, 0)
                pygame.draw.circle(screen, (black), (530, 450), 30, 0)
                pygame.draw.circle(screen, (black), (600, 370), 30, 0)
            elif dice_two == 6:
                pygame.draw.rect(screen, (white), (450,220, 300, 300), 0)
                pygame.draw.circle(screen, (black), (530, 290), 30, 0)
                pygame.draw.circle(screen, (black), (670, 450), 30, 0)
                pygame.draw.circle(screen, (black), (670, 290), 30, 0)
                pygame.draw.circle(screen, (black), (530, 450), 30, 0)
                pygame.draw.circle(screen, (black), (530, 370), 30, 0)
                pygame.draw.circle(screen, (black), (670, 370), 30, 0)
       
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()