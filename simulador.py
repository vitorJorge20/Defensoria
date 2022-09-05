# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame
import pygame, sys
import random
import math
from pygame.locals import*
import time
import timeit
pygame.init()
clock = pygame.time.Clock()
sair = False
mapa = pygame.image.load("mapa.png")

tela = pygame.display.set_mode((800, 600))
#pygame.draw.rect(mapa,(0,0,0),pos)
avatar_x = 20
avatar_y = 20
char = pygame.image.load('avatar2.png')

    
    
while True:
    
    tela.blit(mapa,(0,0))
    tela.blit(char,(avatar_x,avatar_y))
    
    for event in pygame.event.get():
        
        tela.fill((250,250,250))
        if event.type == QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                avatar_x -= 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                avatar_x += 10
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                avatar_y -= 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                avatar_y += 10
            
    clock.tick(33)
    pygame.display.update()
