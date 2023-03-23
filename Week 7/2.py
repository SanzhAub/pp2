import pygame
pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Music Player")

pygame.mixer.music.load("mp3/your_music_file.mp3")
pygame.mixer.music.set_volume(0.5)

font = pygame.font.Font(None, 36)

play_text = font.render("Press P to play", True, WHITE)
stop_text = font.render("Press S to stop", True, WHITE)
next_text = font.render("Press N for next", True, WHITE)
prev_text = font.render("Press B for previous", True, WHITE)

status = "stopped"

done = False

while not done:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if status == "stopped":
                    pygame.mixer.music.play()
                    status = "playing"
            elif event.key == pygame.K_s:                
                if status == "playing":
                    pygame.mixer.music.stop()
                    status = "stopped"
            elif event.key == pygame.K_n:               
                pygame.mixer.music.stop()
                pygame.mixer.music.load("mp3/your_next_music_file.mp3")
                pygame.mixer.music.play()
                status = "playing"
            elif event.key == pygame.K_b:             
                pygame.mixer.music.stop()
                pygame.mixer.music.load("mp3/your_previous_music_file.mp3")
                pygame.mixer.music.play()
                status = "playing"

    
    screen.fill(BLACK)
    if status == "stopped":
        screen.blit(play_text, [50, 50])
    elif status == "playing":
        screen.blit(stop_text, [50, 50])
        screen.blit(next_text, [50, 100])
        screen.blit(prev_text, [50, 150])

   
    pygame.display.flip()


pygame.quit()
