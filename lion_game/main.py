import pygame
pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("lion game")
FPS = 60
clock = pygame.time.Clock()
icon = pygame.image.load("lion.png")
pygame.display.set_icon(icon)

lion = icon
lion_rect = lion.get_rect()
lion_rect.bottom = WINDOW_HEIGHT
lion_rect.centerx = WINDOW_WIDTH/2

pygame.mixer.music.load("bgsound.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

font = pygame.font.Font("myfont.otf",48)
game_title = font.render("My Game", True, (255, 0, 0))
game_title_rect = game_title.get_rect()
game_title_rect.top = 0
game_title_rect.centerx = WINDOW_WIDTH/2


running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(lion, lion_rect)
    screen.blit(game_title, game_title_rect)
    pygame.display.update()
