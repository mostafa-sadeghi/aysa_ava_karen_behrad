import pygame
import random
pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

lives = 3
score = 0

clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dragon game")

dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_image = pygame.transform.scale(dragon_left_image, (64, 64))


dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right_image = pygame.transform.flip(dragon_left_image, True, False)
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)

player_image = dragon_right_image
player_rect = player_image.get_rect()
player_rect.x = 20
player_rect.y = WINDOW_HEIGHT/2 - 32

egg_image = pygame.image.load("egg.png")
egg_rect = egg_image.get_rect()
egg_rect.center = (WINDOW_WIDTH + 100, random.randint(100, WINDOW_HEIGHT-100))

font = pygame.font.SysFont("Arial", 32)


lives_text = font.render(f"Lives:{lives}", True, (255, 0, 0))
lives_rect = lives_text.get_rect()
lives_rect.topleft = (WINDOW_WIDTH/2 - 200, 10)

score_text = font.render(f"score:{score}", True, (255, 0, 0))
score_rect = score_text.get_rect()
score_rect.topleft = (WINDOW_WIDTH/2 + 100, 10)

gameover_text = font.render(
    f"Game Over\nPress any Key To continue...", True, (255, 0, 0))
gameover_rect = gameover_text.get_rect()
gameover_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)


mysound = pygame.mixer.Sound("sound.wav")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 64:
        player_rect.y -= 5
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += 5

    egg_rect.x -= 5
    if egg_rect.x < 0:
        mysound.play()
        lives -= 1
        egg_rect.center = (WINDOW_WIDTH + 100,
                           random.randint(100, WINDOW_HEIGHT-100))

    if player_rect.colliderect(egg_rect):
        score += 1
        egg_rect.center = (WINDOW_WIDTH + 100,
                           random.randint(100, WINDOW_HEIGHT-100))

    if lives == 0:
        display_surface.blit(gameover_text, gameover_rect)
        pygame.display.update()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    is_paused = False
                    lives = 3
                    score = 0

                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    score_text = font.render(f"score:{score}", True, (255, 0, 0))
    lives_text = font.render(f"Lives:{lives}", True, (255, 0, 0))
    display_surface.fill(BLACK)
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(score_text, score_rect)

    pygame.draw.line(display_surface, WHITE, (0, 64), (WINDOW_WIDTH, 64), 4)

    display_surface.blit(player_image, player_rect)
    display_surface.blit(egg_image, egg_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
