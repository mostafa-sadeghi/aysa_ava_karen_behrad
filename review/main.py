import pygame

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700


display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
FPS = 60
clock = pygame.time.Clock()

wolf_image = pygame.image.load("wolf.png")
wolf_rect = wolf_image.get_rect()
wolf_rect.bottom = WINDOW_HEIGHT
wolf_rect.right = WINDOW_WIDTH

sheep_image = pygame.image.load("sheep.png")
sheep_image = pygame.transform.flip(sheep_image, True, False)
sheep_rect = sheep_image.get_rect()
sheep_rect.bottom = WINDOW_HEIGHT
sheep_rect.x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and wolf_rect.top > 0:
        wolf_rect.y -= 5

    if keys[pygame.K_DOWN] and wolf_rect.bottom < WINDOW_HEIGHT:
        wolf_rect.y += 5

    if keys[pygame.K_LEFT] and wolf_rect.left > 0:
        wolf_rect.x -= 5

    if keys[pygame.K_RIGHT] and wolf_rect.right < WINDOW_WIDTH:
        wolf_rect.x += 5

    if keys[pygame.K_d]:
        sheep_rect.x += 5

    display_surface.fill((0,0,0))
    display_surface.blit(wolf_image, wolf_rect)
    display_surface.blit(sheep_image, sheep_rect)
    pygame.display.update()
    clock.tick(FPS)
