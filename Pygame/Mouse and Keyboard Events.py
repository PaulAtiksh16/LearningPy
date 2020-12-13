# import pygame
# from pygame.locals import *
# pygame.init()
# import random

# #colors
# white = ((255,255,255))
# blue = ((0,0,255))
# green = ((0,255,0))
# red = ((255,0,0))
# black = ((0,0,0))
# orange = ((255,100,10))
# yellow = ((255,255,0))
# blue_green = ((0,255,170))
# marroon = ((115,0,0))
# lime = ((180,255,100))
# pink = ((255,100,180))
# purple = ((240,0,255))
# gray = ((127,127,127))
# magenta = ((255,0,230))
# brown = ((100,40,0))
# forest_green = ((0,50,0))
# navy_blue = ((0,0,100))
# rust = ((210,150,75))
# dandilion_yellow = ((255,200,0))
# highlighter = ((255,255,100))
# sky_blue = ((0,255,255))
# light_gray = ((200,200,200))
# dark_gray = ((50,50,50))
# tan = ((230,220,170))
# coffee_brown =((200,190,140))
# moon_glow = ((235,245,255))

# screen = pygame.display.set_mode((800,570))
# pygame.display.set_caption("Shapes!!!")
# color = ( random.randint(0, 255), random.randint(0, 255), random.randint(0, 255) )
# while True:
#     pygame.draw.rect(screen, (color), (100, 100, 50, 100), 0)
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#         if event.type == pygame.KEYDOWN:
#             print(chr(event.type))
#             if event.key == pygame.K_SPACE:
#                 color = ( random.randint(0, 255), random.randint(0, 255), random.randint(0, 255) )
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             print(event.button, event.pos)
#     pygame.display.update()


# import pygame
# from pygame.locals import *
# pygame.init()
# import random
# import time
# clock = pygame.time.Clock()

# #colors
# white = ((255,255,255))
# blue = ((0,0,255))
# green = ((0,255,0))
# red = ((255,0,0))
# black = ((0,0,0))
# orange = ((255,100,10))
# yellow = ((255,255,0))
# blue_green = ((0,255,170))
# marroon = ((115,0,0))
# lime = ((180,255,100))
# pink = ((255,100,180))
# purple = ((240,0,255))
# gray = ((127,127,127))
# magenta = ((255,0,230))
# brown = ((100,40,0))
# forest_green = ((0,50,0))
# navy_blue = ((0,0,100))
# rust = ((210,150,75))
# dandilion_yellow = ((255,200,0))
# highlighter = ((255,255,100))
# sky_blue = ((0,255,255))
# light_gray = ((200,200,200))
# dark_gray = ((50,50,50))
# tan = ((230,220,170))
# coffee_brown =((200,190,140))
# moon_glow = ((235,245,255))

# screen = pygame.display.set_mode((800,570))
# pygame.display.set_caption("Shapes!!!")
# x = 300
# y = 300
# direction = None
# while True:
#     screen.fill(black)
#     pygame.draw.circle(screen, (lime), (x, y), 30, 0)
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 direction = "right"
#             if event.key == pygame.K_LEFT:
#                 direction = "left"
#             if event.key == pygame.K_UP:
#                 direction = "up"
#             if event.key == pygame.K_DOWN:
#                 direction = "down"
#         if event.type == pygame.KEYUP:
#             direction = None
            
#     if direction == "right":
#         x = x + 50
#     if direction == "left":
#         x = x - 50
#     if direction == "up":
#         y = y - 50
#     if direction == "down":
#         y = y + 50
    
#     clock.tick(20)
#     pygame.display.update()


# import pygame
# from pygame.locals import *
# pygame.init()
# import random
# import time
# clock = pygame.time.Clock()

# #colors
# white = ((255,255,255))
# blue = ((0,0,255))
# green = ((0,255,0))
# red = ((255,0,0))
# black = ((0,0,0))
# orange = ((255,100,10))
# yellow = ((255,255,0))
# blue_green = ((0,255,170))
# marroon = ((115,0,0))
# lime = ((180,255,100))
# pink = ((255,100,180))
# purple = ((240,0,255))
# gray = ((127,127,127))
# magenta = ((255,0,230))
# brown = ((100,40,0))
# forest_green = ((0,50,0))
# navy_blue = ((0,0,100))
# rust = ((210,150,75))
# dandilion_yellow = ((255,200,0))
# highlighter = ((255,255,100))
# sky_blue = ((0,255,255))
# light_gray = ((200,200,200))
# dark_gray = ((50,50,50))
# tan = ((230,220,170))
# coffee_brown =((200,190,140))
# moon_glow = ((235,245,255))

