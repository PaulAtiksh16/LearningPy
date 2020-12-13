import pygame
from pygame.locals import *
pygame.init()

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

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Shapes!!!")

#functions
def text_one(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",150)
    msgobj_one = fontobj_one.render(msg_one, False, purple)
    screen.blit(msgobj_one,(x_one,y_one))
def text_two(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",100)
    msgobj_one = fontobj_one.render(msg_one, False, purple)
    screen.blit(msgobj_one,(x_one,y_one))
def text_three(msg_one, x_one, y_one):
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
    
while True:
    menu(text_one, text_two)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
            l, m = pygame.mouse.get_pos()
            if (0 <= l <= 300) and (0 <= m <= 300):
                print("Play")
            elif (300 < l <= 600) and (0 < m <= 300):
                print("Quit")
                pygame.quit()
                exit()
    pygame.display.update()