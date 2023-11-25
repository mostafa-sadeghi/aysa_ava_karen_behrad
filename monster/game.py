import pygame
from monster import Monster
import random
from constants import *
class Game:
    def __init__(self, player, monster_group):
        self.score = 0
        self.player = player
        self.monster_group = monster_group
        self.level_number = 0
        self.font = pygame.font.Font("assets/Abrushow.ttf")


        self.all_images = []
        blue_monster = pygame.image.load("assets/blue_monster.png")
        green_monster = pygame.image.load("assets/green_monster.png")
        orange_monster = pygame.image.load("assets/orange_monster.png")
        purple_monster = pygame.image.load("assets/purple_monster.png")
        self.all_images = [blue_monster, green_monster, orange_monster,
                    purple_monster]

    def start_new_level(self):
        self.level_number += 1
        for i in range(self.level_number):
            for i in range(4):
                Monster(random.randint(0, WINDOW_WIDTH-64), 
                        random.randint(100, WINDOW_HEIGHT-164),
                        self.all_images[i],
                        self.monster_group
                        )
               
    def draw(self,screen):
        score_text = self.font.render(f'Score:{self.score}', True, (247, 13,168))
        score_rect = score_text.get_rect(topleft = (10, 10))
        screen.blit(score_text, score_rect)

        #TODO  نمایش جان بازیکن در صفحه
        #TODO  نمایش شماره مرحله بازیکن در صفحه
        #TODO  نمایش شماره مرحله بازیکن در صفحه

        pygame.draw.rect(screen, (247, 13,168), (0,100,WINDOW_WIDTH, WINDOW_HEIGHT-200),4)
