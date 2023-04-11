import pygame, sys
from pygame.locals import *
import random, time
#Initialization
pygame.init()
#Setting of FPS
FPS = 60
FramePerSec = pygame.time.Clock()
#Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#Some variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEEDENEMY = 5
SPEEDCOIN = 6
SPEEDCOIN2 = 5
SCORE = 0
NUMBERCOIN = 0
#Font Settings
font = pygame.font.Font('mp3/g.otf', 90)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load("images/AnimatedStreet.png")
#Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
# Setting Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) #point of occurence

    def move(self):
        #Score
        global SCORE
        #moves the rectangle into place
        self.rect.move_ip(0, SPEEDENEMY)
        if (self.rect.bottom > 600):
            SCORE += 1
            #random spawn of enemy
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
#Setting Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) #spawn
    def move(self):
        #moves on right, left
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
# Setting Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)#spawn
        self.state = False

    def move(self):
        #SPEEDCOIN
        global SPEEDCOIN
        #moves the rectangle into place
        self.rect.move_ip(0, SPEEDCOIN)
        if (self.rect.bottom > 600 or self.state):
            SPEEDCOIN = 6
            self.state = False
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/coin2.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 60), 0)#spawn
        self.state = False

    def move(self):
        #SPEEDCOIN
        global SPEEDCOIN2
        self.rect.move_ip(0, SPEEDCOIN2)
        #appearance of coin
        if (self.rect.bottom > 600 or self.state):
            SPEEDCOIN2 = 5
            self.state = False
            self.rect.top = 0
            self.rect.center = (random.randint(20, SCREEN_WIDTH - 60), 0)
# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin2()
# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
coins2 = pygame.sprite.Group()
coins2.add(C2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)
#Game loop
while True:
    #Cyclic passage of all the events taking place
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #superimpose one image on another
    DISPLAYSURF.blit(background, (0, 0))
    #container for storing and managing multiple Sprite objects
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    collect = font_small.render(str(NUMBERCOIN), True, BLACK)
    DISPLAYSURF.blit(collect, (SCREEN_WIDTH - 30, 10))
    #Moves and redraws all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    #It is executed if there is a collision between the player and the opponent
    if pygame.sprite.spritecollideany(P1, enemies):
        #A simple check to see if the sprite intersects anything in the group.
        pygame.mixer.Sound('mp3/crash.wav').play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        pygame.mixer.Sound('mp3/gameover.mp3').play()
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
            #remove sprite from all groups
        time.sleep(4)
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(P1, coins):
        NUMBERCOIN += 1
        SPEEDENEMY += 1
        for entity in coins:
            entity.state = True
    if pygame.sprite.spritecollideany(P1, coins2):
        NUMBERCOIN += 10
        for entity in coins2:
            entity.state = True
    pygame.display.update()
    FramePerSec.tick(FPS)