#imports
import random
import pygame
from sys import exit
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()

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

screen = pygame.display.set_mode((800,570))
pygame.display.set_caption("Pong!")

#background variables
star_count = 0
ex = []
why = []
x = None
y = None

#score variables
one_score = 0
two_score = 0

#functions
def text_one(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",25)
    msgobj_one = fontobj_one.render(msg_one, False,purple)
    screen.blit(msgobj_one,(x_one,y_one))
    
def text_two(msg_two, x_two, y_two):
    fontobj_two = pygame.font.SysFont("freesans",100)
    msgobj_two = fontobj_two.render(msg_two, False,purple)
    screen.blit(msgobj_two,(x_two,y_two))


#collison variables
horizontal = True
vertical = None

#shape variables
width = 50
length = 200
radius = 50
rect_one_x = 50
rect_one_y = 50
rect_two_x = 700
rect_two_y = 300
circ_x = 400
circ_y = 300

#movement variables
up_one = None
up_two = None

#background
while star_count <= 100:
    x = random.randint(1, 800)
    y = random.randint(1, 800)
    ex.append(x)
    why.append(y)
    star_count = star_count + 1
for things in range(1, 101, 1):
    pygame.draw.circle(screen, (yellow), (ex[things], why[things]), 3, 0)

while True:
    screen.fill(black)

    #background
    for things in range(1, 101, 1):
        pygame.draw.circle(screen, (yellow), (ex[things], why[things]), 3, 0)
    
    #shapes
    pygame.draw.circle(screen, (green), (circ_x, circ_y), radius, 0)
    pygame.draw.rect(screen, (red), (rect_one_x, rect_one_y, width, length), 0)
    pygame.draw.rect(screen, (blue), (rect_two_x, rect_two_y, width, length), 0)
    
    #words
    text_one(("Player one: " + str(one_score)), 10, 10)
    text_one(("Player two: " + str(two_score)), 670, 10)

    #edge collision
    if circ_x == 800:
        circ_x = 400
        one_score = one_score + 1
    if circ_x == 0:
        circ_x = 400
        two_score = two_score + 1
    
    #ball collision
    if (circ_x == rect_two_x - 50) and (rect_two_y <= circ_y <= rect_two_y + 200):
        horizontal = False
        if rect_two_y <= circ_y + 50 <= rect_two_y + 100:
            vertical = True
        if rect_two_y + 100 <= circ_y - 50 <= rect_two_y + 200:
            vertical = False
    
    elif (rect_two_x <= circ_x + 50 <= rect_two_x + 50) and (rect_two_y == circ_y + 50):
        horizontal = False
        vertical = False
    elif (rect_two_x <= circ_x + 50 <= rect_two_x + 50) and (rect_two_y + 200 == circ_y - 50):
        horizontal = False
        vertical = False
    
    if (circ_x == rect_one_x + 100) and (rect_one_y <= circ_y <= rect_one_y + 200):
        horizontal = True
        if rect_one_y <= circ_y + 50 <= rect_one_y + 100:
            vertical = True
        if rect_one_y + 100 <= circ_y - 50 <= rect_one_y + 200:
            vertical = False
        
    elif (rect_one_x <= circ_x - 50 <= rect_one_x + 50) and (rect_one_y == circ_y + 50):
        horizontal = False
        vertical = False
    elif (rect_one_x <= circ_x - 50 <= rect_one_x + 50) and (rect_one_y + 200 == circ_y - 50):
        horizontal = False
        vertical = False
        
    if circ_y + 50 >= 570:
        vertical = True
    if circ_y - 50 <= 0:
        vertical = False
    
    #ball bouncing
    if horizontal == True:
        circ_x = circ_x + 1
    if horizontal == False:
        circ_x = circ_x - 1
        
    if vertical == True:
        circ_y = circ_y - 1
    if vertical == False:
        circ_y = circ_y + 1   
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        #paddle movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up_two = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                up_two = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                up_one = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                up_one = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_two = None
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                up_two = None
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                up_one = None
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                up_one = None

    #paddle movement
    if up_two == True:
        rect_two_y = rect_two_y - 1
    if up_two == False:
        rect_two_y = rect_two_y + 1
    if up_one == True:
        rect_one_y = rect_one_y - 1
    if up_one == False:
        rect_one_y = rect_one_y + 1

    #paddle barriers
    if (rect_one_y == 0) or (rect_one_y == 370):
        up_one = None
    if (rect_two_y == 0) or (rect_two_y == 370):
        up_two = None
        
    #score
    if one_score == 5:
        print("Player one wins!")
        break
    if two_score == 5:
        print("Player two wins!")
        break

    clock.tick(500)
    pygame.display.update()
if one_score == 5:
    text_two("Player one wins!", 100, 235)
if two_score == 5:
    text_two("Player two wins!", 100, 235)
pygame.display.update()