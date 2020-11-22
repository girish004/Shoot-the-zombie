import pygame
from pygame.locals import *
pygame.init()
width, height = 1240, 620
screen=pygame.display.set_mode((width, height))
pos=[700,230]
player = pygame.image.load("D:\Girish\Project\Game\Resources\zombie.png")
grass = pygame.image.load("D:\Girish\Project\Game\Resources\grass.jpg")
player = pygame.transform.scale(player, (280, 220))
grass = pygame.transform.scale(grass, (1240, 620))
screen.blit(grass, (0,0))
while 1:
    # 5 - clear the screen before drawing it again
    # 6 - draw the screen elements
    screen.blit(player, pos)
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(1)
        if event.type == pygame.KEYDOWN:
            if event.key==K_DOWN:
                pos[1]=pos[1]+50
                screen.blit(grass, (0, 0))
                screen.blit(player, pos)
            if event.key==K_s:
                pos[1]=pos[1]+50
                screen.blit(grass, (0, 0))
                screen.blit(player, pos)
            if event.key==K_UP:
                pos[1]=pos[1]-50
                screen.blit(grass, (0, 0))
                screen.blit(player, pos)
            if event.key==K_w:
                pos[1]=pos[1]-50
                screen.blit(grass, (0, 0))
                screen.blit(player, pos)
            if event.key==K_a:
                pos[0]=pos[0]-50
                screen.blit(grass, (0, 0))
                screen.blit(player, pos)
            if event.key==K_LEFT:
                pos[0]=pos[0]-50
                screen.blit(grass, (0, 0))
                screen.blit(player, pos)
            if event.key==K_d:
                pos[0]=pos[0]+50
                screen.blit(grass, (0, 0))
                screen.blit(player, pos)
            if event.key==K_RIGHT:
                pos[0]=pos[0]+50
                screen.blit(grass, (0,0))
                screen.blit(player, pos)

