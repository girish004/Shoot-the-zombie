import pygame
from pygame.locals import *
import time
import random
pygame.init()
def show(nature, grass, count):
    green = (0, 255, 0)
    blue = (0, 0, 128)
    screen.blit(grass, (0, 0))
    screen.blit(nature, (0, 0))
    screen.blit(nature, (0, 200))
    screen.blit(nature, (0, 400))
    font = pygame.font.SysFont('freesansbold.ttf', 32)
    score = font.render("Score: "+str(count),True,green,blue)
    screen.blit(score,(1000,0))
    t = font.render("Time:" + str(60 - (int(time.time()) - starttimer)), True, green, blue)
    screen.blit(t, (1000, 20))
start_time=int(time.time())
c=int(time.time())
d=int(time.time())
width, height = 1240, 620
screen=pygame.display.set_mode((width, height))
pos=[250,0]
enemypos=[]
timeline=[]
green = (0, 255, 0)
blue = (0, 0, 128)
white = (255, 255, 255)
player = pygame.image.load("Resources\zombie.png")
grass = pygame.image.load("Resources\grass.jpg")
hero = pygame.image.load("Resources\hero.png").convert_alpha()
nature = pygame.image.load("Resources\safe.png")
bullet = pygame.image.load("Resources\Bullet.png")
pygame.display.set_caption('Zombie apocalypse')
font = pygame.font.SysFont('freesansbold.ttf', 32)
text=font.render("Zombie apocalypse",True,blue,green)
textRect = text.get_rect()
player = pygame.transform.scale(player, (180, 120))
grass = pygame.transform.scale(grass, (1240, 620))
hero = pygame.transform.scale(hero, (180, 120))
nature = pygame.transform.scale(nature, (180, 160))
bullet = pygame.transform.scale(bullet, (80, 20))
naturerect=pygame.Rect(nature.get_rect())
badrect = pygame.Rect(hero.get_rect())
zombrect=pygame.Rect(player.get_rect())
startgame=font.render("Click to start the game", True, (100,100,100), (200,200,200))
instructions1=font.render("1. A total of 60 seconds will be given",True,blue,green)
instructions2=font.render("2. Try and kill as many zombies as you can within the given time",True,blue,green)
instructions3=font.render("3. You will be considered as out of the game when a zombie reaches a tree",True,blue,green)
instructions4=font.render("4. Move the shooter using the up and down arrow keys :)",True,blue,green)
instructions5=font.render("5. Shoot the zombies using the space button:)",True,blue,green)
instructions6=font.render("6. Have fun with the easy game play :)",True,blue,green)
bla=0
while 1:
    screen.blit(hero,(300,150))
    screen.blit(player,(700,150))
    screen.blit(text,(500,250))
    screen.blit(startgame,(495,300))
    screen.blit(instructions1,(380,325))
    screen.blit(instructions2,(380,350))
    screen.blit(instructions3,(380,375))
    screen.blit(instructions4,(380,400))
    screen.blit(instructions5, (380, 425))
    screen.blit(instructions6, (380, 450))
    startrect = pygame.Rect(startgame.get_rect())
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(1)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 495<= mouse[0] <=495+startrect[2]  and 300<= mouse[1] <=300+startrect[3]:
                bla=1
    if bla==1: break

while 1:
    go=0
    bla=0
    count = 0
    starttimer = int(time.time())
    start_time = int(time.time())
    show(nature, grass, count)
    screen.blit(hero, (250, 0))
    while (int(time.time())-start_time)<=60:
        pygame.display.flip()
        if((int(time.time())-start_time)%1==0 and c!=int(time.time())):
            enemypos.append([1100,random.randint(0,520)])
            a=int(time.time())
            timeline.append(a)
            c=int(time.time())
        show(nature, grass,count)
        screen.blit(hero, pos)
        for i in range(len(enemypos)):
            if((int(time.time())-timeline[i])%1==0 and d!=int(time.time())):
                enemypos[i][0]=enemypos[i][0]-40
            if(i==len(enemypos)-1):
                d = int(time.time())
            screen.blit(player, enemypos[i])
            if (enemypos[i][0] <= naturerect[2]):
                bla = 1
                break
        if(bla==1): break
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(1)
            if event.type == pygame.KEYDOWN:
                if event.key==K_DOWN or event.key==K_s:
                    if(pos[1]+50<=620):
                        pos[1]=pos[1]+50
                    show(nature,grass,count)
                    screen.blit(hero, pos)
                if event.key==K_UP or event.key==K_w:
                    if(pos[1]-50>=0):
                        pos[1]=pos[1]-50
                    show(nature,grass,count)
                    screen.blit(hero, pos)
                if event.key==K_SPACE:
                    for i in range(len(enemypos)):
                        if((badrect[3]//2)+pos[1]>=enemypos[i][1] and (badrect[3]//2)+pos[1]<=enemypos[i][1]+zombrect[3]):
                            screen.blit(bullet,(pos[0]+badrect[2]+40,badrect[3]//2+pos[1]))
                            screen.blit(player,enemypos[i])
                            enemypos.pop(i)
                            timeline.pop(i)
                            count+=1
                            break
    while 1:
        if(bla==1):
            pygame.draw.rect(screen, (128,0,0), pygame.Rect(0, 0, 1250, 620))
            over = font.render("Oops... you failed to save the trees!!!", True, (100, 100, 100), (200, 200, 200))
            screen.blit(over,(425,300))
            score = font.render("Your score:"+str(count),True,(100, 100, 100), (200, 200, 200))
            screen.blit(score,(pygame.Rect(over.get_rect())[3]+500,350))
            screen.blit(nature, (300, 135))
            screen.blit(player, (700, 150))
            restart=font.render("Click to restart",True,green,blue)
            screen.blit(restart,(Rect(score.get_rect())[3]+490,400))
            againrect=pygame.Rect(restart.get_rect())
            pygame.display.flip()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if 490<= mouse[0] <=490+againrect[2]  and 400<= mouse[1] <=400+againrect[3]:
                        go=1
            if go==1:
                enemypos.clear()
                timeline.clear()
                break
        else:
            pygame.draw.rect(screen, (0,100,0), pygame.Rect(0, 0, 1250, 620))
            over = font.render("You saved the trees from zombies..success!!!", True, (100, 100, 100), (200, 200, 200))
            screen.blit(over,(375,300))
            score = font.render("Your score:"+str(count),True,(100, 100, 100), (200, 200, 200))
            screen.blit(score,(pygame.Rect(over.get_rect())[3]+500,350))
            screen.blit(hero, (300, 150))
            screen.blit(player, (700, 150))
            restart=font.render("Click to restart",True,green,blue)
            screen.blit(restart,(Rect(score.get_rect())[3]+490,400))
            againrect=pygame.Rect(restart.get_rect())
            pygame.display.flip()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit(1)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if 490<= mouse[0] <=490+againrect[2]  and 400<= mouse[1] <=400+againrect[3]:
                        go=1
            if go==1:
                enemypos.clear()
                timeline.clear()
                break