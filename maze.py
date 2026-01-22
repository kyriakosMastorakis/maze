import pygame
import time
import threading
from pygame.examples.cursors import image

pygame.init()

screen = pygame.display.set_mode((800,800))

p1 = "player1.jpg"
p2 = "player2.png"
surf1 = pygame.image.load(p1).convert_alpha()
surf1small = pygame.transform.smoothscale(surf1, (70,50))
surf2 = pygame.image.load(p2).convert_alpha()
surf2small = pygame.transform.smoothscale(surf2, (70,50))



done = False
clock = pygame.time.Clock()
duration1 = 0
duration2 = 0
startTime1= time.time()
startTime2= time.time()
endTime1= time.time()
endTime2= time.time()
x=40
y=50
speed=0.2
speed2=0.2
oldx = x
oldy = y

x2 = 50
y2 = 30
oldx2 = x2
oldy2 = y2

partWidth8 = 300
partHeight8 = 200

partWidth9 = 300
partHeight9 = 300

def resize():
    global partWidth8, partHeight8
    while True:
        for i in range(100):
            partWidth8 += 1
            time.sleep(0.01)
        time.sleep(3)
        for i in range(100):
            partWidth8 -= 1
            time.sleep(0.01)
        time.sleep(3)



resize_thread = threading.Thread(target=resize)
resize_thread.start()
resize_thread.deamon = True

def resize():
    global partWidth9, partHeight9
    while True:
        for i in range(100):
            partHeight9 += 1
            time.sleep(0.01)
        time.sleep(3)
        for i in range(100):
            partHeight9 -= 1
            time.sleep(0.01)
        time.sleep(3)


resize_thread = threading.Thread(target=resize)
resize_thread.start()
resize_thread.deamon = True

partWidth1 = 130
partHeight1 = 0

def move():
    global partWidth1, partHeight1
    while True:
        for i in range(100):
            partWidth1 += 1
            time.sleep(0.01)
        time.sleep(3)
        for i in range(100):
            partWidth1 -= 1
            time.sleep(0.01)
        time.sleep(4)


resize_thread = threading.Thread(target=move)
resize_thread.start()
resize_thread.deamon = True



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((150,0,0))

    player1 = surf1small.get_rect(topleft=(x,y))
    screen.blit(surf1small,(x,y))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed



    player2 = surf2small.get_rect(topleft=(x2,y2))
    screen.blit(surf2small,(x2,y2))
    keys2 = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x2 -= speed
    if keys[pygame.K_d]:
        x2 += speed
    if keys[pygame.K_w]:
        y2 -= speed
    if keys[pygame.K_s]:
        y2 += speed

    wall1 = pygame.draw.rect(screen,(0,0,0),(0,0,800,40))       # πανω τοιχος
    wall2 = pygame.draw.rect(screen,(0,0,0),(0,760,800,40))     # κατω τοιχος
    wall3= pygame.draw.rect(screen,(0,0,0),(0,0,40,800))        # αριστερα τοιχος
    wall4 = pygame.draw.rect(screen,(0,0,0),(760,0,40,800))     # δεξια τοιχος


    if player1.colliderect(wall1):y += 15
    if player1.colliderect(wall2):y -= 15
    if player1.colliderect(wall3):x += 15
    if player1.colliderect(wall4):x -= 15

    if player2.colliderect(wall1): y2 += 15
    if player2.colliderect(wall2): y2 -= 15
    if player2.colliderect(wall3): x2 += 15
    if player2.colliderect(wall4): x2 -= 15

    wall5 = pygame.draw.rect(screen,(0,0,0),(partWidth1,partHeight1,30,330)) #130 0
    wall6 = pygame.draw.rect(screen,(0,0,0),(40,430,290,30))
    wall8 = pygame.draw.rect(screen,(0,0,0),(partWidth8,partHeight8,30,330)) #zxcvb x=300 y=200
    wall9 = pygame.draw.rect(screen,(0,0,0),(partWidth9,partHeight9,350,30)) #rhhdty 300
    wall10 = pygame.draw.rect(screen,(0,0,0),(450,150,350,30))
    wall11 = pygame.draw.rect(screen,(0,0,0),(450,500,350,30))
    wall12 = pygame.draw.rect(screen,(0,0,0),(450,500,30,150))
    wall13 = pygame.draw.rect(screen,(0,0,0),(150,620,300,30))

    finish = pygame.draw.rect(screen, (128,128,128), (700,700 , 50, 50))


    walls = [wall5,wall6,wall8,wall9,wall10,wall10,wall11,wall12,wall13]

    for i in walls:
        if player1.colliderect(i):
            x = oldx
            y = oldy

    for i in walls:
        if player2.colliderect(i):
            x2 = oldx2
            y2 = oldy2

    if player1.colliderect(finish):
        x = oldx
        y = oldy
        endTime1 = time.time()
        duration1 = round(endTime1 - startTime1, 2)
        startTime1 = time.time()

    if player2.colliderect(finish):
        x2 = oldx2
        y2 = oldy2
        endTime2 = time.time()
        duration2 = round(endTime2 - startTime2, 2)
        startTime2 = time.time()

    Font = pygame.font.SysFont("comicsansms", 30,True, False)
    gametitle = Font.render("MAZE PYGAME", True, (255,255,255))
    screen.blit(gametitle,(40,0))


    Font = pygame.font.SysFont("comicsansms", 30,True, True)
    timerA = Font.render("timer1:"+str(duration1), True, (255,255,255))
    screen.blit(timerA,(300,0))

    Font = pygame.font.SysFont("comicsansms", 30,True, True)
    timerB = Font.render("timer2:"+str(duration2), True, (255,255,255))
    screen.blit(timerB,(600,0))





    pygame.display.flip()
pygame.quit()
clock.tick()



