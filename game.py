#text Rendering
#font = pygame.font.Font(None, 36)
#text = font.render("Hello There", 1, (10, 10, 10))
#textpos = text.get_rect()
#textpos.centerx = background.get_rect().centerx
#textpos.centery = background.get_rect().centery
#background.blit(text, textpos)
import os
import sys
import random
import math
import pygame
from pygame.locals import *
""" imports classes in same dir """
from EnemyFrigate import *

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
red      = ( 255,   0,   0)
blue     = (   0,   0, 255)
green  = (0,255,0)
WIDTH,  HEIGHT = 700, 750 
Score = 0
class Bullet(pygame.sprite.Sprite):
     def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self) 
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(white)
 
        self.rect = self.image.get_rect()
         
     def update(self):
        """ Move the bullet. """
        self.rect.y -= 7
class EnemyBullet(pygame.sprite.Sprite):
     def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self) 
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(white)
 
        self.rect = self.image.get_rect()
         
     def update(self):
        """ Move the bullet. """
        self.rect.y += 4
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
     
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load('Spaceship.gif').convert()
        
        self.rect = self.image.get_rect()
         
    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
class HealthPack(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('heart.gif').convert()
        self.image = pygame.transform.flip(self.image, False,False)
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(15,HEIGHT-20)
        self.rect.x = random.randint(0,WIDTH-24)    
    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.    
def main():
    FPS = 60
    FPSCLOCK = pygame.time.Clock()
    BCOLOR = (255,255,255)
#INTIALIZE screen
    pygame.init()
    
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    maxrange = 10000
    minrange = 1
    pygame.display.set_caption('Game')

# Fill Background
    background = pygame.Surface(screen.get_size())
    background = pygame.image.load('space.jpg').convert()
    b1 = 'space.jpg'
    back1 = pygame.image.load(b1).convert()
    back2 = pygame.image.load(b1).convert()
    y=0
    screenHEIGHT = HEIGHT
#  health bar
    MAXHPLENGTH = 150
    HPLength = MAXHPLENGTH
    MAXHEALTH = 10
    NUMOFHITS = MAXHEALTH
    HealthBar = pygame.Rect(0,HEIGHT-20,HPLength,20)
    pygame.draw.rect(screen,red,HealthBar,0)
    playing = True
    
# energy bar
    MAXENERGY = 250
    ELength = MAXENERGY
    EnergyBar = pygame.Rect(WIDTH-ELength,HEIGHT-20,ELength,20)
    pygame.draw.rect(screen,blue,EnergyBar,0)
    # This is a list of every sprite. All blocks and the player block as well.
    all_sprites_list = pygame.sprite.Group()
    bullet_list = pygame.sprite.Group()
    enemy_list = pygame.sprite.Group()
    player = Player()
    enemyBullet_list = pygame.sprite.Group()
    all_sprites_list.add(player)
    item_list = pygame.sprite.Group()
# Blit everything to the screen
    screen.blit(background,(0,0))
    Score = 0
    myfont = pygame.font.SysFont("monospace", 25)
    hptext = myfont.render("HP", 1, (255,30,30))
    Enetext = myfont.render("Energy", 1, (0,255,0))
    ScoreText = myfont.render(str(Score), 1, white)
    pygame.display.flip()
# construct variables
    leftheld = False
    rightheld = False
    upheld = False
    downheld = False
    dashheld = False
#draw image
    SPEED = 3
    player.rect.x = 400
    player.rect.y = 500
#sounds
    pygame.mixer.init()
    a_explosion = pygame.mixer.Sound(os.path.join("sounds", "asteroid_explosion.wav"))
    laser = pygame.mixer.Sound(os.path.join("sounds", "laser.wav"))
    soundtrack = pygame.mixer.Sound(os.path.join("sounds", "soundtrack.wav"))
    explosionImg = pygame.image.load('explosion.gif').convert()
  
    while playing==True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                playing=False
            if event.type==KEYUP and event.key == K_LEFT:
               leftheld = False
            if event.type==KEYDOWN and event.key == K_LEFT:
               leftheld = True
            if event.type==KEYUP and event.key == K_RIGHT:
               rightheld = False
            if event.type==KEYDOWN and event.key == K_RIGHT:
               rightheld = True
            if event.type==KEYUP and event.key == K_UP:
               upheld = False
            if event.type==KEYDOWN and event.key == K_UP:
               upheld = True
            if event.type==KEYUP and event.key == K_DOWN:
               downheld = False
            if event.type==KEYDOWN and event.key == K_DOWN:
               downheld = True
            if event.type==KEYUP and event.key == K_z:
               dashheld = False   
            if event.type==KEYDOWN and event.key == K_z:
               dashheld = True
            if event.type==KEYDOWN and event.key == K_SPACE:
            
            # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
            # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.centerx
                bullet.rect.y = player.rect.y
            # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                laser.play()
                 
        #upate States of objects - player
        if (rightheld and player.rect.x < WIDTH-40):
           if(dashheld and ELength > 1):
               player.rect.x +=6     
               ELength -= 1
           else:
                player.rect.x +=4
        if (leftheld and  player.rect.x > -10):
            if(dashheld and ELength > 1):
               player.rect.x -=6
               ELength -= 1
            else:
               player.rect.x -=4
        if (upheld and player.rect.y  > 10):
            if(dashheld and ELength > 1):
               player.rect.y -=6
               ELength -= 1
            else:
               player.rect.y -=4
        if (downheld and player.rect.y < HEIGHT-40):
            if(dashheld and ELength > 1):
               player.rect.y +=6
               ELength -= 1
            else:
               player.rect.y +=4
        all_sprites_list.update()
        for bullet in bullet_list:
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
            for enemy in enemy_list:
               dx = enemy.rect.centerx - bullet.rect.centerx
               dy = enemy.rect.y - bullet.rect.centery
               distance=math.sqrt(dx**2+dy**2)
               if(distance <= 30):
                    if (enemy.enemyhp == 0):
                         a_explosion.play()
                         enemy_list.remove(enemy)
                         all_sprites_list.remove(enemy)
                         bullet_list.remove(bullet)
                         all_sprites_list.remove(bullet)
                         Score += enemy.score
                    else:
                         enemy.enemyhp -=1
                         bullet_list.remove(bullet)
                         all_sprites_list.remove(bullet)
        #UPDATE ene BAR STATUS 
        if not dashheld and ELength <= MAXENERGY:
          ELength+=1
        EnergyBar = pygame.Rect(WIDTH-ELength,HEIGHT-20,ELength,20)
        
        ##ENEMY HANDLing minrange = 1, max  = 1000 
        spawned = False
        cValue = random.randint(minrange,maxrange)
        
        if(random.randint(minrange,maxrange) < 10):
            enemy = EnemyFrigate()
            enemy_list.add(enemy)
            all_sprites_list.add(enemy)
            spawned = True
        if(random.randint(0,10000) < 50 and not spawned):
            enemy = EnemySpeedster()
            enemy_list.add(enemy)
            all_sprites_list.add(enemy)
            spawned = True   
        if(random.randint(0,25000) < 35):
              enemy = MinorCapShip()
              enemy_list.add(enemy)
              all_sprites_list.add(enemy)
              spawned = True    
        if(random.randint(0,25000) < 10):
              enemy = CapitalShip()
              enemy_list.add(enemy)
              all_sprites_list.add(enemy)
              spawned = True 
        if(random.randint(0,20000) < 10):
              health = HealthPack()
              all_sprites_list.add(health)
              item_list.add(health)
        for health in item_list:
              dx = health.rect.centerx - player.rect.centerx
              dy = health.rect.y - player.rect.y
              distance=math.sqrt(dx**2+dy**2)
              if(distance <= 25):
                    if NUMOFHITS+3 <= MAXHEALTH:
                         NUMOFHITS += 3
                         HPLength += MAXHPLENGTH/NUMOFHITS
                    all_sprites_list.remove(health)
                    item_list.remove(health)
        for enemy in enemy_list:
             if(enemy.chanceForBullet == 10):
                   ebullet = EnemyBullet()
                   enemyBullet_list.add(ebullet)
                   all_sprites_list.add(ebullet)               
                   ebullet.rect.x = enemy.rect.centerx
                   ebullet.rect.y = enemy.rect.y
             dxCollision = enemy.rect.centerx - player.rect.centerx
             dyCollision = enemy.rect.y - player.rect.centery
             Pdistance=math.sqrt(dxCollision**2+dyCollision**2)
             if(Pdistance <= 30):
                    a_explosion.play()
                    enemy_list.remove(enemy)
                    all_sprites_list.remove(enemy)
                    ##Damage script
                    if(NUMOFHITS > 1):
                         HPLength -= HPLength/NUMOFHITS
                    else:
                         HPLength = 0
                    NUMOFHITS-=1
             if enemy.rect.y > HEIGHT:
                    enemy_list.remove(enemy)
                    all_sprites_list.remove(enemy)
             for ebullet in enemyBullet_list:
                    if (ebullet.rect.y < 0):
                         enemyBullet_list.remove(ebullet)
                         all_sprites_list.remove(ebullet)
                    dxbullet = ebullet.rect.centerx - player.rect.centerx
                    dybullet = ebullet.rect.y - player.rect.centery
                    Edistance=math.sqrt(dxbullet**2+dybullet**2)
                    if(Edistance <= 30):
                         a_explosion.play()
                         enemyBullet_list.remove(ebullet)
                         all_sprites_list.remove(ebullet)
                         ##Damage script
                         if(NUMOFHITS > 1):
                              HPLength -= HPLength/NUMOFHITS
                         else:
                              HPLength = 0
                         NUMOFHITS-=1 
                         
        HealthBar = pygame.Rect(0,HEIGHT-20,HPLength,20) 
        #blit the screen
        
        screen.blit(back1,(0,y))
        screen.blit(back1,(0,y-HEIGHT))
        screen.blit(hptext, (0,HEIGHT-50))
        screen.blit(Enetext, (WIDTH-ELength,HEIGHT-50))
        ScoreText = myfont.render(str(Score), 1, white)
        screen.blit(ScoreText, (0,0))
        if(player.rect.y < HEIGHT-70 or player.rect.x >HPLength):
            pygame.draw.rect(screen,red,HealthBar)
        pygame.draw.rect(screen,green,EnergyBar,0)
        y = y + 1
        if y == HEIGHT:
            y = 0
       #check for game over condition
        if(NUMOFHITS == 0):
             playing = False

        # Draw all the spites
        all_sprites_list.draw(screen)

        pygame.display.flip()
        FPSCLOCK.tick(FPS)
        if maxrange > 700:
             maxrange -= 1
if __name__ == '__main__':
    main()
    print "You have failed your mission!"
    print str(Score)
    pygame.quit()
    sys.exit()
     

