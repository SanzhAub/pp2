import pygame

pygame.init()

W, H = 800, 800
sc=pygame.display.set_mode((800, 800))

WHITE=(255, 255, 255)
RED=(255, 0, 0)

FPS=60
clock=pygame.time.Clock()

x= W//2
y=H//2
speed=20
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP] and y > 0: y -= speed
    if pressed[pygame.K_DOWN] and y < 800 - 25: y += speed
    if pressed[pygame.K_LEFT] and x > 0: x -= speed
    if pressed[pygame.K_RIGHT] and x < 800 - 35: x += speed

    sc.fill(WHITE)
    pygame.draw.circle(sc, RED, (x, y), 25)
    pygame.display.update()

    clock.tick(FPS)




