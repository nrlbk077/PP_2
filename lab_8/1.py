

import pygame
from pygame.locals import *
import random

# initialize
pygame.init()

# display settings
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer with Coins")

# color
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

# game settings
speed = 2
score = 0
coin_score = 0
gameover = False

# size of road
marker_width = 10
marker_height = 50

# position of line in the road
road = (100, 0, 300, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

# line of drives
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]
lan_marker_move_y = 0

# coin load
coin_image = pygame.image.load("coin (2).png")

# for all cars
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (int(new_width), int(new_height)))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

# player
class Player_Vehicle(Vehicle):
    def __init__(self, x, y):
        image = pygame.image.load("car.png")
        super().__init__(image, x, y)

# coin
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(coin_image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

# creating player
player_x = 250
player_y = 400
player = Player_Vehicle(player_x, player_y)
player_group = pygame.sprite.Group()
player_group.add(player)

# loading cars
image_filenames = ['audi.png', 'Mini_truck.png', 'Mini_van.png', 'police.png', 'taxi.png']
vehicle_images = [pygame.image.load(img) for img in image_filenames]
vehicle_group = pygame.sprite.Group()

# group of coins
coin_group = pygame.sprite.Group()

# accident
crash = pygame.image.load('explosion2.png')
crash_rect = crash.get_rect()

# general loop
clock = pygame.time.Clock()
fps = 120
running = True

while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN and not gameover:
            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100

    # font
    screen.fill(green)
    pygame.draw.rect(screen, gray, road)
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)

    # moving
    lan_marker_move_y += speed * 2
    if lan_marker_move_y >= marker_height * 2:
        lan_marker_move_y = 0

    for y in range(-marker_height * 2, height, marker_height * 2):
        pygame.draw.rect(screen, white, (left_lane + 45, y + lan_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lan_marker_move_y, marker_width, marker_height))

    # random cars
    if len(vehicle_group) < 2:
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False
        if add_vehicle:
            lane = random.choice(lanes)
            image = random.choice(vehicle_images)
            vehicle = Vehicle(image, lane, height / -2)
            vehicle_group.add(vehicle)

    # random coins
    if len(coin_group) < 1 and random.randint(0, 100) < 2:
        lane = random.choice(lanes)
        coin = Coin(lane, -30)
        coin_group.add(coin)

    # move cars and scores
    for vehicle in vehicle_group:
        vehicle.rect.y += speed
        if vehicle.rect.top >= height:
            vehicle.kill()
            score += 1
            if score > 0 and score % 5 == 0:
                speed += 1

    # moving of coins
    for coin in coin_group:
        coin.rect.y += speed
        if coin.rect.top >= height:
            coin.kill()

    # checking 
    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True
        crash_rect.center = [player.rect.center[0], player.rect.top]

    # check
    coins_collected = pygame.sprite.spritecollide(player, coin_group, True)
    coin_score += len(coins_collected)

    player_group.draw(screen)
    vehicle_group.draw(screen)
    coin_group.draw(screen)
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    score_text = font.render('Score: ' + str(score), True, white)
    screen.blit(score_text, (20, 450))

    coin_text = font.render('Coins: ' + str(coin_score), True, yellow)
    screen.blit(coin_text, (430, 20))

    # massage 
    if gameover:
        screen.blit(crash, crash_rect)
        pygame.draw.rect(screen, red, (0, 50, width, 100))
        text = font.render('Game Over. Play again? (Y/N)', True, white)
        screen.blit(text, (width // 2 - 120, 100))

    pygame.display.update()

    # play again
    while gameover:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT:
                gameover = False
                running = False
            if event.type == KEYDOWN:
                if event.key == K_y:
                    gameover = False
                    speed = 2
                    score = 0
                    coin_score = 0
                    vehicle_group.empty()
                    coin_group.empty()
                    player.rect.center = [player_x, player_y]
                elif event.key == K_n:
                    gameover = False
                    running = False

pygame.quit()
