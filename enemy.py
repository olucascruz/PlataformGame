import pygame

import config
from objectMobile import ObjectMobile


class Enemy(ObjectMobile):

    def __init__(self):
        self.speed = 3
        self.img_right = []
        self.img = config.image_soldier
        super().__init__(self.img, self.img_right)
        self.index = 0
        self.img_attack = []
        self.speed_attack = 0.25
        self.is_attack = False
        self.animation()


    def attack(self, check):
        self.is_attack = check

    def attack_animate(self):
        if self.is_attack:
            self.index += self.speed_attack
            if self.index >= len(self.img_attack):
                self.index = 0
            if self.current_direction == 'right':
                self.image = self.img_attack[int(self.index)]
            elif self.current_direction == 'left':
                self.image = pygame.transform.flip(self.img_attack[int(self.index)], True, False)
        elif not self.is_attack and self.index != 0:
            if self.current_direction == 'right':
                self.image = self.img_attack[0]
            elif self.current_direction == 'left':
                self.image = pygame.transform.flip(self.img_attack[0], True, False)

    def animation(self):
        for num in range(1, 7):
            img_right = pygame.image.load(f'animation/soldier/soldier_walk_{num}.png')
            img_right = pygame.transform.scale(img_right, (config.quadrant_size, config.quadrant_size))
            self.img_right.append(img_right)

        for num in range(1, 4):
            img_attack = pygame.image.load(f'animation/soldier/Soldier_attack_{num}.png')
            img_attack = pygame.transform.scale(img_attack, (config.quadrant_size, config.quadrant_size))
            self.img_attack.append(img_attack)

    def reverse(self):
        self.direction.x *= -1
        self.current_direction = 'left'

    def behavior(self):
        if self.rect.x < config.SCREEN_WIDTH // 2:
            self.move('right')
        if self.rect.x > config.SCREEN_WIDTH // 2:
            self.move('left')

