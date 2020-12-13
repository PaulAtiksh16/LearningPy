import pygame
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

#variables
screen = pygame.display.set_mode((800,570))
pygame.display.set_caption("Sprite Animation!")
x = 100
y = 400
count = 0
movement = None
jumping = False
jump_height = 10
jump_offset = 0

#image loading
back = pygame.image.load("./Sprites/graveyardtilesetnew/png/BG.png")
attack_anim = []
idle_anim = []
jump_anim = []
run_anim = []
run_anim2 = []
for things in range(4):
    attack = pygame.image.load("./Sprites/ninjaadventurenew/png/Attack__00" + str(things) + ".png")
    attack = pygame.transform.scale(attack, (150, 150))
    attack_anim.append(attack)

for things in range(4):
    idle = pygame.image.load("./Sprites/ninjaadventurenew/png/Idle__00" + str(things) + ".png")
    idle = pygame.transform.scale(idle, (65, 120))
    idle_anim.append(idle)

for things in range(4):
    jump = pygame.image.load("./Sprites/ninjaadventurenew/png/Jump__00" + str(things) + ".png")
    jump = pygame.transform.scale(jump, (100, 130))
    jump_anim.append(jump)

for things in range(4):
    run = pygame.image.load("./Sprites/ninjaadventurenew/png/Run__00" + str(things) + ".png")
    run = pygame.transform.scale(run, (90, 120))
    run_anim.append(run)
for things in range(4):
    run2 = pygame.image.load("./Sprites/ninjaadventurenew/png/Run__00" + str(things) + ".png")
    run2 = pygame.transform.scale(run2, (90, 120))
    run2 = pygame.transform.flip(run2, True, False)
    run_anim2.append(run2)

while True:
    #idle
    screen.fill(black)
    screen.blit(idle_anim[count], (x, y))
    count = count + 1
    if count >= len(idle_anim):
        count = 0
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYDOWN:
            #attack
            if event.key == pygame.K_x:
                movement = "atak"
            
            #jump
            if (event.key == pygame.K_SPACE):
                movement = "jump"
            
            #run
            if event.key == pygame.K_LEFT:
                movement = "left"
            if event.key == pygame.K_RIGHT:
                movement = "right"
                
        if event.type == pygame.KEYUP:
            movement = None
            screen.fill(black)
     
    #attack
    if movement == "atak":
        screen.fill(black)
        screen.blit(attack_anim[count], (x, y))

    #jump
    if movement == "jump":
        screen.fill(black)
        screen.blit(jump_anim[count], (x, y))
        if (jumping == False) and (jump_offset == 0):
            jumping = True
    if jumping == True:
         jump_offset = jump_offset + 1
         y = y - jump_offset
         if jump_offset >= jump_height:
             jumping = False
    elif jump_offset > 0 and jumping == False:
        jump_offset = jump_offset - 1
        y = y + jump_offset
    
        
    #run
    if movement == "left":
        screen.fill(black)
        screen.blit(run_anim2[count], (x, y))
        x = x - 5
    elif movement == "right":
        screen.fill(black)
        screen.blit(run_anim[count], (x, y))
        x = x + 5
                
    clock.tick(15)
    pygame.display.update()