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
dark_green = ((0,153,0))

#variables
pipe_width = 50
gap = 100
radius = 30
x = 350
y = 350
pipe_x = 500
pipe_top_length = 300
game_over = False
score = 0

#functions
def text_one(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",100)
    msgobj_one = fontobj_one.render(msg_one, False,purple)
    screen.blit(msgobj_one,(x_one,y_one))

def text_two(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",50)
    msgobj_one = fontobj_one.render(msg_one, False,blue)
    screen.blit(msgobj_one,(x_one,y_one))

screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Flappy Bird!")
back = pygame.image.load("./Sprites/free_plane_sprite/png/BG.png")
back = pygame.transform.scale(back, (700, 700))
bird = pygame.image.load("./Sprites/Flappy Bird.png")
bird = pygame.transform.scale(bird, (90, 90))

while True:  
    #shapes
    pipe_bottom_y = pipe_top_length + 200
    screen.blit(back, (0, 0))
    birdrect = screen.blit(bird, (x-30, y-30))
    pipe_top_rect = pygame.draw.rect(screen, (dark_green), (pipe_x, 0, pipe_width, pipe_top_length), 0)
    pipe_bottom_rect = pygame.draw.rect(screen, (dark_green), (pipe_x, pipe_bottom_y, pipe_width, 700), 0)
    text_two("Score: " + str(score), 200, 50)
    y = y + 2
    pipe_x = pipe_x - 1
    
    #pipes
    if pipe_x <= -50:
        pipe_x = 650
        pipe_top_length = random.randint(0, 500)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y = y - 50
                
    #score
    if x == pipe_x + 50:
        score = score + 1
    
    #collision
    if (birdrect.colliderect(pipe_top_rect)):
        game_over = True
    if (birdrect.colliderect(pipe_bottom_rect)):
        game_over = True
    if (y - 30 <= 0) or (y + 30 >= 700):
        game_over = True
    
    if score == 10:
        game_over = True
        
    #game over
    if game_over == True:
        screen.fill(black)
        if score != 10:
            text_one("Game Over!", 200, 200)
        if score == 10:
            text_one("You Win!", 200, 200)
    
    clock.tick(80)
    pygame.display.update()