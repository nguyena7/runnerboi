import pygame
from player import Player
from obstacles import saw, spike
from pygame.locals import *
import sys
import math
import random

pygame.init()

size = width, height = 800, 447
screen = pygame.display.set_mode(size)

pygame.display.set_caption("JUMP!")
clock = pygame.time.Clock()

bg = pygame.image.load('images/bg.png')
bgX = 0
bgX2 = bg.get_width()

speed = 30
pygame.time.set_timer(USEREVENT + 1, 500)
pygame.time.set_timer(USEREVENT + 2, random.randrange(3000, 5000))

objects = []

pause = 0
fallSpeed = 0
score = 0

def redrawWindow():
    screen.blit(bg, (bgX, 0))
    screen.blit(bg, (bgX2, 0))
    for objt in objects:
        objt.draw(screen)
    runner.draw(screen)
    font = pygame.font.SysFont('comicsans', 30)
    text = font.render('Score: ' + str(score), 1, (255, 255, 255))
    screen.blit(text, (700, 10))
    pygame.display.update()

def endScreen():
    global pause, speed, score
    pause = 0
    speed = 30

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                runner.isFalling = False
                runner.jumping = False
                runner.sliding = False
        screen.blit(bg, (0, 0))
        largeFont = pygame.font.SysFont('comicsans', 80)
        newScore = largeFont.render("Score: " + str(score), 1, (255, 255, 255))
        screen.blit(newScore, (width / 2 - newScore.get_width() / 2, height / 2))
        pygame.display.update()
    score = 0

runner = Player(200, 313, 64, 64)

run = True
while run:
    score = speed // 5 - 6

    if pause > 0:
        pause += 1
        if pause > fallSpeed * 2:
            endScreen()

    for obstacle in objects:
        if obstacle.collide(runner.hitbox):
            runner.isFalling = True

            if pause == 0:
                fallSpeed = speed
                pause = 1

    for objt2 in objects:
        objt2.x -= 1.4
        if objt2.x < objt2.width * -1:
            objects.pop(objects.index(objt2))

    bgX -= 1.4
    bgX2 -= 1.4
    if bgX < bg.get_width() * -1: # if the background has moved left off the screen completely
        bgX = bg.get_width()      # reset
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == USEREVENT + 1: # Fix to eventually have constant FPS
            speed += 1
        if event.type == USEREVENT + 2:
            r = random.randrange(0, 2)
            if r == 0:
                objects.append(saw(810, 310, 64, 64))
            else:
                objects.append(spike(810, 0, 48, 320))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not runner.jumping:
            runner.jumping = True
    if keys[pygame.K_DOWN]:
        if not runner.sliding:
            runner.sliding = True

    clock.tick(speed)
    redrawWindow()


pygame.quit()
