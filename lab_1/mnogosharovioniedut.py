import pygame
from pygame.draw import *
import random 
import math as mh
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

def new_balls():
    x0=100
    y0=100
    r0=30
    ux=1
    uy=1
    x01=300
    y01=500
    r01=25
    ux1=1
    uy1=-1
    while not finished:
            color0 = RED
            color1=YELLOW
            circle(screen, color0, (x0, y0), r0)
            circle(screen, color1, (x01, y01), r01)
            x0=x0+ux
            y0=y0+uy
            x01=x01+ux1
            y01=y01+uy1
            pygame.display.update()
            screen.fill(BLACK)
            if x0>1200:
                ux=-random.randint(30,100)*ux/(100*mh.fabs(ux))
            if y0>800:
                uy=-random.randint(30,100)*uy/(100*mh.fabs(uy))
            if x0<0:
                ux=-random.randint(30,100)*ux/(100*mh.fabs(ux))
            if y0<0:
                uy=-random.randint(30,100)*uy/(100*mh.fabs(uy))
            if x01>1200:
                ux1=-random.randint(30,100)*ux1/(100*mh.fabs(ux1))
            if y01>800:
                uy1=-random.randint(30,100)*uy1/(100*mh.fabs(uy1))
            if x01<0:
                ux1=-random.randint(30,100)*ux1/(100*mh.fabs(ux1))
            if y01<0:
                uy1=-random.randint(30,100)*uy1/(100*mh.fabs(uy1))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (((event.pos[0]-x0)**2+(event.pos[1]-y0)**2)<= r0**2):
                count_popadaniy+=1
            if (((event.pos[0]-x01)**2+(event.pos[1]-y01)**2)<= r01**2):
                count_popadaniy+=1                     
    new_balls()
print(count_popadaniy)

pygame.quit()
