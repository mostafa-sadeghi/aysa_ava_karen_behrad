import pygame
from player import Player
from constants import *
from monster import Monster
import random
from game import Game
pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

monster_group = pygame.sprite.Group()
my_player = Player()

my_game = Game(my_player, monster_group)
my_game.start_new_level()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    my_player.draw(screen)
    monster_group.update()
    monster_group.draw(screen)
    my_game.draw(screen)
    pygame.display.update()
    clock.tick(FPS)

