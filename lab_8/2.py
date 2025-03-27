import pygame
import random

pygame.init()


width = 800
height = 600
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
green = (0, 255, 0)
red = (255, 0, 0)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game with Levels")
score = 0
level = 1
speed = 200  
fruit_eaten = False


head_square = [100, 100]
squares = [[30, 100], [40, 100], [50, 100], [60, 100], [70, 100], [80, 100], [90, 100], [100, 100]]
direction = "right"
next_dir = "right"

def check_wall_collision(head):
    if head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
        return True
    return False

def generate_food():
    while True:
        fr_x = random.randrange(1, width // 10) * 10
        fr_y = random.randrange(1, height // 10) * 10
        fruit_coor = [fr_x, fr_y]
        if fruit_coor not in squares: 
            return fruit_coor

fruit_coor = generate_food()

done = False
def game_over():
    global done
    font = pygame.font.SysFont("times new roman", 45)
    text = font.render(f"Game Over! Your score: {score}", True, gray)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.fill(black)
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    exit()
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
    for square in squares[:-1]:
        if head_square == square:
            game_over()
    if check_wall_collision(head_square):
        game_over()

    direction = next_dir

    
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


    if head_square == fruit_coor:
        fruit_eaten = True
        score += 10
    else:
        squares.pop(0) 

    if fruit_eaten:
        fruit_coor = generate_food()
        fruit_eaten = False
    if score % 30 == 0 and score > 0:
        level = score // 30 + 1
        speed = max(50, 200 - (level * 20)) 
    screen.fill(black)
    font = pygame.font.SysFont("times new roman", 20)
    score_surface = font.render(f"Score: {score}  Level: {level}", True, gray)
    screen.blit(score_surface, (20, 20))
    pygame.draw.circle(screen, green, (fruit_coor[0] + 5, fruit_coor[1] + 5), 5)


    for el in squares:
        pygame.draw.rect(screen, white, pygame.Rect(el[0], el[1], 10, 10))

    pygame.display.flip()
    pygame.time.delay(speed)

pygame.quit()
