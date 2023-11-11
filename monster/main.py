import pygame
from player import Player
from constants import *
from monster import Monster
import random
pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

monster_group = pygame.sprite.Group()

all_images = []
blue_monster = pygame.image.load("assets/blue_monster.png")
green_monster = pygame.image.load("assets/green_monster.png")
orange_monster = pygame.image.load("assets/orange_monster.png")
purple_monster = pygame.image.load("assets/purple_monster.png")
all_images = [blue_monster, green_monster, orange_monster,
               purple_monster]

for i in range(4):
    Monster(random.randint(0, WINDOW_WIDTH-64), 
            random.randint(100, WINDOW_HEIGHT-164),
            all_images[i],
            monster_group
            )
my_player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    my_player.draw(screen)
    monster_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
