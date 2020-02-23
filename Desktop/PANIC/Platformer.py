import pygame, sys
from pygame.locals import *
pygame.init()

WINDOW_SIZE = (1000, 600)
x = 500 
y = 300
#Setup Vars
moving_right = False
moving_left = False
moving_up = False
moving_down = False

#Story Line




screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
pygame.display.set_caption("Panic")
clock = pygame.time.Clock()
#Runtime
while(True):
    screen.fill((0,0,0))
    player_rect = pygame.draw.rect(screen, (255, 0, 0), (x,y, 50, 50))
    if moving_right == True:
        x += 6
    if moving_left == True:
        x -= 6
    if moving_up == True:
        y -= 6
    if moving_down == True:
        y += 6
    for event in pygame.event.get(): # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                moving_up = True
            if event.key == K_DOWN:
                moving_down = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
            if event.key == K_UP:
                moving_up = False
            if event.key == K_DOWN:
                moving_down = False
    clock.tick(60)
    pygame.display.update()