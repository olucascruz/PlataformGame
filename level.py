import pygame
from plataform import Block
from enemy import Enemy
import config


class Level:
    def __init__(self, map_data):
        self.object_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.setup_level(map_data)

    def setup_level(self, data):
        row_cont = 0
        for row in data:
            col_cont = 0
            for quadrant in row:
                if quadrant == 1:
                    block = Block()
                    block.rect.x = col_cont * config.quadrant_size
                    block.rect.y = row_cont * config.quadrant_size
                    self.object_list.add(block)
                if quadrant == 2:
                    enemy = Enemy()
                    enemy.rect.x = col_cont * config.quadrant_size
                    enemy.rect.y = row_cont * config.quadrant_size
                    self.enemy_list.add(enemy)
                col_cont += 1
            row_cont += 1




