import config
import pygame
from objectGame import ObjectGame

class Plataform(ObjectGame):
    def __init__(self, size_x, size_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(config.image_grass, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = size_x
    
    def update(self, prox):
        self.rect.x += prox