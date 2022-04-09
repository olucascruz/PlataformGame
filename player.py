import pygame
from objectMobile import ObjectMobile
import config


class Player(ObjectMobile):
    def __init__(self, x, y):
        self.speed = 4
        super().__init__(config.image_player, self.speed)
        self.rect.x = x
        self.rect.y = y

    def attack(self):
        pass