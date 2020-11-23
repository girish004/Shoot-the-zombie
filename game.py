import pygame
from pygame.locals import *
pygame.init()
def show(nature,grass):
    screen.blit(grass, (0, 0))
    screen.blit(nature, ((0, 0)))
    screen.blit(nature, ((0, 200)))
    screen.blit(nature, ((0, 400)))
width, height = 1240, 620
screen=pygame.display.set_mode((width, height))
pos=[250,0]
player = pygame.image.load("D:\Girish\Project\Game\Resources\zombie.png")
grass = pygame.image.load("D:\Girish\Project\Game\Resources\grass.jpg")
hero = pygame.image.load("D:\Girish\Project\Game\Resources\hero.png")
nature = pygame.image.load("D:\Girish\Project\Game\Resources\safe.png")
player = pygame.transform.scale(player, (180, 120))
grass = pygame.transform.scale(grass, (1240, 620))
hero = pygame.transform.scale(hero, (180, 120))
nature = pygame.transform.scale(nature, (180, 160))
show(nature,grass)
screen.blit(player,(750,300))
screen.blit(hero,(250,0))
while 1:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(1)
        if event.type == pygame.KEYDOWN:
            if event.key==K_DOWN or event.key==K_s:
                if(pos[1]+50<=620):
                    pos[1]=pos[1]+50
                show(nature,grass)
                screen.blit(hero, pos)
            if event.key==K_UP or event.key==K_w:
                if(pos[1]-50>=0):
                    pos[1]=pos[1]-50
                show(nature,grass)
                screen.blit(hero, pos)
            if event.key==K_a or event.key==K_LEFT:
                if(pos[0]-50>=250):
                    pos[0]=pos[0]-50
                show(nature,grass)
                screen.blit(hero, pos)
            if event.key==K_d or event.key==K_RIGHT:
                if(pos[0]+50<=1240):
                    pos[0]=pos[0]+50
                show(nature,grass)
                screen.blit(hero, pos)