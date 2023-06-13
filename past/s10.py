import pygame
PURPLE = (235, 52, 232)
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
xposition = 0
yposition = 0
x_change = 1
y_change = 1
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pygame.draw.rect(screen, PURPLE, [xposition, yposition, 10, 10])
    xposition = xposition + x_change
    yposition = yposition + y_change

    if yposition > 490 or yposition < 0:
        y_change = -1 * y_change

    if xposition > 690 or xposition < 0:
        x_change = -1 * x_change

    pygame.display.flip()
    clock.tick(1000)