# screen = pygame.display.set_mode((800,570))
# pygame.display.set_caption("Shapes!!!")
# x = 300
# y = 300
# direction = "right"
# while True:
#     screen.fill(black)
#     pygame.draw.circle(screen, (lime), (x, y), 30, 0)
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 if direction != "left":
#                     direction = "right"
#             if event.key == pygame.K_LEFT:
#                 if direction != "right":
#                     direction = "left"
#             if event.key == pygame.K_UP:
#                 if direction != "down":
#                     direction = "up"
#             if event.key == pygame.K_DOWN:
#                 if direction != "up":
#                     direction = "down"
    
#     if y <= 0:
#         y = 570
#     elif y >= 570:
#         y = 0
    
#     if x <= 0:
#         x = 800
#     elif x >= 800:
#         x = 0
            
#     if direction == "right":
#         x = x + 50
#     if direction == "left":
#         x = x - 50
#     if direction == "up":
#         y = y - 50
#     if direction == "down":
#         y = y + 50
    
#     clock.tick(20)
#     pygame.display.update()


# import pygame
# from pygame.locals import *
# pygame.init()

# #colors
# white = ((255,255,255))
# blue = ((0,0,255))
# green = ((0,255,0))
# red = ((255,0,0))
# black = ((0,0,0))
# orange = ((255,100,10))
# yellow = ((255,255,0))
# blue_green = ((0,255,170))
# marroon = ((115,0,0))
# lime = ((180,255,100))
# pink = ((255,100,180))
# purple = ((240,0,255))
# gray = ((127,127,127))
# magenta = ((255,0,230))
# brown = ((100,40,0))
# forest_green = ((0,50,0))
# navy_blue = ((0,0,100))
# rust = ((210,150,75))
# dandilion_yellow = ((255,200,0))
# highlighter = ((255,255,100))
# sky_blue = ((0,255,255))
# light_gray = ((200,200,200))
# dark_gray = ((50,50,50))
# tan = ((230,220,170))
# coffee_brown =((200,190,140))
# moon_glow = ((235,245,255))

# def text_one(msg_one, x_one, y_one):
#     fontobj_one = pygame.font.SysFont("freesans",100)
#     msgobj_one = fontobj_one.render(msg_one, False,red)
#     screen.blit(msgobj_one,(x_one,y_one))

# screen = pygame.display.set_mode((800,570))
# pygame.display.set_caption("Shapes!!!")
# word = ""
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#         if event.type == pygame.KEYDOWN:
#             screen.fill(black)
#             word = word + chr(event.key)
#             text_one(word, 100, 100)
#     pygame.display.update()


# import pygame
# from pygame.locals import *
# pygame.init()
# import random
# import time
# clock = pygame.time.Clock()

# #colors
# white = ((255,255,255))
# blue = ((0,0,255))
# green = ((0,255,0))
# red = ((255,0,0))
# black = ((0,0,0))
# orange = ((255,100,10))
# yellow = ((255,255,0))
# blue_green = ((0,255,170))
# marroon = ((115,0,0))
# lime = ((180,255,100))
# pink = ((255,100,180))
# purple = ((240,0,255))
# gray = ((127,127,127))
# magenta = ((255,0,230))
# brown = ((100,40,0))
# forest_green = ((0,50,0))
# navy_blue = ((0,0,100))
# rust = ((210,150,75))
# dandilion_yellow = ((255,200,0))
# highlighter = ((255,255,100))
# sky_blue = ((0,255,255))
# light_gray = ((200,200,200))
# dark_gray = ((50,50,50))
# tan = ((230,220,170))
# coffee_brown =((200,190,140))
# moon_glow = ((235,245,255))

# screen = pygame.display.set_mode((800,570))
# pygame.display.set_caption("Shapes!!!")
# while True:
#     screen.fill(black)
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#         if event.type == pygame.MOUSEMOTION:
#             x, y = event.pos
#     pygame.draw.circle(screen, (lime), (x, y), 30, 0)
    
#     clock.tick(20)
#     pygame.display.update()


# import pygame
# from pygame.locals import *
# pygame.init()
# import random
# clock = pygame.time.Clock()

