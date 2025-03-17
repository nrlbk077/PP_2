import pygame
import os
pygame.init()

screen = pygame.display.set_mode((900,700))
pygame.display.set_caption("Music Player")

musics = ["Justin Bieber - Sorry.mp3","DJ Snake feat. Justin Bieber - Let Me Love You.mp3","Rompasso - Ignis.mp3","Rompasso - Angetenar (RJ_TOP Remix)..mp3"]
ind = 0

def to_play(index):
    pygame.mixer.music.load(musics[index])
    pygame.mixer.music.play()
    print("music is playing")

running  = True
is_playing  = False

while running:
    screen.fill((30,30,30))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_p:
                if not is_playing:
                    to_play(ind)
                    is_playing  = True

            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                print("stop")
                is_playing = False
            
            elif event.key == pygame.K_n:
                ind += 1
                to_play(ind)
                is_playing = True

            elif event.key == pygame.K_b:
                ind -=1
                to_play(ind)
                is_playing = True
pygame.quit()