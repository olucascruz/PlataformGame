import pygame
from objectMobile import ObjectMobile
import config


class Player(ObjectMobile):
    def __init__(self, x, y):
        self.img_right = []
        img = config.image_player
        self.speed = 5
        super().__init__(img, self.img_right)
        self.rect.x = x
        self.rect.y = y
        self.is_attack = False
        self.img_attack = []
        self.animation()
        self.index = 0
        self.speed_attack = 0.25
        self.update_status()

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
        for num in range(1, 4):
            img_right = pygame.image.load(f'animation/player/player_walk_{num}.png')
            img_right = pygame.transform.scale(img_right, (config.quadrant_size, config.quadrant_size))
            self.img_right.append(img_right)

        for num in range(1, 4):
            img_attack = pygame.image.load(f'animation/player/player_attack_{num}.png')
            if 4 > num > 1:
                img_attack = pygame.transform.scale(img_attack, (config.quadrant_size+40, config.quadrant_size))
            else:
                img_attack = pygame.transform.scale(img_attack, (config.quadrant_size, config.quadrant_size))
            self.img_attack.append(img_attack)


