import pygame
import random
import time

# init
pygame.init()

# display
width, height = 800, 600
black, white, gray, green, red, blue = (0, 0, 0), (255, 255, 255), (128, 128, 128), (0, 255, 0), (255, 0, 0), (0, 0, 255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game with Levels and Timed Food")

score, level, speed = 0, 1, 200
fruit_eaten, done = False, False

# snake
head_square = [100, 100]
squares = [[30, 100], [40, 100], [50, 100], [60, 100], [70, 100], [80, 100], [90, 100], [100, 100]]
direction, next_dir = "right", "right"

# food
food_types = [
    {"color": green, "points": 10},
    {"color": red, "points": 20},
    {"color": blue, "points": 30}
]

# wall collision
def check_wall_collision(head):
    return head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height

# generating food
def generate_food():
    while True:
        fr_x = random.randrange(1, width // 10) * 10
        fr_y = random.randrange(1, height // 10) * 10
        food = random.choice(food_types)
        if [fr_x, fr_y] not in squares:
            return {"coord": [fr_x, fr_y], "color": food["color"], "points": food["points"], "spawn_time": time.time()}

fruit = generate_food()
food_timer = 10  # 10 sec

# game over
def game_over():
    global done
    font = pygame.font.SysFont("times new roman", 45)
    text = font.render(f"Game Over! Your score: {score}", True, gray)
    screen.fill(black)
    screen.blit(text, text.get_rect(center=(width // 2, height // 2)))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    exit()

# main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and direction != "up":
                next_dir = "down"
            if event.key == pygame.K_UP and direction != "down":
                next_dir = "up"
            if event.key == pygame.K_LEFT and direction != "right":
                next_dir = "left"
            if event.key == pygame.K_RIGHT and direction != "left":
                next_dir = "right"

    # check for self-collision
    for square in squares[:-1]:
        if head_square == square:
            game_over()
    if check_wall_collision(head_square):
        game_over()

    direction = next_dir

    # movement
    if direction == "right":
        head_square[0] += 10
    elif direction == "left":
        head_square[0] -= 10
    elif direction == "up":
        head_square[1] -= 10
    elif direction == "down":
        head_square[1] += 10

    new_square = [head_square[0], head_square[1]]
    squares.append(new_square)

    # food eaten
    if head_square == fruit["coord"]:
        fruit_eaten = True
        score += fruit["points"]
    else:
        squares.pop(0)

    # check food timer
    if time.time() - fruit["spawn_time"] > food_timer:
        fruit_eaten = True  # исчезает, создаётся новое

    if fruit_eaten:
        fruit = generate_food()
        fruit_eaten = False

    level = score // 30 + 1  # each level = 30 points
    speed = max(50, 200 - (level * 20))

    # render
    screen.fill(black)
    font = pygame.font.SysFont("times new roman", 20)
    score_surface = font.render(f"Score: {score}  Level: {level}", True, gray)
    screen.blit(score_surface, (20, 20))

    # draw food
    pygame.draw.circle(screen, fruit["color"], (fruit["coord"][0] + 5, fruit["coord"][1] + 5), 5)

    # draw snake
    for el in squares:
        pygame.draw.rect(screen, white, pygame.Rect(el[0], el[1], 10, 10))

    pygame.display.flip()
    pygame.time.delay(speed)

pygame.quit()
