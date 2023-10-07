import pygame
import random
pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
FPS = 60
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

score = 0
font = pygame.font.SysFont("Arial",30)
score_text = font.render(f"Score: {score}", True, (255,255,255))
score_rect = score_text.get_rect(topleft=(10,10))

dog_image_left = pygame.image.load("dog.png")
dog_image_right = pygame.transform.flip(dog_image_left, True, False)


dog = dog_image_right
dog_rect = dog.get_rect()
dog_rect.bottom = WINDOW_HEIGHT
dog_rect.centerx = WINDOW_WIDTH/2

dog_normal_velocity = 5
dog_fast_velocity = 10
dog_velocity = dog_normal_velocity


burger = pygame.image.load("burger.png")
burger_rect = burger.get_rect()
burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -100)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        dog_rect.y -= dog_velocity

    if keys[pygame.K_DOWN]:
        dog_rect.y += dog_velocity

    if keys[pygame.K_LEFT]:
        dog_rect.x -= dog_velocity
        dog = dog_image_left
    if keys[pygame.K_RIGHT]:

        dog_rect.x += dog_velocity
        dog = dog_image_right

    if keys[pygame.K_SPACE]:
        dog_velocity = dog_fast_velocity

    else:
        dog_velocity = dog_normal_velocity


    burger_rect.y += 5

    if burger_rect.y > WINDOW_HEIGHT:
        score -= 1
        burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -100)

    
    if dog_rect.colliderect(burger_rect):
        score += 1
        burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -100)
    
    score_text = font.render(f"Score: {score}", True, (255,255,255))
    
    
    display_surface.fill((0, 0, 0))
    display_surface.blit(dog, dog_rect)
    display_surface.blit(burger, burger_rect)
    display_surface.blit(score_text, score_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
