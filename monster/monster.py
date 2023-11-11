from pygame.sprite import Sprite
import pygame
import random
class Monster(Sprite):
    def __init__(self, x, y, image, monster_group):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = random.randint(1,5)
        monster_group.add(self)
