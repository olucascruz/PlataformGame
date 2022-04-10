import pygame
from objectGame import ObjectGame


class ObjectMobile(ObjectGame):
    def __init__(self, img, speed):
        super().__init__(img)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = speed
        self.index = 0

    def move(self, movement):

        if movement == 'right':
            self.direction.x = 1
        elif movement == 'left':
            self.direction.x = -1

        elif movement == 'clear':
            self.direction.x = 0

        if movement == "jump":
            self.direction.y = -15

    def apply_gravity(self):
        gravity = 0.8
        self.direction.y += gravity
        if self.direction.y > 10:
            self.direction.y = 10
        self.rect.y += self.direction.y

    def update(self):
        self.apply_gravity()
        self.rect.x += self.direction.x * self.speed

        self.index += 0.25
        if self.index >= len(self.img_right):
            self.index = 0
        if self.direction.x > 0:
            self.image = self.img_right[int(self.index)]
        elif self.direction.x < 0:
            self.image = self.img_left[int(self.index)]
