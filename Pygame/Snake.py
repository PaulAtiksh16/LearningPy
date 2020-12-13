import pygame
from pygame.locals import *
pygame.init()
import random
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

#functions
def text_one(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",100)
    msgobj_one = fontobj_one.render(msg_one, False,purple)
    screen.blit(msgobj_one,(x_one,y_one))
    
def text_two(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",30)
    msgobj_one = fontobj_one.render(msg_one, False,blue)
    screen.blit(msgobj_one,(x_one,y_one))

#variables
screen = pygame.display.set_mode((640,700))
pygame.display.set_caption("Snake!")
foodx = (random.randint(0, 640)//10)*10
foody = (random.randint(0, 640)//10)*10
snakex = (random.randint(0, 640)//10)*10
snakey = (random.randint(0, 640)//10)*10
direction = None
snakelist = []
snakerect = pygame.draw.rect(screen, (green), (snakex, snakey, 10, 10), 0)
speed = 10
gameover = False
score = 0

snakelist.append([snakex, snakey])
while True:
    #drawing
    screen.fill(black)
    foodrect = pygame.draw.rect(screen, (red), (foodx, foody, 10, 10), 0)
    scorerect = pygame.draw.rect(screen, (yellow), (0, 640, 640, 60), 0)
    text_two("Score: " + str(score), 100, 655)
    for segment in snakelist:
        snakerect = pygame.draw.rect(screen, green, segment+[10,10])
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        #movement
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if direction != "up":
                    direction = "down"
            if event.key == pygame.K_UP:
                if direction != "down":
                    direction = "up"
            if event.key == pygame.K_LEFT:
                if direction != "right":
                    direction = "left"
            if event.key == pygame.K_RIGHT:
                if direction != "left":
                    direction = "right"
    if direction == "down":
        snakey = snakey + 10
    elif direction == "up":
        snakey = snakey - 10
    elif direction == "left":
        snakex = snakex - 10
    elif direction == "right":
        snakex = snakex + 10
    
    #wall collision
    if snakex >= 640:
        snakex = 0
    elif snakex <=0:
        snakex = 640
    if snakey >= 640:
        snakey = 0
    elif snakey <=0:
        snakey = 640
        
    #eat
    if snakerect.colliderect(foodrect):
        foodx = (random.randint(0, 640)//10)*10
        foody = (random.randint(0, 640)//10)*10
        score = score + 1
        if len(snakelist) == 10:
            snakelist = []
            speed = speed + 5
            snakelist.append([snakex, snakey])
        else:
            snakelist.append([snakex, snakey])
        
    #body collision
    if snakelist[0] in snakelist[1:]:
        print("Game Over!")
        gameover = True
        
    #game over
    if gameover == True:
        screen.fill(black)
        text_one("Game Over!", 100, 200)
            
    clock.tick(speed)
    snakelist.insert(0, [snakex, snakey])
    snakelist.pop()
    pygame.display.update()