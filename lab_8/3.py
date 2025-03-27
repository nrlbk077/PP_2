import pygame
pygame.init()
w, h = 800, 600
white = (255, 255, 255)

BRUSH_SIZE = 5  
brush_color = (0, 0, 0) 

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Pygame Paint")

running = True
drawing = False  
mode = "brush"  
start_pos = None  
screen.fill(white) 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

      
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                start_pos = event.pos
                drawing = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = event.pos

                
                if mode == "circle" and start_pos:
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, brush_color, start_pos, radius, 2)

               
                elif mode == "rect" and start_pos:
                    x, y = min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1])
                    width, height = abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])
                    pygame.draw.rect(screen, brush_color, (x, y, width, height), 2)

        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  
                brush_color = (255, 0, 0)
            elif event.key == pygame.K_g:  
                brush_color = (0, 255, 0)
            elif event.key == pygame.K_b:  
                brush_color = (0, 0, 255)
            elif event.key == pygame.K_w:  
                brush_color = white
            elif event.key == pygame.K_o:  
                mode = "circle"
            elif event.key == pygame.K_p:  
                mode = "rect"
            elif event.key == pygame.K_d: 
                mode = "brush"

    if drawing and mode == "brush":
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), BRUSH_SIZE)

    pygame.display.update()

pygame.quit()
