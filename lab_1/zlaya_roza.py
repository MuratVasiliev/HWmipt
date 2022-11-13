import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (0, 255, 255), (200, 175), 80)
circle(screen, (255, 0, 0), (170, 150), 20)
circle(screen, (255, 0, 0), (230, 150), 20)
circle(screen, (0, 0, 0), (230, 150), 10)
circle(screen, (0, 0, 0), (170, 150), 10)
rect(screen, (0, 0, 0), (170, 210, 60, 10))
line(screen, (0,0,0), (160, 105), (195, 130), 10)
line(screen, (0,0,0), (210, 130), (255, 105), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()