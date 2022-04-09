import pygame
from objectMobile import ObjectMobile
import config


class Player(ObjectMobile):
    def __init__(self, x, y, size_x, size_y):
        super().__init__()
        self.image = pygame.transform.scale(config.image_player, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = x
        self.rect.y = y
        self.speed = 4
        