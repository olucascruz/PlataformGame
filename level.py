import pygame
from plataform import Plataform
import config


class Level:
    def __init__(self, surface, map_data):
        self.surface = surface
        self.setup_level(map_data)

    def setup_level(self, data):
        self.object_list = pygame.sprite.Group()
        row_cont = 0
        for row in data:
            col_cont = 0
            for quadrant in row:
                if quadrant == 1:
                    plataform = Plataform(config.quadrant_size, config.quadrant_size)
                    plataform.rect.x = col_cont * config.quadrant_size
                    plataform.rect.y = row_cont * config.quadrant_size
                    self.object_list.add(plataform)
                col_cont += 1
            row_cont += 1

    def draw(self):
        self.object_list.update(0)
        self.object_list.draw(self.surface)
    


