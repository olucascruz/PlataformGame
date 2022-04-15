import pygame
from block import Block
from enemy import Enemy
import config


class Level:
    def __init__(self):
        self.object_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.map_data = config.map_data
        self.setup_level()

    def setup_level(self):
        row_cont = 0
        for row in self.map_data:
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
                    enemy.behavior()
                    self.object_list.add(enemy)
                    self.enemy_list.add(enemy)
                col_cont += 1
            row_cont += 1

    def add_enemy(self):
        if len(self.enemy_list) == 1:
            self.object_list.empty()
            self.map_data = config.map_data2
            self.map_data[0][0] = 2
            self.map_data[0][1] = 2
            self.map_data[0][10] = 2
            self.map_data[0][11] = 2
            self.setup_level()

    def update(self):
        self.add_enemy()

