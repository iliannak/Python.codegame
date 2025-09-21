import pygame
from pygame.locals import *

pygame.init()


screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Rocket Movement")

player = pygame.image.load("6.webp")
background = pygame.image.load("5.webp")

player_x = 200
player_y = 200
keys - [False,False,False,False,]


clock = pygame.time.Clock()

running = True
while player_y < 600 and running:
    screen.blit(background,(0,0))
    screen.blit(player,(player_x,player_y))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
