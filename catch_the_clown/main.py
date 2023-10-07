import pygame
import random

pygame.init()
WINWINDTH = 960
WINHEIGHT = 600

display_surface = pygame.display.set_mode((WINWINDTH, WINHEIGHT))
background = pygame.image.load("background.png")
background_rect = background.get_rect()
background_rect.topleft = (0, 0)

clown = pygame.image.load("clown.png")
clown_rect = clown.get_rect()
clown_rect.center = (WINWINDTH/2, WINHEIGHT/2)

dx = random.choice([-1, 1])
dy = random.choice([-1, 1])
clown_velocity = 5

score = 0
font = pygame.font.SysFont("arial", 30)
score_text = font.render(f"Score: {score}", True, (255, 0, 0))
score_rect = score_text.get_rect()
score_rect.topleft = (20, 0)

lives = 5
lives_text = font.render(f"Lives:{lives}", True, (255, 0, 0))
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINWINDTH, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if clown_rect.collidepoint(event.pos):
                score += 1
            else:
                lives -= 1

    if lives == 0:
        pause_text = font.render(
            f"Press Any key to continue..", True, (255, 0, 0))
        pause_rect = pause_text.get_rect()
        pause_rect.center = (WINWINDTH/2, WINHEIGHT/2)
        display_surface.blit(pause_text, pause_rect)
        lives_text = font.render(f"Lives:{lives}", True, (255, 0, 0))
        score_text = font.render(f"Score: {score}", True, (255, 0, 0))

        display_surface.blit(score_text, score_rect)
        display_surface.blit(lives_text, lives_rect)

        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    is_paused = False
                    score = 0
                    lives = 5
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    clown_rect.x += dx * clown_velocity
    clown_rect.y += dy * clown_velocity

    if clown_rect.left <= 0 or clown_rect.right >= WINWINDTH:
        dx = -1 * dx
    if clown_rect.top <= 0 or clown_rect.bottom >= WINHEIGHT:
        dy = -1 * dy
    lives_text = font.render(f"Lives:{lives}", True, (255, 0, 0))
    score_text = font.render(f"Score: {score}", True, (255, 0, 0))
    display_surface.blit(background, background_rect)
    display_surface.blit(clown, clown_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.display.update()

pygame.quit()
