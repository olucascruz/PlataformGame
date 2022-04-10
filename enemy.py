import pygame

import config
from objectMobile import ObjectMobile


class Enemy(ObjectMobile):

    def __init__(self):
        speed = 2
        self.img = config.image_zombie
        super().__init__(self.img, speed)
        self.img_right = []
        self.img_left = []
        self.index = 0
        self.status = 'stopped'
        self.animation()

    def animation(self):
        for num in range(1, 7):
            img_right = pygame.image.load(f'animation/soldier_walk_right_{num}.png')
            img_right = pygame.transform.scale(img_right, (config.quadrant_size, config.quadrant_size))
            self.img_right.append(img_right)

            img_left = pygame.image.load(f'animation/soldier_walk_right_{num}.png')
            img_left = pygame.transform.scale(img_left, (config.quadrant_size, config.quadrant_size))
            img_left = pygame.transform.flip(img_left, True, False)
            self.img_left.append(img_left)

        if self.status != 'stopped':
            self.image = self.img_right[self.index]
