import pygame
import math

pygame.init()

#colours
w, h = 800, 600
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# size of brush
BRUSH_SIZE = 5
brush_color = black

# display
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Pygame Paint")
screen.fill(white)

# beginning sets
running = True
drawing = False
mode = "brush"
start_pos = None
#main code
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # mouse
                start_pos = event.pos
                drawing = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = event.pos

                if mode == "circle" and start_pos:
                    radius = int(math.dist(start_pos, end_pos))
                    pygame.draw.circle(screen, brush_color, start_pos, radius, 2)

                elif mode == "rect" and start_pos:
                    x, y = min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1])
                    width, height = abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])
                    pygame.draw.rect(screen, brush_color, (x, y, width, height), 2)
                
                elif mode == "square" and start_pos:
                    side = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, brush_color, (start_pos[0], start_pos[1], side, side), 2)
                
                elif mode == "right_triangle" and start_pos:
                    pygame.draw.polygon(screen, brush_color, [start_pos, (end_pos[0], start_pos[1]), end_pos], 2)
                
                elif mode == "equilateral_triangle" and start_pos:
                    side = abs(end_pos[0] - start_pos[0])
                    height = (math.sqrt(3) / 2) * side
                    pygame.draw.polygon(screen, brush_color, [start_pos, (start_pos[0] + side, start_pos[1]), (start_pos[0] + side / 2, start_pos[1] - height)], 2)
                
                elif mode == "rhombus" and start_pos:
                    dx = abs(end_pos[0] - start_pos[0]) // 2
                    dy = abs(end_pos[1] - start_pos[1]) // 2
                    pygame.draw.polygon(screen, brush_color, [(start_pos[0], start_pos[1] - dy), (start_pos[0] + dx, start_pos[1]), (start_pos[0], start_pos[1] + dy), (start_pos[0] - dx, start_pos[1])], 2)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                brush_color = red
            elif event.key == pygame.K_g:
                brush_color = green
            elif event.key == pygame.K_b:
                brush_color = blue
            elif event.key == pygame.K_w:
                brush_color = white
            elif event.key == pygame.K_o:
                mode = "circle"
            elif event.key == pygame.K_p:
                mode = "rect"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "right_triangle"
            elif event.key == pygame.K_e:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_m:
                mode = "rhombus"
            elif event.key == pygame.K_d:
                mode = "brush"

    if drawing and mode == "brush":
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), BRUSH_SIZE)

    pygame.display.update()

pygame.quit()