# #colors
# white = ((255,255,255))
# blue = ((0,0,255))
# green = ((0,255,0))
# red = ((255,0,0))
# black = ((0,0,0))
# orange = ((255,100,10))
# yellow = ((255,255,0))
# blue_green = ((0,255,170))
# marroon = ((115,0,0))
# lime = ((180,255,100))
# pink = ((255,100,180))
# purple = ((240,0,255))
# gray = ((127,127,127))
# magenta = ((255,0,230))
# brown = ((100,40,0))
# forest_green = ((0,50,0))
# navy_blue = ((0,0,100))
# rust = ((210,150,75))
# dandilion_yellow = ((255,200,0))
# highlighter = ((255,255,100))
# sky_blue = ((0,255,255))
# light_gray = ((200,200,200))
# dark_gray = ((50,50,50))
# tan = ((230,220,170))
# coffee_brown =((200,190,140))
# moon_glow = ((235,245,255))

# screen = pygame.display.set_mode((800,570))
# pygame.display.set_caption("Shapes!!!")
# color = lime
# turn = 0
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             x, y = event.pos              
#             color = ( random.randint(0, 255), random.randint(0, 255), random.randint(0, 255) )
#             turn = turn + 1
#             if turn%2 == 0:
#                 pygame.draw.rect(screen, (color), (x, y, 50, 100), 0)
#             else:
#                 pygame.draw.circle(screen, (color), (x, y), 30, 0)
#     clock.tick(20)
#     pygame.display.update()


# import pygame
# from pygame.locals import *
# pygame.init()
# import random
# clock = pygame.time.Clock()

# #colors
# white = ((255,255,255))
# blue = ((0,0,255))
# green = ((0,255,0))
# red = ((255,0,0))
# black = ((0,0,0))
# orange = ((255,100,10))
# yellow = ((255,255,0))
# blue_green = ((0,255,170))
# marroon = ((115,0,0))
# lime = ((180,255,100))
# pink = ((255,100,180))
# purple = ((240,0,255))
# gray = ((127,127,127))
# magenta = ((255,0,230))
# brown = ((100,40,0))
# forest_green = ((0,50,0))
# navy_blue = ((0,0,100))
# rust = ((210,150,75))
# dandilion_yellow = ((255,200,0))
# highlighter = ((255,255,100))
# sky_blue = ((0,255,255))
# light_gray = ((200,200,200))
# dark_gray = ((50,50,50))
# tan = ((230,220,170))
# coffee_brown =((200,190,140))
# moon_glow = ((235,245,255))

# screen = pygame.display.set_mode((800,570))
# pygame.display.set_caption("Shapes!!!")
# color = lime
# turn = 0
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if turn%2 == 0:
#                 x, y = event.pos   
#             else:
#                 a, b = event.pos
#                 # screen.fill(black)
#                 pygame.draw.line(screen, (color), (x,y), (a,b), 5)
#             color = ( random.randint(0, 255), random.randint(0, 255), random.randint(0, 255) )
#             turn = turn + 1
#     clock.tick(20)
#     pygame.display.update()


# import pygame
# from pygame.locals import *
# pygame.init()
# clock = pygame.time.Clock()

# #colors
# white = ((255,255,255))
# blue = ((0,0,255))
# green = ((0,255,0))
# red = ((255,0,0))
# black = ((0,0,0))
# orange = ((255,100,10))
# yellow = ((255,255,0))
# blue_green = ((0,255,170))
# marroon = ((115,0,0))
# lime = ((180,255,100))
# pink = ((255,100,180))
# purple = ((240,0,255))
# gray = ((127,127,127))
# magenta = ((255,0,230))
# brown = ((100,40,0))
# forest_green = ((0,50,0))
# navy_blue = ((0,0,100))
# rust = ((210,150,75))
# dandilion_yellow = ((255,200,0))
# highlighter = ((255,255,100))
# sky_blue = ((0,255,255))
# light_gray = ((200,200,200))
# dark_gray = ((50,50,50))
# tan = ((230,220,170))
# coffee_brown =((200,190,140))
# moon_glow = ((235,245,255))

# screen = pygame.display.set_mode((800,570))
# pygame.display.set_caption("Shapes!!!")
# x = 100
# y = 100
# ham = None
# while True:
#     screen.fill(black)
#     pygame.draw.circle(screen, (lime), (x, y), 30, 0)
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             ham = True
#         elif event.type == pygame.MOUSEBUTTONUP:
#             ham = False
#         elif (event.type == pygame.MOUSEMOTION) and (ham == True):
#             x, y = event.pos
    
