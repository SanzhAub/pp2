import pygame as pg, os, random, sys
pg.init()

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200
SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

DINO_RUNNING = [pg.image.load("Materials\Dino\DinoRun1.png"),
                pg.image.load("Materials\Dino\DinoRun2.png")]
DINO_JUMPING = pg.image.load("Materials/Dino/DinoJump.png")
DINO_DUCKING = [pg.image.load("Materials/Dino/DinoDuck1.png"),
           pg.image.load("Materials/Dino/DinoDuck2.png")]
CLOUD = pg.image.load("Materials/Other/Cloud.png")
JOL = pg.image.load("Materials/Other/Track.png")
LUCKYBOX = pg.image.load("Materials\LuckyBox/1.png")
LUCKYBOX = pg.transform.scale(LUCKYBOX, (80, 80))
SMALL_CACTUS = [pg.image.load(os.path.join("Materials/Cactus", "SmallCactus1.png")),
                pg.image.load(os.path.join("Materials/Cactus", "SmallCactus2.png")),
                pg.image.load(os.path.join("Materials/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pg.image.load(os.path.join("Materials/Cactus", "LargeCactus1.png")),
                pg.image.load(os.path.join("Materials/Cactus", "LargeCactus2.png")),
                pg.image.load(os.path.join("Materials/Cactus", "LargeCactus3.png"))]

BIRD = [pg.image.load(os.path.join("Materials/Bird", "Bird1.png")),
        pg.image.load(os.path.join("Materials/Bird", "Bird2.png"))]
class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DINO_DUCKING
        self.run_img = DINO_RUNNING
        self.jump_img = DINO_JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pg.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pg.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pg.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))        
class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

class LuckyBox:
    def __init__(self):
        # self.x = random.randint(1000, 1600)
        # self.y = random.randint(100, 150)
        self.image = LUCKYBOX
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(500,800)
        self.rect.y = random.randint(100,150)
    def update(self,isCollide):
        self.rect.x -= game_speed
        if self.rect.x < 0 or isCollide == True:
            self.rect.x = SCREEN_WIDTH + random.randint(500,800)
            self.rect.y = random.randint(70, 150)
            isCollide = False
            Aluckybox = False
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y)) 
    

def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles,is2xscore,Aluckybox
    run = True
    clock = pg.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    luckybox = LuckyBox()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    EXL = 0
    font = pg.font.Font('freesansbold.ttf', 20)
    font2 = pg.font.Font('freesansbold.ttf', 100)
    obstacles = []
    is2xscore = False
    turboDino = False
    death_count = 0
    Aluckybox = False
    pg.time.set_timer(pg.USEREVENT + 1, 2500)
    pg.time.set_timer(pg.USEREVENT + 2, 5000)
    pg.time.set_timer(pg.USEREVENT + 3,10000)
    # pg.time.set_timer(pg.USEREVENT + 4,15000)
    # pg.time.set_timer(pg.USEREVENT + 5,20000)
    # pg.time.set_timer(pg.USEREVENT + 6,30000)
    def score():
        global points, game_speed
        if is2xscore == True:
            points += 2
        else:
            points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)
    def point():   
        text1 = font.render("EXTRA Lifes: " + str(EXL), True, (0, 0, 0))
        textRect = text1.get_rect()
        textRect.center = (1000, 60)
        SCREEN.blit(text1, textRect)
    def Team():   
        text1 = font2.render("Team 11. Tell4Hell", True, (0, 0, 0))
        textRect = text1.get_rect()
        textRect.center = (600, 600)
        SCREEN.blit(text1, textRect)
    def background():
        global x_pos_bg, y_pos_bg
        image_width = JOL.get_width()
        SCREEN.blit(JOL, (x_pos_bg, y_pos_bg))
        SCREEN.blit(JOL, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(JOL, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -=game_speed

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                sys.exit()
            elif event.type == pg.USEREVENT + 1:
                is2xscore = False
            elif event.type == pg.USEREVENT + 2 and turboDino:
                game_speed -= 20
            elif event.type == pg.USEREVENT + 3 and Aluckybox == False:
                Aluckybox = True

        SCREEN.fill((255, 255, 255))
        userInput = pg.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)
        if Aluckybox:
            luckybox.draw(SCREEN)
            luckybox.update(False)
        # print(death_count)
        # pg.draw.rect(SCREEN,(0,255,0),luckybox.rect)
        # # pg.draw.rect(SCREEN,(0,255,0),(1200,0,80,80))
        # pg.draw.rect(SCREEN,(255,0,0),player.dino_rect)
        if player.dino_rect.colliderect(luckybox.rect):
            print(player.dino_rect.colliderect(luckybox.rect))
            if random.randint(0,2) == 0:
                is2xscore = True
            elif random.randint(0,2) == 1:
                death_count -= 1
                EXL += 1
            elif random.randint(0,2) == 2:
                turboDino = True
                game_speed += 30
            luckybox.update(True)
            Aluckybox = False
            

        
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                # pg.time.delay(2000)
                death_count += 1
                EXL -=1
                if death_count > 0:
                    menu(death_count)
                obstacles.pop()

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()
        point()
        Team()
        clock.tick(30)
        pg.display.update()

def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pg.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(DINO_RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                main()
menu(death_count=0)