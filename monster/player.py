import pygame
from pygame.sprite import Sprite
from constants import *


class Player(Sprite):
    def __init__(self):
        self.image = pygame.image.load("assets/knight.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH/2
        self.rect.bottom = WINDOW_HEIGHT
        self.catch_sound = pygame.mixer.Sound("assets/catch.wav")
        self.die_sound = pygame.mixer.Sound("assets/die.wav")

        self.lives = 3
        self.speed = 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        #TODO حرکت بازیکن
        pass