#     clock.tick(20)
#     pygame.display.update()

# import pygame
# from pygame.locals import *
# pygame.init()
# clock = pygame.time.Clock()

# #colors
# white = ((255,255,255))
# blue = ((0,0,255))
# green = ((0,255,0))
# red = ((255,0,0))
# black = ((0,0,0))
# orange = ((255,100,10))
# yellow = ((255,255,0))
# blue_green = ((0,255,170))
# marroon = ((115,0,0))
# lime = ((180,255,100))
# pink = ((255,100,180))
# purple = ((240,0,255))
# gray = ((127,127,127))
# magenta = ((255,0,230))
# brown = ((100,40,0))
# forest_green = ((0,50,0))
# navy_blue = ((0,0,100))
# rust = ((210,150,75))
# dandilion_yellow = ((255,200,0))
# highlighter = ((255,255,100))
# sky_blue = ((0,255,255))
# light_gray = ((200,200,200))
# dark_gray = ((50,50,50))
# tan = ((230,220,170))
# coffee_brown =((200,190,140))
# moon_glow = ((235,245,255))

# screen = pygame.display.set_mode((800,570))
# pygame.display.set_caption("Shapes!!!")
# x = 100
# y = 100
# length = 0
# width = 0
# ham = None
# while True:
#     screen.fill(black)
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             ham = True
#             x, y = event.pos
#             pygame.draw.rect(screen, (rust), (x,y, width, length), 0)
#         elif event.type == pygame.MOUSEBUTTONUP:
#             ham = False
#             pygame.draw.rect(screen, (rust), (x,y, width, length), 0)
#         elif (event.type == pygame.MOUSEMOTION) and (ham == True):
#             c, d = event.pos
#             width = c - x
#             length = d - y
#             pygame.draw.rect(screen, (rust), (x,y, width, length), 0)
#     pygame.draw.rect(screen, (rust), (x,y, width, length), 0)
    
#     clock.tick(20)
#     pygame.display.update()
    

# import pygame
# from pygame.locals import *
# pygame.init()
# clock = pygame.time.Clock()

# #colors
# white = ((255,255,255))
# blue = ((0,0,255))
# green = ((0,255,0))
# red = ((255,0,0))
# black = ((0,0,0))
# orange = ((255,100,10))
# yellow = ((255,255,0))
# blue_green = ((0,255,170))
# marroon = ((115,0,0))
# lime = ((180,255,100))
# pink = ((255,100,180))
# purple = ((240,0,255))
# gray = ((127,127,127))
# magenta = ((255,0,230))
# brown = ((100,40,0))
# forest_green = ((0,50,0))
# navy_blue = ((0,0,100))
# rust = ((210,150,75))
# dandilion_yellow = ((255,200,0))
# highlighter = ((255,255,100))
# sky_blue = ((0,255,255))
# light_gray = ((200,200,200))
# dark_gray = ((50,50,50))
# tan = ((230,220,170))
# coffee_brown =((200,190,140))
# moon_glow = ((235,245,255))

# screen = pygame.display.set_mode((800,570))
# pygame.display.set_caption("Shapes!!!")
# x = 400
# y = 285
# radius = 10
# clicks = 0
# while True:
#     screen.fill(black)
#     pygame.draw.circle(screen, (lime), (x, y), radius, 0)
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#         elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
#             c, d = event.pos
#             if (x - radius <= c <= x + radius) and (y - radius <= d <= y + radius):
#                 clicks = clicks + 1
#                 if clicks%2 == 0:
#                     radius = radius*2
#         elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 3):
#             if (x - radius <= c <= x + radius) and (y - radius <= d <= y + radius):
#                 radius = radius//2
    
#     clock.tick(20)
#     pygame.display.update()


import pygame
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
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

screen = pygame.display.set_mode((800,570))
pygame.display.set_caption("Shapes!!!")
x = 0
y = 0
clicks = 0
width = 20
while True:
    pygame.draw.rect(screen, (rust), (x,y, width, width), 0)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
            c, d = event.pos
            if (x - width <= c <= x + width) and (y - width <= d <= y + width):
                clicks = clicks + 1
                if clicks%2 == 0:
                    a = random.randint(0, 780)
                    b = random.randint(0, 550)
                    pygame.draw.rect(screen, (rust), (a,b, width, width), 0)
    pygame.display.update()