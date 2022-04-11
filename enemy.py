import pygame

import config
from objectMobile import ObjectMobile


class Enemy(ObjectMobile):

    def __init__(self):
        self.speed = 2
        self.img_right = []
        self.img = config.image_soldier
        super().__init__(self.img, self.img_right)
        self.index = 0
        self.animation()
        self.behavior()

    def attack(self):
        pass

    def attack_animate(self):
        pass

    def animation(self):
        for num in range(1, 7):
            img_right = pygame.image.load(f'animation/soldier/soldier_walk_{num}.png')
            img_right = pygame.transform.scale(img_right, (config.quadrant_size, config.quadrant_size))
            self.img_right.append(img_right)

    def reverse(self):
        self.direction.x *= -1

    def update_status(self):
        if self.direction.x != 0:
            self.status = "run"

    def behavior(self):
        if self.rect.x < config.SCREEN_WIDTH/2:
            self.move('right')
        if self.rect.x > config.SCREEN_WIDTH/2:
            self.reverse()


