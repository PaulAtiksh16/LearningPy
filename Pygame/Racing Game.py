import pygame
from sys import exit
pygame.init()
import random
clock = pygame.time.Clock()
import time

#colors
white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_forest_green = ((0,255,170))
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

#display/sprites
screen = pygame.display.set_mode((800, 530))
pygame.display.set_caption("Racing!")
car = pygame.image.load("./Sprites/Racing Car.png")
track = pygame.image.load("./Sprites/Racetrack.png")
grass = pygame.image.load("./Sprites/Grass.jpg")
boom = pygame.image.load("./Sprites/Boom.png")
cone = pygame.image.load("./Sprites/Cone.png")
tires = pygame.image.load("./Sprites/Tires.png")
track = pygame.transform.scale(track, (1600, 300))
grass = pygame.transform.scale(grass, (1600, 570))
car = pygame.transform.scale(car, (120, 120))
boom = pygame.transform.scale(boom, (800, 530))
cone = pygame.transform.scale(cone, (60, 60))
tires = pygame.transform.scale(tires, (60, 60))

#text
def text_one(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",25)
    msgobj_one = fontobj_one.render(msg_one, False, white)
    screen.blit(msgobj_one,(x_one,y_one))
    
def text_two(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",100)
    msgobj_one = fontobj_one.render(msg_one, False, black)
    screen.blit(msgobj_one,(x_one,y_one))
    
def text_three(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",100)
    msgobj_one = fontobj_one.render(msg_one, False, white)
    screen.blit(msgobj_one,(x_one,y_one))

def text_four(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",75)
    msgobj_one = fontobj_one.render(msg_one, False, white)
    screen.blit(msgobj_one,(x_one,y_one))

def text_five(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",100)
    msgobj_one = fontobj_one.render(msg_one, False, blue)
    screen.blit(msgobj_one,(x_one,y_one))
    
#game
def game():
    #variables
    middle = 220
    top = 130
    bottom = 310
    lane = middle
    part = [middle, top, bottom]
    road = top
    x = 800
    car_x = 50
    stuff = [cone, tires]
    thing = cone
    lives = 5
    back_x = 0
    pass_count = 0
    streak = 0
    speed = 5
    global score
    level = 1
    la = 10
    
    #life color
    one = green
    two = green
    three = green
    four = green
    five = green
    
    #start
    screen.fill(red)
    text_two("Ready", 280, 180)
    pygame.display.update()
    time.sleep(1)
    screen.fill(yellow)
    text_two("Set", 320, 180)
    pygame.display.update()
    time.sleep(1)
    screen.fill(green)
    text_two("GO!", 320, 180)
    pygame.display.update()
    time.sleep(1)
    
    while True:
        #draw
        screen.blit(grass, (0, 0))
        pygame.draw.rect(screen, (black), (0, 0, 800, 45), 0)
        screen.blit(track, (back_x, 130))
        text_one("HP: ", 565, 10)
        text_one("Score: " + str(score), 30, 10)
        text_one("Level " + str(level), 360, 10)
        car_rect = screen.blit(car, (car_x, lane))
        thing_rect = screen.blit(thing, (x, road + 30))
        x = x - speed
        
        #lives
        pygame.draw.rect(screen, (one), (620, 10, 25, 25), 0)
        pygame.draw.rect(screen, (two), (645, 10, 25, 25), 0)
        pygame.draw.rect(screen, (three), (670, 10, 25, 25), 0)
        pygame.draw.rect(screen, (four), (695, 10, 25, 25), 0)
        pygame.draw.rect(screen, (five), (720, 10, 25, 25), 0)
        
        if lives == 5:
            one = green
            two = green
            three = green
            four = green
            five = green
        elif lives == 4:
            one = green
            two = green
            three = green
            four = green
            five = red
        elif lives == 3:
            one = green
            two = green
            three = green
            four = red
            five = red
        elif lives == 2:
            one = green
            two = green
            three = red
            four = red
            five = red
        elif lives == 1:
            one = green
            two = red
            three = red
            four = red
            five = red
        
        #car move graphic
        # if car_x >= 150:
        #     move = True
        # elif car_x <=50:
        #     move = False
            
        # if move == True:
        #     car_x = car_x - 1
        # else: 
        #     car_x = car_x + 2
        
        #back move
        if back_x >= -800:
            back_x = back_x - speed
        else:
            back_x = 0
        
        #next thing
        if x <= 5:
            x = 800
            road = random.choice(part)
            thing = random.choice(stuff)
            pass_count = pass_count + 1
            streak = streak + 1
            score = score + 1
            
        #game over
        if (car_rect.colliderect(thing_rect)):
            lives = lives - 1
            x = 800
            road = random.choice(part)
            thing = random.choice(stuff)
            streak = 0
        if lives == 0:
            break
        
        #next level
        if pass_count%la == 0 and pass_count != 0:
            level = level + 1
            screen.fill(red)
            text_three("Level " + str(level), 280, 180)
            pygame.display.update()
            time.sleep(1)
            speed = speed + 3
            lives = 5
            la = la + 10
            pass_count = 0
            
        #more lives
        if streak == 5 and lives < 5:
            lives = lives + 1
            streak = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            #move
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if lane == bottom:
                        lane = middle
                    elif lane == middle: 
                        lane = top
                        
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if lane == top:
                        lane = middle
                    elif lane == middle:
                        lane = bottom

        pygame.display.update()
    
    
    
play = True
again = None
score = 0
qwerty = 0
while True:
    if play == True:
        game()
        game_over = True
        play = False
    if game_over == True:
        screen.blit(boom, (0, 0))
        pygame.display.update()
        time.sleep(1)
        game_over = False
        qwerty = qwerty + 20*(len(str(score)))
        aaa = 250 - qwerty
    
    screen.fill(gray)
    text_five("Score: " + str(score), aaa, 80)
    pygame.draw.rect(screen, (blue), (180, 200, 420, 130), 0)
    text_four("Play Again", 230,220)
    pygame.draw.rect(screen, (blue), (180, 350, 420, 130), 0)
    text_four("Quit", 320, 370)
    
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
            l, m = pygame.mouse.get_pos()
            
            if (180 <= l <= 600) and (200 <= m <= 320):
                again = True
                play = True
                print("true")
            elif (180 <= l <= 600) and (350 <= m <= 480):
                again = False
                print("false")
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
            
    if again == False:
        pygame.quit()
        exit()