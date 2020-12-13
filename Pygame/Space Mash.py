import pygame
from pygame.locals import *
import random
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

#text functions
def text_one(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",32)
    msgobj_one = fontobj_one.render(msg_one, False,red)
    screen.blit(msgobj_one,(x_one,y_one))
def text_two(msg_one, x_one, y_one):
    fontobj_one = pygame.font.SysFont("freesans",200)
    msgobj_one = fontobj_one.render(msg_one, False,green)
    screen.blit(msgobj_one,(x_one,y_one))

#variables
stuff = [white, blue, green, red, black, orange, yellow, blue_green, marroon, lime, pink, purple, gray, magenta, brown, forest_green, rust, tan]
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Space Mash!")
color = random.choice(stuff)
width = 800
length = 570
radius = 10
edge = False
counter = 0
ex = []
why = []
x = None
y = None
count = 0

#background
while count <= 100:
        x = random.randint(1, 700)
        y = random.randint(1, 700)
        ex.append(x)
        why.append(y)
        count = count + 1
for things in range(1, 101, 1):
    koler = random.choice(stuff)
    pygame.draw.circle(screen, (koler), (ex[things], why[things]), 3, 0)

#text
print("Let's play space mash! Mash space as many times as you can in ten seconds.")
text_one("LET'S PLAY SPACE MASH!!!", 100, 100)
text_one("Mash space as many times as possible in 10", 50, 200)
text_one("seconds.", 250, 250)
pygame.display.update()
pygame.time.wait(3000)
print("Ready?")
screen.fill(black)
for things in range(1, 101, 1):
    koler = random.choice(stuff)
    pygame.draw.circle(screen, (koler), (ex[things], why[things]), 3, 0)
text_one("READY?", 150, 150)
pygame.display.update()
pygame.time.wait(1000)
screen.fill(black)
for things in range(1, 101, 1):
    koler = random.choice(stuff)
    pygame.draw.circle(screen, (koler), (ex[things], why[things]), 3, 0)
pygame.display.update()
print("GO!")
text_two("GO!", 300, 300)

start_time = pygame.time.get_ticks()

while True:
    color = random.choice(stuff)

    #events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                counter = counter + 1
                
                #circle animation
                pygame.draw.circle(screen, (color), (350, 350), radius, 0)
                if edge == False:
                    radius = radius + 10
                    if radius == 350:
                        edge = True
                        color = random.choice(stuff)
                if edge == True:
                    radius = radius - 10
                    if radius == 10:
                        edge = False
                        color = random.choice(stuff)
    
    #game end
    time_now = pygame.time.get_ticks()
    elapsed = time_now - start_time
    if elapsed >= 10000:
        break
    pygame.display.update()

#score
screen.fill(black)
for things in range(1, 101, 1):
    koler = random.choice(stuff)
    pygame.draw.circle(screen, (koler), (ex[things], why[things]), 3, 0)
print("You pushed space", counter ,"times in ten seconds!")

if counter == 0:
    text_one(("You got " + str(counter) + " clicks! Are you dead?"), 100, 200)
elif counter <= 10:
    text_one(("Are you a sloth? You got " + str(counter) + " clicks."), 100, 250)
elif 10 < counter <= 30:
    text_one(("You only got " + str(counter) + " clicks. Try again."), 100, 250)
elif 30 < counter <= 80:
    text_one(("Pretty average. You got " + str(counter) + " clicks."), 100, 250)
elif 80 < counter <= 130:
    text_one(("Amazing! You got " + str(counter) + " clicks!"), 100, 250)
else:
    text_one(("You're using an auto clicker, aren't you?"), 100, 200)
    text_one((" You got " + str(counter) + " clicks!"), 100, 250)

pygame.display.update()
