##import time
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
##width = 80
##length = 80
##x = 0
##pygame.display.set_caption("Shapes!!!")
##clock = pygame.time.Clock()
##while True:
##    screen.fill(black)
##    pygame.draw.rect(screen, (white), (x,0, width, length), 0)
##    x = x + 80
##    if x == 800:
##        x = 0
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    clock.tick(25)
##    pygame.display.update()


##import time
##import random
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
##stuff = [white, blue, green, red, black, orange, yellow, blue_green, marroon, lime, pink, purple, gray, magenta, brown, forest_green, rust, tan]
##screen = pygame.display.set_mode((700,700))
##width = 70
##length = 70
##x = 0
##y = 0
##oof = 10
##pygame.display.set_caption("Shapes!!!")
##clock = pygame.time.Clock()
##while True:
##    screen.fill(black)
##    color = random.choice(stuff)
##    pygame.draw.rect(screen, (color), (x,y, width, length), 0)
##    x = x + 70
##    if x == 700 and y != 700:
##        x = 0
##        y = y + 80
##    if x >= 630 and y >= 630:
##        x = 0
##        y = 0
##        oof = oof + 5
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    clock.tick(oof)
##    pygame.display.update()


##import random
##import time
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
##stuff = [white, blue, green, red, black, orange, yellow, blue_green, marroon, lime, pink, purple, gray, magenta, brown, forest_green, rust, tan]
##screen = pygame.display.set_mode((700,700))
##width = 70
##length = 70
##x = 0
##y = 0
##pygame.display.set_caption("Shapes!!!")
##clock = pygame.time.Clock()
##while True:
##    color = random.choice(stuff)
##    screen.fill(black)
##    pygame.draw.rect(screen, (color), (x,y, width, length), 0)
##    x = x + 70
##    y = y + 70
##    if x == 700 and y == 700:
##        x = 0
##        y = 0
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    clock.tick(10)
##    pygame.display.update()


##import random
##import time
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
##stuff = [white, blue, green, red, black, orange, yellow, blue_green, marroon, lime, pink, purple, gray, magenta, brown, forest_green, rust, tan]
##screen = pygame.display.set_mode((700,700))
##width = 70
##length = 70
##x = 0
##y = 0
##exe = 630
##why = 0
##pygame.display.set_caption("Shapes!!!")
##clock = pygame.time.Clock()
##while True:
##    color = random.choice(stuff)
##    screen.fill(black)
##    pygame.draw.rect(screen, (color), (x,y, width, length), 0)
##    pygame.draw.rect(screen, (color), (exe,why, width, length), 0)
##    x = x + 70
##    y = y + 70
##    exe = exe - 70
##    why = why + 70
##    if x == 700 and y == 700:
##        x = 0
##        y = 0
##    if exe == -70 and why == 700:
##        exe = 630
##        why = 0
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    clock.tick(5)
##    pygame.display.update()


##import random
##import time
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
##stuff = [white, blue, green, red, black, orange, yellow, blue_green, marroon, lime, pink, purple, gray, magenta, brown, forest_green, rust, tan]
##screen = pygame.display.set_mode((700,700))
##width = 70
##length = 70
##x = 0
##y = 0
##exe = 630
##why = 0
##pygame.display.set_caption("Shapes!!!")
##clock = pygame.time.Clock()
##radius = 10
##edge = False
##while True:
##    color = random.choice(stuff)
##    screen.fill(black)
##    pygame.draw.circle(screen, (color), (350, 350), radius, 0)
##    if edge == False:
##        radius = radius + 1
##        if radius == 350:
##            edge = True
##    if edge == True:
##        radius = radius - 1
##        if radius == 10:
##            edge = False
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    clock.tick(50)
##    pygame.display.update()


