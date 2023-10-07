import pygame
pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("lion game")
FPS = 60
clock = pygame.time.Clock()
icon = pygame.image.load("lion_game/lion.png")
pygame.display.set_icon(icon)


pygame.mixer.music.load("lion_game/bgsound.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




