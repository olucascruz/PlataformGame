import pygame

import config
from objectMobile import ObjectMobile


class Enemy(ObjectMobile):
    def __init__(self):
        self.speed = 2
        super().__init__(config.image_zombie, self.speed)
