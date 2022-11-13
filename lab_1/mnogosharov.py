import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))
count_popadaniy=0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    #'''рисует новый шарик '''
    global x,y,r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def new_ball1():
    #'''рисует новый шарик '''
    global x1,y1,r1
    x1= randint(100, 1100)
    y1 = randint(100, 900)
    r1 = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x1, y1), r1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (((event.pos[0]-x)**2+(event.pos[1]-y)**2)<= r**2):
                count_popadaniy+=1
            if (((event.pos[0]-x1)**2+(event.pos[1]-y1)**2)<= r1**2):
                count_popadaniy+=1                     
    new_ball()
    new_ball1()
    pygame.display.update()
    screen.fill(BLACK)
print(count_popadaniy)

pygame.quit()
