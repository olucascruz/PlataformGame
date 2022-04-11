import pygame
from objectGame import ObjectGame


class ObjectMobile(ObjectGame):
    def __init__(self, img, img_animate):
        super().__init__(img)
        self.direction = pygame.math.Vector2()
        self.index = 0
        self.current_direction = None
        self.image_animate = img_animate
        self.status = "stopped"

    def update_status(self):
        if self.direction.y < 0:
            self.status = "jumped"
        elif self.direction.y > 1:
            self.status = "fall"
        else:
            self.status = "stopped"

    def move(self, movement):

        if movement == 'right' and self.status != "fall":
            self.direction.x = 1
            self.current_direction = 'right'
        elif movement == 'left' and self.status != "fall":
            self.direction.x = -1
            self.current_direction = 'left'

        elif movement == 'clear':
            self.direction.x = 0

        if movement == "jump" and self.status != "jumped":
            self.direction.y = -15

    def apply_gravity(self):
        gravity = 0.8
        self.direction.y += gravity
        if self.direction.y > 10:
            self.direction.y = 10
        self.rect.y += self.direction.y

    def update(self):
        self.attack_animate()
        self.apply_gravity()
        self.rect.x += self.direction.x * self.speed
        self.index += 0.1

        if self.index >= len(self.image_animate):
            self.index = 0
        if self.direction.x > 0:
            self.image = self.image_animate[int(self.index)]
        elif self.direction.x < 0:
            self.image = pygame.transform.flip(self.image_animate[int(self.index)], True, False)

        self.update_status()


