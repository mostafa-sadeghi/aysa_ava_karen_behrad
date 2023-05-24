import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((700,500))
clock = pygame.time.Clock()

pos_x = 0
pos_y = 0
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    pygame.draw.rect(screen,GREEN, [pos_x, pos_y, 10,10])
    pos_x += 1
    pos_y += 1
    pygame.display.flip()
    clock.tick(20)