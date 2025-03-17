import pygame
import datetime

pygame.init()
pygame.display.set_caption("AIUclock")

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=(x, y))
    return rotated_image, new_rect


H, W = 700, 700
screen = pygame.display.set_mode((H, W))

mickey = pygame.image.load("clock.png")
hand_img = pygame.image.load("leftarm.png")  

mickey = pygame.transform.scale(mickey, (H, W))
hand_img = pygame.transform.scale(hand_img, (100, 550))  


minute_hand = hand_img.copy()
second_hand = hand_img.copy()

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    minute_angle = (-6 * now.minute) % 360
    second_angle = (-6 * now.second) % 360

    
    rotated_minute, minute_rect = rot_center(minute_hand, minute_angle, H / 2, W / 2)
    rotated_second, second_rect = rot_center(second_hand, second_angle, H / 2, W / 2)

    
    screen.blit(mickey, (0, 0))
    screen.blit(rotated_minute, minute_rect)
    screen.blit(rotated_second, second_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