##import random
##import time
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
##stuff = [white, blue, green, red, black, orange, yellow, blue_green, marroon, lime, pink, purple, gray, magenta, brown, forest_green, rust, tan]
##screen = pygame.display.set_mode((700,700))
##width = 70
##length = 70
##x = 0
##y = 0
##exe = 630
##why = 0
##pygame.display.set_caption("Shapes!!!")
##clock = pygame.time.Clock()
##radius = 10
##edge = False
##color = random.choice(stuff)
##while True:
##    screen.fill(black)
##    pygame.draw.circle(screen, (color), (350, 350), radius, 0)
##    if edge == False:
##        radius = radius + 1
##        if radius == 350:
##            edge = True
##            color = random.choice(stuff)
##    if edge == True:
##        radius = radius - 1
##        if radius == 10:
##            edge = False
##            color = random.choice(stuff)
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    clock.tick(100)
##    pygame.display.update()


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
##width = 600
##length = 300
##screen = pygame.display.set_mode((800,570))
##pygame.display.set_caption("Shapes!!!")
##while True:
##    pygame.draw.rect(screen, (red), (100, 100, width, length), 0)
##    pygame.draw.circle(screen, (light_gray), (200, 400), 100, 0)
##    pygame.draw.circle(screen, (light_gray), (600, 400), 100, 0)
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    pygame.display.update()


##import time
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
##width = 100
##length = 50
##screen = pygame.display.set_mode((800,570))
##pygame.display.set_caption("Shapes!!!")
##clock = pygame.time.Clock()
##x = 100
##ex = 125
##eexe = 175
##while True:
##    screen.fill(black)
##    pygame.draw.rect(screen, (red), (x, 300, width, length), 0)
##    pygame.draw.circle(screen, (light_gray), (ex, 350), 10, 0)
##    pygame.draw.circle(screen, (light_gray), (eexe, 350), 10, 0)
##    x = x + 1
##    ex = ex + 1
##    eexe = eexe + 1
##    if x == 600:
##        x = 100
##        ex = 125
##        eexe = 175
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    clock.tick(50)
##    pygame.display.update()


##import time
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
##width = 100
##length = 50
##screen = pygame.display.set_mode((800,570))
##pygame.display.set_caption("Shapes!!!")
##clock = pygame.time.Clock()
##x = 100
##ex = 125
##eexe = 175
##y = 300
##why = 350
##direction = None
##while True:
##    screen.fill(black)
##    pygame.draw.rect(screen, (red), (x, y, width, length), 0)
##    pygame.draw.circle(screen, (light_gray), (ex, why), 10, 0)
##    pygame.draw.circle(screen, (light_gray), (eexe, why), 10, 0)
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                direction = "left"
##            if event.key == pygame.K_RIGHT:
##                direction = "right"
##            if event.key == pygame.K_UP:
##                direction = "up"
##            if event.key == pygame.K_DOWN:
##                direction = "down"
##        if event.type == pygame.KEYUP:
##            if event.key == pygame.K_LEFT:
##                direction = None
##            if event.key == pygame.K_RIGHT:
##                direction = None
##            if event.key == pygame.K_UP:
##                direction = None
##            if event.key == pygame.K_DOWN:
##                direction = None
##    if direction == "right":
##        x = x + 10
##        ex = ex + 10
##        eexe = eexe + 10
##    if direction == "left":
##        x = x - 10
##        ex = ex - 10
##        eexe = eexe - 10
##    if direction == "up":
##        y = y - 10
##        why = why - 10
##    if direction == "down":
##        y = y + 10
##        why = why + 10
##    if x > 700:
##        x = 100
##        ex = 125
##        eexe = 175
##        y = 300
##        why = 350
##    if y < 0:
##        x = 100
##        ex = 125
##        eexe = 175
##        y = 300
##        why = 350
##    if x < 0:
##        x = 100
##        ex = 125
##        eexe = 175
##        y = 300
##        why = 350
##    if y > 510:
##        x = 100
##        ex = 125
##        eexe = 175
##        y = 300
##        why = 350
##    clock.tick(50)
##    pygame.display.update()


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
##x = 0
##color = red
##width = 80
##length = 80
##screen = pygame.display.set_mode((800,570))
##pygame.display.set_caption("Shapes!!!")
##while True:
##    for things in range(1,10,1):
##        pygame.draw.rect(screen, (red), (x, 0, width, length), 0)
####        pygame.draw.rect(screen, (color), (x, 0, width, length), 0)
##        x = x + 80
####        if color == blue:
####            color = red
####        else:
####            color = blue
##        red, blue = blue, red
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    pygame.display.update()


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
##x = 0
##y = 0
##color = red
##width = 70
##length = 70
##screen = pygame.display.set_mode((700,700))
##pygame.display.set_caption("Shapes!!!")
##while True:
##    for thingamajigs in range(1, 10, 1):
##        for things in range(1,11,1):
##            pygame.draw.rect(screen, (color), (x, y, width, length), 0)
##            x = x + 70
##            if color == blue:
##                color = red
##            else:
##                color = blue
##        y = y + 70
##        x = 0
##        if color == blue:
##            color = red
##        else:
##            color = blue
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    pygame.display.update()


