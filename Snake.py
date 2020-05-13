import pygame
import random
import tkinter as tk
from pygame.locals import *
from tkinter import messagebox

Width = 625
Height = 625
score = 0
foodeaten = 1
#box = 25
BLACK = (0, 0, 0)
SNAKE = (0, 70, 0)
SNAKE_HEAD = (0, 50, 0)
running = True
win = pygame.display.set_mode((Width, Height))
fps = pygame.time.Clock()
key = "S"
newkey = "S"
body = [(50, 50)]
newX = 50
newY = 50
fruit = pygame.image.load("Images/apple.png")
background = pygame.image.load("Images/background.png")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                newkey = "D"
            if event.key == pygame.K_UP:
                newkey = "U"
            if event.key == pygame.K_RIGHT:
                newkey = "R"
            if event.key == pygame.K_LEFT:
                newkey = "L"
    
    direction = True
    if newkey == "R" and key == "L":
        direction = False
    if newkey == "L" and key == "R":
        direction = False
    if newkey == "U" and key == "D":
        direction = False
    if newkey == "D" and key == "U":
        direction = False
    
    if direction == True:
        if newkey == "R":
            newX += 25
        if newkey == "L":
            newX -= 25
        if newkey == "U":
            newY -= 25
        if newkey == "D":
            newY += 25
        key = newkey
    else:
        if key == "R":
            newX += 25
        if key == "L":
            newX -= 25
        if key == "U":
            newY -= 25
        if key == "D":
            newY += 25
    
    if newX < 0 or newX > 600 or newY < 0 or newY > 600:
        running = False
    for i in body[1:]:
        if i[0] == body[0][0] and i[1] == body[0][1]:
            running = False
    body.insert(0, (newX, newY))
    if foodeaten == 1:
        foodx = random.randrange(1, 20) * 25
        foody = random.randrange(1, 20) * 25
        foodeaten = 0

    if(newX == foodx and newY == foody):
        score += 10
        foodeaten = 1
    else:   
        body.pop()
    win.blit(background, (0,0))
    #Border
    for i in range(25):
        pygame.draw.line(win, (105,105,105), (i*25, 0), (i*25, 625), 1)
        pygame.draw.line(win, (105,105,105), (0, i*25), (625, i*25), 1)
    pygame.draw.rect(win,SNAKE_HEAD,(body[0][0], body[0][1],25,25))
    for i in body[1:]:
        pygame.draw.rect(win,SNAKE,(i[0],i[1],25,25))
    win.blit(fruit,(foodx,foody,25,25))
    
    pygame.display.flip()   
    pygame.display.set_caption("Snake Score = " + str(score))
    fps.tick(18)
    answer = 'no'
    root = tk.Tk()
    root.withdraw()
    if running == False:
        answer = tk.messagebox.askquestion("Snake","Vrei sa continui jocul?")
    if answer == 'yes':
        running = True
        key = "S"
        newkey = "S"
        body = [(50, 50)]
        newX = 50
        newY = 50   
        score = 0    
