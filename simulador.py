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
mapa_x = 0
velocidade = 10
tela = pygame.display.set_mode((1248, 600))
#pygame.draw.rect(mapa,(0,0,0),pos)
avatar_x = 600
avatar_y = 200
char = pygame.image.load('avatar2.png')
instruc = pygame.font.Font('freesansbold.ttf',32)
    
    
while True:
    
    tela.fill((0,0,0,))
    tela.blit(mapa,(mapa_x,0))
    tela.blit(char,(avatar_x,avatar_y))
    
    
    for event in pygame.event.get():
        
        
        if event.type == QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a:
                char = pygame.image.load('avatar3.png')
                avatar_x -= velocidade
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                char = pygame.image.load('avatar2.png')
                avatar_x += velocidade
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                char = pygame.image.load('avatar4.png')
                avatar_y -= velocidade
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                char = pygame.image.load('avatar.png')
                avatar_y += velocidade
        
        #if avatar_x >= 600 and mapa_x != -400:
            #mapa_x -= 10
        if avatar_x >= 1200:
            avatar_x = 1200
        
        #if avatar_x <= 10 and mapa_x != 0:
            #mapa_x += 10
        if avatar_x <= 0:
            avatar_x = 0
        
        if avatar_y <= 200 and avatar_x <= 600:
            avatar_y = 200
        
        if avatar_y >= 200 and avatar_x <= 600:
            avatar_y = 200
        
        if avatar_x >= 620 and avatar_x <=645 and avatar_y >= 150:
            avatar_x = 620
        
        if avatar_y >= 140 and avatar_y <= 180 and avatar_x <=645:
            avatar_y = 140
        
        
        #if avatar_x >= 500:
           #instrucim = instruc.render("piso defensoria",True,(255,255,255,))
            #tela.blit(instrucim, (20, 550))
    clock.tick(33)
    pygame.display.update()