##import random
##import pygame
##from pygame.locals import *
##pygame.init()
##
##x = 0
##y = 0
###functions
##def color_board(color, stuff, listbr, x, y):
##        for thingamajigs in range(1, 10, 1):
##            for things in range(1,11,1):
##                if color == listbr[-1]:
##                    color = random.choice(stuff)
##                if len(listbr) >= 10:
##                    if listbr[-10] == color:
##                        color = random.choice(stuff)
##                pygame.draw.rect(screen, (color), (x, y, width, length), 0)
##                listbr.append(color)
##                color = random.choice(stuff)
##                x = x + 70
##            y = y + 70
##            x = 0
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
##stuff = [white, blue, green, red, black, orange, yellow, blue_green, marroon, lime, pink, purple, gray, magenta, brown, forest_green, rust, tan]
##color = random.choice(stuff)
##listbr = []
##listbr.append(color)
##width = 70
##length = 70
##screen = pygame.display.set_mode((700,700))
##pygame.display.set_caption("Shapes!!!")
##while True:
##    color_board(color, stuff, listbr, x, y)
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    pygame.display.update()


##import random
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
##ex = []
##why = []
##counter = 0
##
##screen = pygame.display.set_mode((700,700))
##pygame.display.set_caption("Shapes!!!")
##x = None
##y = None
##while True:
##    while counter <= 100:
##        x = random.randint(1, 700)
##        y = random.randint(1, 700)
##        ex.append(x)
##        why.append(y)
##        counter = counter + 1
##    for things in range(1, 101, 1):
##        pygame.draw.circle(screen, (white), (ex[things], why[things]), 3, 0)
##    
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    pygame.display.update()


##import random
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
##ex = []
##why = []
##counter = 0
##oof = 0
##
##while counter <= 100:
##        x = random.randint(1, 700)
##        y = random.randint(1, 700)
##        ex.append(x)
##        why.append(y)
##        counter = counter + 1
##
##screen = pygame.display.set_mode((700,700))
##pygame.display.set_caption("Shapes!!!")
##whellow = [white, yellow]
##while True:
##    screen.fill(black)
##
##    for things in range(1, 101, 1):
##        pygame.draw.circle(screen, (random.choice(whellow)), (ex[things], why[things] + 1), 3, 0)
##        why[things] = why[things] + 1
##        if why[things] == 700:
##            why[things] = 0
##
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    pygame.display.update()


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

screen = pygame.display.set_mode((800,700))
pygame.display.set_caption("Shapes!!!")
y = 350
x_one = 100
x_two = 700
inside = True
while True:
    screen.fill(black)
    pygame.draw.circle(screen, (white), (x_one, y), 100, 0)
    pygame.draw.circle(screen, (yellow), (x_two, y), 100, 0)
    if inside == True:
        x_one = x_one + 1
        x_two = x_two - 1
        if (x_two == 500) and (x_one == 300):
            inside = False
    if inside == False:
        x_one = x_one - 1
        x_two = x_two + 1
        if (x_two == 700) and (x_one == 100):
            inside = True
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
