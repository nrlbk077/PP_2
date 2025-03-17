import pygame
pygame.init()
w = 800
h = 600
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Ball")

radius = 25
step = 5
x = w//2
y = h//2
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen,(255, 0, 0),(x,y),radius)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - step - radius >= 0:
        x -= step
    if keys[pygame.K_RIGHT] and x + step + radius <= w:
        x += step
    if keys[pygame.K_UP] and y - step - radius >= 0:
        y -= step
    if keys[pygame.K_DOWN] and y + step + radius <= h:
        y += step
    clock.tick(60)

pygame.quit()