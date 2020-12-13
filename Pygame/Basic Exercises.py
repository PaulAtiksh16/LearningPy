# import pygame
# from pygame.locals import *
# pygame.init()
# screen = pygame.display.set_mode((800,570))
# pygame.display.set_caption("Shapes!!!")
# while True:
#   for event in pygame.event.get():
#     pygame.draw.circle(screen, (0,255,0), (400, 285), 100, 0)
#     if event.type == QUIT:
#         pygame.quit()
#         exit()
#     pygame.display.update()


# import pygame
# import random
# length = random.randint(1,800)
# width = random.randint(1,570)
# from pygame.locals import *
# pygame.init()
# screen = pygame.display.set_mode((800,570))
# pygame.display.set_caption("Shapes!!!")
# while True:
#   for event in pygame.event.get():
#     pygame.draw.rect(screen, (0,0,255), (0, 0, width, length), 0)
#     if event.type == QUIT:
#         pygame.quit()
#         exit()
#     pygame.display.update()


## import pygame
## from pygame.locals import *
## pygame.init()
## screen = pygame.display.set_mode((800,570))
## pygame.display.set_caption("Shapes!!!")
## while True:
##   for event in pygame.event.get():
##     pygame.draw.line(screen, (250,235,215), (1,1), (800,1), 5)
##     pygame.draw.line(screen, (250,235,215),(800,1),(400,569),5)
##     pygame.draw.line(screen, (250,235,215), (400,569), (1,1), 5)
##     if event.type == QUIT:
##         pygame.quit()
##         exit()
##     pygame.display.update()


# import pygame
# from pygame.locals import *
# pygame.init()
# screen = pygame.display.set_mode((800,570))
# pygame.display.set_caption("Shapes!!!")
# while True:
#   pygame.draw.polygon(screen, (250,235,215), ((1, 1), (800, 1), (400,569)), 5)
#   for event in pygame.event.get():
#     if event.type == QUIT:
#         pygame.quit()
#         exit()
#   pygame.display.update()


##import pygame
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((800,570))
##pygame.display.set_caption("Shapes!!!")
##length = 40
##width = 28
##while True:
##   pygame.draw.rect(screen, (0,0,255), (0, 0, width, length), 0)
##   pygame.draw.rect(screen, (0,0,255), (400, 285, width, length), 0)
##   for event in pygame.event.get():
##      if event.type == QUIT:
##        pygame.quit()
##        exit()
##   pygame.display.flip()


##import pygame
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((800,570))
##pygame.display.set_caption("Shapes!!!")
##while True:
##    pygame.draw.circle(screen, (0,255,0), (0, 0), 50, 0)
##    pygame.draw.circle(screen, (0,255,0), (800, 0), 50, 0)
##    pygame.draw.circle(screen, (0,255,0), (0, 570), 50, 0)
##    pygame.draw.circle(screen, (0,255,0), (800, 570), 50, 0)
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##        pygame.display.update()


##import pygame
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((800,570))
##pygame.display.set_caption("Shapes!!!")
##while True:
##    pygame.draw.circle(screen, (255, 100, 10), (0, 0), 50, 0)
##    pygame.draw.circle(screen, (255, 100, 10), (800, 0), 50, 0)
##    pygame.draw.circle(screen, (255, 100, 10), (0, 570), 50, 0)
##    pygame.draw.circle(screen, (255, 100, 10), (800, 570), 50, 0)
##    pygame.draw.circle(screen, (255, 100, 10), (400, 285), 50, 0)
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##        pygame.display.update()


##import pygame
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((800,570))
##pygame.display.set_caption("Shapes!!!")
##while True:
##    pygame.draw.polygon(screen, (250,235,215), ((200, 20), (200, 500), (400,500)), 5)
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##        pygame.display.update()

##import pygame
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((800,570))
##pygame.display.set_caption("Shapes!!!")
##while True:
##  for event in pygame.event.get():
##    pygame.draw.line(screen, (250,235,215), (0,0), (800,570), 5)
##    pygame.draw.line(screen, (250,235,215),(800,0),(0,570),5)
##    if event.type == QUIT:
##        pygame.quit()
##        exit()
##    pygame.display.update()


##x_line = 0
##y_line = 0
##import pygame
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((800,570))
##pygame.display.set_caption("Shapes!!!")
##while True:
##    for things in range(1,11,1):
##        pygame.draw.line(screen, (250,235,215), (x_line,0), (x_line,570), 5)
##        pygame.draw.line(screen, (250,235,215), (0,y_line), (800,y_line), 5)
##        x_line = x_line + 80
##        y_line = y_line + 57
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##        pygame.display.update()


##import pygame
##from pygame.locals import *
##pygame.init()
##
###colors
##white = ((255,255,255))
##blue = ((0,0,255))
##green = ((0,255,0))
##red = ((255,0,0))
##black = ((0,0,0))
##orange = ((255,100,10))
##yellow = ((255,255,0))
##blue_green = ((0,255,170))
##marroon = ((115,0,0))
##lime = ((180,255,100))
##pink = ((255,100,180))
##purple = ((240,0,255))
##gray = ((127,127,127))
##magenta = ((255,0,230))
##brown = ((100,40,0))
##forest_green = ((0,50,0))
##navy_blue = ((0,0,100))
##rust = ((210,150,75))
##dandilion_yellow = ((255,200,0))
##highlighter = ((255,255,100))
##sky_blue = ((0,255,255))
##light_gray = ((200,200,200))
##dark_gray = ((50,50,50))
##tan = ((230,220,170))
##coffee_brown =((200,190,140))
##moon_glow = ((235,245,255))
##
##screen = pygame.display.set_mode((800,570))
##pygame.display.set_caption("Shapes!!!")
##while True:
##    pygame.draw.polygon(screen, (brown), ((350,350), (450,350), (450,550), (350,550)), 5)
##    pygame.draw.polygon(screen, (yellow), ((100, 150), (100, 550), (700, 550), (700,150)), 5)
##    pygame.draw.polygon(screen, (red), ((400, 5), (80, 150), (720,150)), 5)
##    pygame.draw.polygon(screen, (blue), ((150,200), (300,200), (300,350), (150,350)), 5)
##    pygame.draw.polygon(screen, (blue), ((650,200), (500,200), (500,350), (650,350)), 5)
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##        pygame.display.update()


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

screen = pygame.display.set_mode((800,570))
width = 400
length = 200
gacho = 200
palo = 400
goo = 600
oof = 800
aaa = 400
pygame.display.set_caption("Shapes!!!")
while True:
    pygame.draw.rect(screen, (light_gray), (200, 50, width, length), 0)
    pygame.draw.circle(screen, red, (300, 150), 50, 0)
    pygame.draw.circle(screen, red, (500, 150), 50, 0)
    pygame.draw.rect(screen, (dark_gray), (300, 250, gacho, palo), 0)
    pygame.draw.rect(screen, (dark_gray), (0, 450, oof, aaa), 0)
    pygame.draw.rect(screen, (light_gray), (100, 400, goo, aaa), 0)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()


