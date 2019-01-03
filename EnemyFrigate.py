import sys
import random
import math
import pygame
from pygame.locals import *
# Define some variables across al classes
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
red      = ( 255,   0,   0)
blue     = (   0,   0, 255)
WIDTH,  HEIGHT = 700, 750 
class EnemyFrigate(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('spshipspr1.gif').convert()
        self.image = pygame.transform.flip(self.image, False,True)
        self.rect = self.image.get_rect()
        self.rect.y = -20
        self.rect.x = random.randint(0,WIDTH-35)
        self.enemyhp = 3
        self.score = 10
        self.chanceForBullet = 0
    def update(self):
        """ Update the player's position. """
        self.rect.y += 3
        self.chanceForBullet =random.randint(1,50) 
            
class EnemySpeedster(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('speedster.gif').convert()
        self.image = pygame.transform.flip(self.image, False,True)
        self.rect = self.image.get_rect()
        self.rect.y = -25
        self.rect.x = random.randint(0,WIDTH-35)
        self.enemyhp = 1
        self.score = 20
        self.chanceForBullet = 0
    def update(self):
        """ Update the player's position. """
        self.rect.y += 6
class MinorCapShip(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('minorcapship.png').convert()
        self.image = pygame.transform.flip(self.image, False,True)
        self.rect = self.image.get_rect()
        self.rect.y = -30
        self.rect.x = random.randint(0,WIDTH-55)
        self.enemyhp = 10
        self.score = 100
        self.chanceForBullet = 0
    def update(self):
        """ Update the player's position. """
        self.chanceForBullet = random.randint(1,40)
        self.rect.y += 2
class CapitalShip(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('swarmer.gif').convert()
        self.image = pygame.transform.flip(self.image, False,True)
        self.rect = self.image.get_rect()
        self.rect.y = -200
        self.rect.x = random.randint(0,WIDTH-100)
        self.enemyhp = 20
        self.score = 500
        self.chanceForBullet = 0
    def update(self):
        """ Update the player's position. """
        self.chanceForBullet =random.randint(1,100)
        if(self.rect.y == 150):
            self.rect.y += 0
        else:
            self.rect.y += 1
        
